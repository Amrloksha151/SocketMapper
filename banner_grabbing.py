import socket

class Grabbing:
    def __init__(self, target, port, protocol):
        self.target = target
        self.port = port
        self.protocol = protocol

    def grab(self):
        request = "GET / HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0\r\n\r\n" % self.target
        if self.protocol == "TCP":
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.target, self.port))
            client.send(request.encode())
            data = client.recv(4096)
        elif self.protocol == "UDP":
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client.sendto(request.encode(), (self.target, self.port))
            data = client.recvfrom(4096)
        return data.decode()

    def save(self):
        with open("banner.txt", "w") as file:
            file.write(self.grab())

    