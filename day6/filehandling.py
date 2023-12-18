f=open("test.txt")
print(f.read())
f.close()
#another method for closing the file
# with open("test.txt") as f:
#     print(f.read())

#use loop in file (assignment)
#use try except(task)



#creating a module
from function import sum

print(sum(1,2))

from function import sum as s

print(s(1,2))
#another method of calling a module

import function

print(function.sum(1,2))

#to delete a file

import os   

os.remove("test.txt")

# ask input from user to create which file ani tyo file create garney ani user lai tyo file ma content halni ho bhanera sodhney ani j bhanxa tei contnt halney file ma ani kun file delete garney user input magney anu tei delete garney
    