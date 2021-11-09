import dropbox

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
        access_token = 'sl.A7_TPBbjwnPQQiPuqPj9b4W407Cche879W_C_C70y6POh8vKxyBz3ym6cFNF2UEgDLkDJovsnMkJQsENUfFjaPyU05j5Kjcok8C49Il4xE3jOp0AFsfLALF46s_OCJki90Lv3zNz0so'
        transfer_Data = TransferData(access_token)

        file_from = input("Enter the file path to Transfer -")
        file_to = input("Enter the full path to transfer files to dropbox - ")

        transfer_Data.upload_file(file_from, file_to)
        print("File has been moved!!")


main()