import threading
import socket
from pyengine2.Network.Packet import Packet
from pyengine2.Utils import logger


class ClientThread(threading.Thread):
    def __init__(self, client):
        super(ClientThread, self).__init__()
        self.client = client
        self.connected = True

    def run(self):
        while self.connected:
            try:
                r = self.client.s.recv(9999999)
                self.client.recieve(Packet.from_recieve(r))
            except (ConnectionResetError, ConnectionAbortedError, OSError) as e:
                logger.error("Connection Error : " + str(e))
                self.connected = False


class Client:
    def __init__(self, ip, port, callback):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))

        self.t = ClientThread(self)
        self.t.start()

        self.callback = callback

    def stop(self):
        self.t.connected = False
        self.s.close()

    def recieve(self, packet):
        if self.callback is not None:
            self.callback(packet)

    def send(self, packet):
        self.s.send(packet.to_send())
