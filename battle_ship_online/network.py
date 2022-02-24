import socket
import pickle

class Network:
    def __init__(self, name):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.97"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.name = name
    
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048*5))
        except:
            print("OOOOPS")
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*5))
        except socket.error as e:
            print("FAIL")
            print(e)

    def disconnect(self):
        print("[EXCEPTION] Disconnected from server")