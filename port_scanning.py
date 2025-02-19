import socket
import csv


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
        for port in range(start=self.start, stop=self.stop):
            try:
                client.connect((self.host, port))
            except Exception:
                self.results.append("Closed")
            else:
                self.results.append("Opened")

    def save(self): ...

    def multithreadedScan(self): ...

    def __str__(self):
        return "Port Scanning --> use scan method for normal scanning and multithreaded for faster scanning"
