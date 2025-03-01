import socket

class Scanning:
    def __init__(self, protocol, host, start, stop, txt, csv):
        self.protocol = protocol
        self.host = host
        self.start = start
        self.stop = stop
        self.txt = txt
        self.csv = csv

    def scan(self):
        self.results = []
        if self.protocol == "TCP":
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for port in range(self.start, self.stop):
            try:
                client.connect((self.host, port))
            except Exception:
                self.results.append("Closed")
            else:
                self.results.append("Opened")

    def save(self):
        if self.txt:
            with open('%s.txt' % self.host, "w") as file:
                file.write('Port ::: State')
                for result in self.results:
                    file.write('%s ::: %s' % (self.results.index(result) + self.start, result))
        elif self.csv:
            with open('%s.csv' % self.host, "w") as file:
                file.write('Port,State')
                for result in self.results:
                    file.write('%s,%s' % (self.results.index(result) + self.start, result))
        else:
            for result in self.results:
                    print('%s ::: %s' % (self.results.index(result) + self.start, result))

    def multithreadedScan(self): ...

    def __str__(self):
        return "Port Scanning --> use scan method for normal scanning and multithreaded for faster scanning"
