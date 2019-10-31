class Packet:
    def __init__(self, datas):
        self.datas = datas

    def to_send(self):
        message = ""
        for k, v in self.datas.items():
            message += str(k)+"(-)"+str(v)
            if k != tuple(self.datas.keys())[-1]:
                message += "(|)"
        return str.encode(message)

    @classmethod
    def from_recieve(cls, recieve):
        message = recieve.decode()
        datas = {}
        for data in message.split("(|)"):
            datas[data.split("(-)")[0]] = data.split("(-)", 1)[1]
        return Packet(datas)
