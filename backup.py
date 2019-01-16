import configparser
import time
import os
import shutil

# Configuration
config = configparser.ConfigParser()
config.read("config.ini")
SOURCE = config.get("Directories","Source")
BACKUP = config.get("Directories","Backup")

# Classes
class File:
    fileCount = 0

    def __init__(self, aName = None, aLocation = None, aModifiedDate = None, aSize = None, aBackupLocation = None):
        self.name = ""
        self.location = ""
        self.modifiedDate = ""
        self.size = ""
        self.backupLocation = ""
        File.fileCount += 1
    
    def setName(self, aName):
        self.name = aName
        
    def setLocation(self, aLocation):
        self.location = aLocation
        self.backupLocation = aLocation.replace(SOURCE, BACKUP)
    
    def setModifiedDate(self, aModifiedDate):
        self.modifiedDate = aModifiedDate
    
    def setSize(self, aSize):
        self.size = aSize
    
    def display(self):
        print("Name: " + self.name)
        print(str(self.location) + "\\" + self.name + ' - ' + str(self.modifiedDate) + " - " + str(self.size))

# Functions
def displayBanner(aString):
    length = len(aString) + 6
    count = 0
    line = ""

    while (count < length):
        line = line + "*"
        count += 1

    print()
    print(line)
    print("*  " + aString.upper() + "  *")
    print(line)
    print()
    return

# Main
if __name__== "__main__":
    displayBanner("Configuration")
    print("Source Directory: " + SOURCE)
    print("Backup Directory: " + BACKUP)  

    displayBanner("Backup: Start")
    startTime = time.time()
    
    # Populate Source File List.
    sourceFileList = []

    for root, dirs, files in os.walk(SOURCE):
        for file in files:
            if (file != "Thumbs.db"):
                aFile = File()
                aFile.setName(file)
                aFile.setLocation(root)
                aFile.setModifiedDate(os.path.getmtime(root + "/" + file))
                aFile.setSize(os.path.getsize(root + "/" + file))
                sourceFileList.append(aFile)
              
    # Backup Files.
    backupCount = 0
    backupSize = 0

    for file in sourceFileList:
        # File exists in backup.
        if (os.path.isfile(file.backupLocation + "\\" + file.name)):
            # File is newer than in backup.
            if (os.path.getmtime(file.backupLocation + "\\" + file.name) < file.modifiedDate):
                # Location of the file doesn't exist in backup.
                if (os.path.exists(file.backupLocation) == False):
                    os.makedirs(file.backupLocation)
                    
                # Backup the file.
                shutil.copy2(file.location + "\\" + file.name, file.backupLocation + "\\" + file.name)
                print("- " + file.name)
                backupCount = backupCount + 1
                backupSize = backupSize + file.size
                
        # File doesn't exist in backup.
        else:
            # Location of the file doesn't exist in backup.
            if (os.path.exists(file.backupLocation) == False):
                os.makedirs(file.backupLocation)
            
            # Backup the file.
            shutil.copy2(file.location + "\\" + file.name, file.backupLocation + "\\" + file.name)
            print("- " + file.name)
            backupCount = backupCount + 1
            backupSize = backupSize + file.size

    totalTime = round(time.time() - startTime, 2)
    displayBanner("Backup: Complete")
    
    # Display runtime statistics.
    print("Run time:       " + str(totalTime) + " seconds.")
    print("Files compared: " + str(File.fileCount))
    print("Files copied:   " + str(backupCount))
    print("                " + str(backupSize) + " bytes.")
            
    input('Press <ENTER> to continue')
    exit()