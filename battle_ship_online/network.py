import socket
import pickle
import time


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.1.230"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.game_data = self.connect()
        self.game_data = pickle.loads(self.game_data)

    def connect(self):
        """
        connect with server
        """
        self.client.connect(self.addr)
        return self.client.recv(4096 * 8)

    def disconnect(self):
        """
        disconnect from server
        """
        self.client.close()

    def send(self, data, pick=False):
        """
        :param data: str
        :return: str
        """
        start_time = time.time()
        while time.time() - start_time < 5:
            try:
                if pick:
                    self.client.send(pickle.dumps(data))
                else:
                    self.client.send(str.encode(data))
                reply = self.client.recv(4096 * 8)
                try:
                    reply = pickle.loads(reply)
                    break
                except Exception as e:
                    print(e)

            except socket.error as e:
                print(e)

        return reply