import dropbox
import random
import time
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        number = random.randint(0,100)
        start_time = time.time
        reminder = start_time+number
        reminder>30000 = True
        reminder<30000 = False

        for int in reminder:
            print("Upload School stuff to cloud storage!")
        
        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'ikj62BDZhdAAAAAAAAAAAae7ajjfVl7mRDT28Rcj4esv8I_rF_xGhrcl868YKYRO'
    transferData = TransferData(access_token)

    file_from = input("Enter File Path on PC : ")
    file_to = input("ENter File Path in Dropbox : ")

    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()