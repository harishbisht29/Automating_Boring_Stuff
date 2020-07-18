# This python module will record mouse movements. The recorded movements can pe played by 
# MousePlay module.

from pynput import mouse
from pyautogui import confirm
from StorageController import StorageController
import sys

class MouseRecorder:
    def __init__(self, storage_file):
        #Setting storage file. 
        self.storage= StorageController(storage_file)

    # This is a mouse mouse even lister function. 
    # It will be called when mouse's cursor is moved.
    def onMouseMove(self, x, y):
        a= {"source":"Mouse",
        "action":"Move",
        "coordinate":str((x,y))}
        print(a)
        self.storage.store(a)
    
    # This method will execute when mouse is clicked
    def onMouseClick(self, x, y, button, pressed):
        mouse_button= "L" if button == mouse.Button.left else  "R"
        is_pressed= "Y" if pressed else "N"
        coordinate= str((x,y))
        self.storage.store({
            "source":"Mouse",
            "action":"Click",
            "isPressed": is_pressed,
            "coordinate": coordinate
        })

# main module of MouseRecord
if __name__ == '__main__':
    print("---MouseRecord Main Method---")
    buttons= ['Record','Quit']
    
    mRecorder= MouseRecorder("storage")
    input= confirm("Mouse Automation",buttons=buttons )
    
    if input == buttons[0]:
        # Creating mouse events. on_move event will call the function whenever mouse moves.
        listener= mouse.Listener(
            on_move= mRecorder.onMouseMove,
            on_click=mRecorder.onMouseClick
            )
        # starting the listener thread. 
        listener.start()

        # Main thread Waiting for user to stop recording.
        input= confirm("Mouse Automation",buttons=["Stop Recording","Quit"])
        
        if input== "Stop Recording":
            mRecorder.storage.close()
            print("Stopping Recording")
            listener.stop()
            sys.exit(0)
    

    