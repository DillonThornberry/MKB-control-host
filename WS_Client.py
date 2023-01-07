import websockets as ws
import asyncio


class WS_Client:
    PORT = 8080
    def __init__(self, address):
        self.uri = 'ws://' + address + ':' + str(self.PORT)
        self.client = None

    def connect(self):
        self.client = ws.connect(self.uri)

        return self.client


    def on_message(self, socket, message):
        print(message)
        return


