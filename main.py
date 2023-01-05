import numpy as np
import keyboard as kb
from pynput import mouse
import asyncio
import websockets as ws

isActive = False
kb.add_hotkey('alt+x', lambda: flipActive())


async def main():
    async with ws.serve(None, "", 8080):
        await asyncio.Future()


def flipActive():
    global isActive
    isActive = not isActive
    print("activated" if isActive else "deactivated")

def onMove(x, y):
    print((x, y))



mouseListener = mouse.Listener(
    on_move=onMove
)

mouseListener.start()

if __name__ == '__main__':
    asyncio.run(main())