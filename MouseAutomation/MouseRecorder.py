# This python module will record mouse movements. The recorded movements can pe played by 
# MousePlay module.

from pynput import mouse
from pyautogui import confirm
from StorageController import StorageController
import sys

class MouseRecorder:
    def __init__(self, storage_file):
        self.storage= StorageController(storage_file, dlm='__')

    # This is a mouse mouse even lister function. 
    # It will be called when mouse's cursor is moved.
    def onMouseMove(self, x, y):
        a= {"source":"Mouse",
        "action":"Move",
        "detail":str((x,y))}
        print(a)
        self.storage.store(a)

    # This is mouse click event listener function.
    # It will be called when mouse is clicked or released
    def onMouseClick(self, x, y, click_side, is_pressed):
        s= 'L' if (click_side== mouse.Button.left) else 'R'
        p= 'P' if is_pressed else 'R'

# main module of MouseRecord
if __name__ == '__main__':
    print("---MouseRecord Main Method---")
    buttons= ['Record','Quit']
    
    mRecorder= MouseRecorder("storage")
    input= confirm("Mouse Automation",buttons=buttons )
    
    if input == buttons[0]:
        listener= mouse.Listener(
            on_move= mRecorder.onMouseMove,
            on_click= mRecorder.onMouseClick)
        listener.start()
        input= confirm("Mouse Automation",buttons=["Stop","Quit"])
        if input== "Stop":
            mRecorder.storage.close()
            listener.stop()
            sys.exit(0)
    

    