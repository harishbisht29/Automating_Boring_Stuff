# This class will handel all the storage activities. Bascially it will help in storing
# all the mouse and keyborad actions.

from os.path import exists

class StorageController:

    def __init__(self, file, dlm='__'):
        if exists(file):
            print("Storage file named {} already exists. Truncating its contents..".format(file))
            open(file, "w+").close()
        self.storage= open(file,"a+")
        self.dlm= dlm

    # store function will store movement to storage file
    def store(self, movement):
        source= movement['source']
        action= movement['action']
        detail= movement['detail']
        fline=  source + self.dlm + action + self.dlm + detail
        self.storage.write(fline+ "\n")

    #close storage file 
    def close(self):
        self.storage.close()

    def __del__(self):
        self.storage.close()  

if __name__ == '__main__':
    storage= StorageController("storage")
    movement= {'source':'Mouse',
    'action':'Pressed',
    'detail':str((3,4))}
    storage.store(movement)
    
