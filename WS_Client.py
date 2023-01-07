import websocket as ws


class WS_Client:
    PORT = 8080
    def __init__(self, address):
        self.uri = 'ws://' + address + ':' + str(self.PORT)
        self.client = None

    def connect(self):
        self.client = ws.WebSocketApp(self.uri, on_message=self.on_message, on_error=self.on_error, on_close=self.on_close)
    def send(self, event):
        print(event)

    def on_error(self, socket, error):
        print(error)
        return

    def on_message(self, socket, message):
        print(message)
        return

    def on_close(self, socket):
        return


def main():
    print('start')
    test = WS_Client('10.0.0.26')
    print('after instantiation')
    test.connect()

    print(type(test.client))

main()