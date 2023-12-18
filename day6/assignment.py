import os

try:
        f=input("Enter the file name")
        fh=open(f,"x")
except Exception as e:
        print("File already exists",e)

ask=input("Do you want to write in the files ")

if ask=="yes":
        something=input("Write something you wanna write")
        fh.write(something)
else:
        print(" ")

fh.close()

dele=input("ENter the name fo the file you want to delete")
try:
        os.remove(dele)
except Exception as e:
         print("File doesn't exist", e)
