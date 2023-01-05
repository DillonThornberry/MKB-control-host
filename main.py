import numpy as np
import keyboard as kb
from pynput import mouse
import asyncio
import websockets as ws
import pyglet

ACTIVATE_HOTKEY = 'alt+x'
PORT = 8080

isActive = False   # Boolean for whether to actively listen for mkb inputs
kb.add_hotkey(ACTIVATE_HOTKEY, lambda: flipActive())  # Listens for hotkey to turn listeners on or off
mouseListener = None  # Event listener to mouse movements
controller = mouse.Controller()  # Controller to move mouse
lastPosition = np.array(controller.position)  # Stores last location of mouse on screen
window = None
window = pyglet.window.Window(caption='Controlling other PC')

def startListeners():
    global mouseListener
    global window

    # window = pyglet.window.Window(caption='Controlling other PC') # fullscreen=True, style=pyglet.window.Window.WINDOW_STYLE_TRANSPARENT,

    # Start event listener for mouse actions
    mouseListener = mouse.Listener(
        on_move=onMove,
        on_scroll=onScroll,
        on_click=onClick
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




def onMove(x, y):
    global lastPosition
    newPosition = np.array((x, y))
    deltaPosition = newPosition - lastPosition
    #print(deltaPosition)
    lastPosition = newPosition


def onScroll(x, y, dx, dy):
    print(dx, dy)
    #controller.scroll(-dx, -dy)


def onClick(x, y, button, pressed):
    return


async def main():
    async with ws.serve(None, "", PORT):
        await asyncio.Future()


if __name__ == '__main__':
    asyncio.run(main())