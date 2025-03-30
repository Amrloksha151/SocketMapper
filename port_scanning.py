import socket
import threading
import ttkbootstrap as ttk

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
        #client.settimeout(0.3)
        for port in range(self.start, self.stop + 1):
            if not bool(client.connect_ex((self.host, port))):
                self.results.append("%s is open" % port)
                self.window.after(0, lambda p=port: self.connectionLabel.configure(text=f"Port {p} is open", foreground="green"))
            else:
                self.window.after(0, lambda p=port: self.connectionLabel.configure(text=f"Port {p} is closed", foreground="red"))
        self.window.after(0, lambda: self.connectionLabel.configure(text="Scan completed!", foreground="black"))
        self.window.after(3000, lambda: self.connectionLabel.destroy())
        client.close()
        self.save()
    
    def start_connection(self, window):
        self.window = window
        self.connectionLabel = ttk.Label(
            master=window, text="Scanning %s" % self.host, font="Chiller 18 bold", foreground="blue"
        )
        self.connectionLabel.pack(pady=40)
        window.after(1000, lambda: threading.Thread(target=self.scan(), daemon=True).start())
        

    def save(self):
        if self.txt:
            with open("%s.txt" % self.host, "w") as file:
                file.write("$Open Ports$\n")
                for result in self.results:
                    file.write(result)
        if self.csv:
            with open("%s.csv" % self.host, "w") as file:
                file.write("Port,State\n")
                port = self.start
                for result in self.results:
                    file.write("%s,Open\n" % port)
                    port += 1

        if not (self.csv or self.txt):
            for result in self.results:
                print(result)

    def multithreadedScan(self): ...

    def __str__(self):
        return "Port Scanning --> use scan method for normal scanning and multithreaded for faster scanning"
