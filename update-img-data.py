import os
import glob
import pexif
from os.path import basename

def main():
    # Set Var
    ext = ".jpeg"
    # Set Path to Image Directory
    path = getPath()
    cpath = raw_input("Is this the correct path to your Image Directory? (Y/N): ")
    while inputValidator(cpath):
        cpath = raw_input("Is this the correct path to your Image Directory? (Y/N): ")
    while cpath == 'n':
        path = getPath()
        cpath = raw_input("Is this the correct path to your Image Directory? (Y/N): ")
    # Set .txt file containing keywords
    txtFile = getTxtFile()
    ctxt = raw_input("Is this the correct .txt file containing your keywords? (Y/N): ")
    while inputValidator(ctxt):
        ctxt = raw_input("Is this the correct .txt file containing your keywords? (Y/N): ")
    while ctxt == 'n':
        txtFile = getTxtFile()
        cTxt = raw_input("Is this the correct .txt file containing your keywords? (Y/N): ")
    # Set image to sample Exfit Data
    exData = getExfit()
    cEx = raw_input("Is this the image with the correct Exfit Data? (Y/N): ")
    while inputValidator(cEx):
        cEx = raw_input("Is this the image with the correct Exfit Data? (Y/N): ")
    while cEx == 'n':
        exData = getExfit()
        cEx = raw_input("Is this the image with the correct Exfit Data? (Y/N): ")
    # Test
    print("Path = " + str(path))
    print(".txt = " + str(txtFile))
    print("Image Sample = " + str(exData))
    backup = raw_input("Have you backed up your images? (Y/N): ")
    while inputValidator(backup):
       backup = raw_input("Have you backed up your images? (Y/N): ")
    if backup.lower() == 'y':
        print("Ok we will now begin...")
        setData(path, exData, txtFile, ext)
    else:
        print("Please Backup your Images then restart script.")

def getPath():
    print("Please type the path to your Image Directory. Make sure it is in the following format: \nC:/Users/<USER>/Desktop/Images/")
    path = raw_input("PATH = ")
    path = path + "*"
    print(path)
    return path

def getTxtFile():
    print("Please type the name of the .txt file that holds the keywords for the names. \nPlease include the extension. Ex. file.txt ")
    txtFile = raw_input("Text File = ")
    print(txtFile)
    return txtFile

def getExfit():
    print("Please type the name of the image that has the correct Exfit Data: ")
    exData = raw_input("Sample Image = ")
    print(exData)
    return exData

def setData(path, exData, txtFile, ext):
    keywordList = getFile(txtFile)
    # This Image Sets the Exif Data
    img_src = pexif.JpegFile.fromFile(exData)
    i = 0
    for fname in glob.glob(path):
        img_dst = pexif.JpegFile.fromFile(fname)
        img_dst.import_exif(img_src.exif)
        print("Copying Exfit Data into " + basename(fname))
        img_dst.writeFile(keywordList[i] + ext)
        print("Renaming " + basename(fname) + " to " + keywordList[i] + ext)
        i+=1
    print("Successfully added Exfit Data to " + str(i) + " images.")

def inputValidator(n):
    try:
        n = n.lower()
        if n not in ["y", "n"]:
            print("Error Please Type (Y/N).")
            return True
    except ValueError:
        print("Error.")
        return True

def getFile(f):
    keywordList = []
    keywords = open(f, "r")
    #read line into array
    for line in keywords.readlines():
         # loop over the elemets, split by whitespace
        for i in line.split():
            # convert to string and append to the list
            keywordList.append(str(i))
    return keywordList

main()
os.system("pause")
