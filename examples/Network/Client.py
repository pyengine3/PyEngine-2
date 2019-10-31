from pyengine2.Network import Client, Packet


def recieve(packet):
    if packet.datas["type"] == "Chat":
        print(packet.datas["author"], ">", packet.datas["message"])


client = Client("localhost", 25565, recieve)
connected = True

while connected:
    message = input()
    if message == "Bye":
        connected = False
    client.send(Packet({"type": "Chat", "message": message}))
    print("Moi >", message)
client.stop()
