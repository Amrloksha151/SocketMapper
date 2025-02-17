import socket

class Scanning:
    def __init__(self, protocol, host, start, stop):
        self.protocol = protocol
        self.host = host
        self.start = start
        self.stop = stop
    
    def scan(self):
        if self.protocol == 'TCP':
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for port in range(start=self.start, stop=self.stop):
            try:
                client.connect((self.host, port))
            except Exception:
                yield 'Closed'
            else:
                yield 'Open'
    
    def multithreadedScan(self):
        ...
    
    def __str__(self):
        return 'Port Scanning --> use scan method for normal scanning and multithreaded for faster scanning'
        