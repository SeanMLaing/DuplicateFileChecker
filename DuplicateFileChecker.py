#DuplicateFileChecker
#Sean Laing
#gitbhub.com/seanmlaing
#Oct 22 2019


#Check for duplicate files using a rainbow table

#IMPORTS
from sys import argv
from os.path import exists
import hashlib

#FUNCTIONS DEF

#check the checksum against the rainbow table, if exists alert user, if not write to rainbow table and alert user
def checkRainbowTable(checkFileHash, rainbowTable):
    table = open(rainbowTable)
    hashes = table.read().split('\n')
    if(checkFileHash in hashes):
        print "\n--- Already in table ---"
    else:
        print "\n\n--- New File ---\n"
        table.close()
        append = open(rainbowTable, "a+")
        append.write(checkFileHash)
    #hashes is an array of the hashes in the rainbow table, now need to read through
    #for loop adding to a list to store the hashes of the other files


#do the checksum and return the hash
def runChecksum(checkFile):
    hash_md5 = hashlib.md5()
    with open(checkFile, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
        return hash_md5.hexdigest()

#check if the files (to check and rainbow table) exist in the specified directories
def checkFilesExist(checkFile, rainbowTable):
    print "Checksum file exists: %r" % exists(checkFile)
    print "Rainbow table file exists: %r" % exists(rainbowTable)
    if (exists(checkFile) & exists(rainbowTable)):
        checkFileHash = runChecksum(checkFile)
        print(checkFileHash)
        checkRainbowTable(checkFileHash, rainbowTable)
    else:
        print("One or more input files does not exist.\n")


def checkInputs():
    if len(argv) >= 3:
        #correct number of arguments, set argv values
        script, checkFile, rainbowTable = argv
        checkFilesExist(checkFile, rainbowTable)
    else:
        print("\nIncorrect inputs, enter a file to check and a rainbow table.\nExample:\n\n\tpython DuplicateFileChecker checkFile.txt rainbowTable.txt\n")


#END FUNCTIONS DEF

#START

#run through a check to see if argv inputs have been put in, return error if not
checkInputs()

#END
