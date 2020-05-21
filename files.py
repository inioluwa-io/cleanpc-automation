import os,re,time, datetime
            
class Clean():
    def __init__(self):
        self.FILEPATH = input('Enter file absolute directory: ')

        if os.path.exists(self.FILEPATH) is not True:
            print("File path does not exist")
            exit()


    def deleteUnusedFiles(self):
        difference = input('Delete unaccessed file from how many months ago: ')

        NOWTIME = datetime.datetime.today()

        for (dirname, _, files) in os.walk(self.FILEPATH):
            for filename in files:
                FILEDETAILS = os.stat(os.path.join(dirname, filename))
                LASTACCESSLOCALTIME = time.localtime(FILEDETAILS.st_atime)
                # calculate the number of months between today and last accessed date
                monthdifference = (NOWTIME.year - LASTACCESSLOCALTIME.tm_year) * 12 + (NOWTIME.month - LASTACCESSLOCALTIME.tm_mon)
                if(monthdifference >= int(difference)):
                    os.remove(os.path.join(dirname, filename))
                    print(f"{filename} Deleted!!")
                    

Clean().deleteUnusedFiles()
