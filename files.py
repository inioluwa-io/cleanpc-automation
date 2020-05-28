import os
import re
import time
import datetime


class Clean():
    def __init__(self):
        self.FILEPATH = input('Enter file absolute directory: ')

        if os.path.exists(self.FILEPATH) is not True:
            print("File path does not exist")
            exit()

    def remove_from_filename(self, filename):
        findparenthesis = re.search(r"\([0-9]\)", filename)
        findcopy = re.search(r"- Copy", filename)
        filechange = False
        ext_start_iter = [m.start(0) for m in re.finditer(r"\.", filename)]
        ext_start_index = ext_start_iter[len(ext_start_iter)-1]
        ext = filename[int(ext_start_index):]
        if findparenthesis:
            filename = filename[:(int(findparenthesis.start())-1)]
            filechange = True
        if findcopy:
            filename = filename[:(int(findcopy.start())-1)]
            filechange = True

        if filechange:
            filename = filename+ext

        return filename

    def findAndDeleteDuplicateFiles(self):
        fileslist = list()
        for (dirname, _, files) in os.walk(self.FILEPATH):
            for filename in files:
                # remove appended name from filename
                filenamepath = dirname+self.remove_from_filename(filename)
                filesize = os.stat(os.path.join(dirname, filename)).st_size
                # store file details in list to compare with current obj
                obj = {"path": filenamepath, "size": str(
                    filesize), "filename": filename}
                for file_obj in fileslist:
                    if (filenamepath == file_obj['path']) and (str(filesize) == file_obj['size']):
                        print(f"{filename} Deleted!!!")
                        self.deleteFile(os.path.join(
                            dirname, filename))
                        break
                fileslist.append(obj)

    def deleteFile(self, filepath):
        os.remove(filepath)

    def deleteUnusedFiles(self):
        difference = input('Delete unaccessed file from how many months ago: ')

        NOWTIME = datetime.datetime.today()

        for (dirname, _, files) in os.walk(self.FILEPATH):
            for filename in files:
                FILEDETAILS = os.stat(os.path.join(dirname, filename))
                LASTACCESSLOCALTIME = time.localtime(FILEDETAILS.st_atime)
                # calculate the number of months between today and last accessed date
                monthdifference = (NOWTIME.year - LASTACCESSLOCALTIME.tm_year) * \
                    12 + (NOWTIME.month - LASTACCESSLOCALTIME.tm_mon)
                if(monthdifference >= int(difference)):
                    os.remove(os.path.join(dirname, filename))
                    print(f"{filename} Deleted!!")


Clean().findAndDeleteDuplicateFiles()
