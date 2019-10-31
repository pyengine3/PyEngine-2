import threading
import socket

from pyengine2.Network.Packet import Packet
from pyengine2.Utils import logger


class Client(threading.Thread):
    def __init__(self, server, clientsocket, ip, identity):
        super(Client, self).__init__()
        self.server = server
        self.clientsocket = clientsocket
        self.ip = ip
        self.identity = identity
        self.connected = True

    def run(self):
        logger.info("New Client. ID : "+str(self.identity) + ". IP : "+str(self.ip))
        while self.connected:
            try:
                r = self.clientsocket.recv(9999999)
                r = Packet.from_recieve(r)
                r.datas["author"] = self.identity
                self.server.recieve(r)
            except (ConnectionResetError, ConnectionAbortedError) as e:
                logger.error("Connection Error : " + str(e))
                self.connected = False
        self.server.quit(self)


class Server(threading.Thread):
    def __init__(self, port):
        super(Server, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(("localhost", port))
        self.clients = []

    def stop(self):
        for i in self.clients:
            i.connected = False
        self.s.close()

    def recieve(self, packet):
        self.sendall(packet)

    def quit(self, client):
        logger.info("End Client. ID : "+str(client.identity) + ". IP : "+str(client.ip))
        self.sendall(Packet({"type": "END", "author": client.identity}))
        self.clients.remove(client)

    def run(self):
        while True:
            self.s.listen(10)
            (clientsocket, (ip, port)) = self.s.accept()
            if len(self.clients):
                tclient = Client(self, clientsocket, ip, self.clients[-1].identity + 1)
            else:
                tclient = Client(self, clientsocket, ip, 0)
            self.clients.append(tclient)
            tclient.start()
            self.sendall(Packet({"type": "NEW", "author": tclient.identity}))

    def send_to(self, identity, packet):
        for i in self.clients:
            if i.identity == identity:
                i.clientsocket.send(packet.to_send())
                break

    def sendall(self, packet):
        for i in self.clients:
            if i.identity != int(packet.datas["author"]) or packet.datas["type"] == "TOALL":
                i.clientsocket.send(packet.to_send())
