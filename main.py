import numpy as np
import keyboard as kb
from pynput import mouse
import asyncio
import websockets as ws

ACTIVATE_HOTKEY = 'alt+x'
PORT = 8080

isActive = False
kb.add_hotkey(ACTIVATE_HOTKEY, lambda: flipActive())
mouseListener = None


async def main():
    async with ws.serve(None, "", PORT):
        await asyncio.Future()

def startListeners():
    global mouseListener
    mouseListener = mouse.Listener(
        on_move=onMove
    )
    mouseListener.start()

def killListeners():
    global mouseListener
    mouseListener.stop()


def flipActive():
    global isActive
    isActive = not isActive
    if isActive:
        startListeners()
    else:
        killListeners()

controller = mouse.Controller()
lastPosition = np.array(controller.position)
def onMove(x, y):
    global lastPosition
    newPosition = np.array((x, y))
    deltaPosition = newPosition - lastPosition
    print(deltaPosition)
    lastPosition = newPosition






if __name__ == '__main__':
    asyncio.run(main())