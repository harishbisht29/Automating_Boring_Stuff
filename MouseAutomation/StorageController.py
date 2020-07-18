# This class will handel all the storage activities. Bascially it will help in storing
# all the mouse and keyborad actions.

from os.path import exists
import json

class StorageController:

    def __init__(self, file):
        if exists(file):
            print("Storage file named {} already exists. Truncating its contents..".format(file))
            open(file, "w+").close()
        self.storage= open(file,"a+")
        self.data = []
    # store function will store movement to storage file
    def store(self, movement):
        self.data.append(movement)

    #close storage file 
    def close(self):
        # Store all the recordings to json file
        json.dump(self.data, self.storage, indent=4)
        self.storage.close()

    def __del__(self):
        self.storage.close()  

if __name__ == '__main__':
    storage= StorageController("storage")
    movement= {'source':'Mouse',
    'action':'Pressed',
    'detail':str((3,4))}
    storage.store(movement)
    
