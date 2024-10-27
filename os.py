# file detection
import os
path = "C:\\Users\\ROHAN\\OneDrive\\Desktop\\pp.txt"

if os.path.exists(path):
    print("it does exist")
# os.path.isfile or .isdir to see if its a directory or a file
text = "poptarts"

with open("C:\\Users\\ROHAN\\OneDrive\\Desktop\\pp.txt",'w')as file:
    file.write(text)
with open("C:\\Users\\ROHAN\\OneDrive\\Desktop\\pp.txt")as file:
    print(file.read())

# w overwrites and a appends only
import shutil

#copyfile() copies the content if file
#copy() copies fiole + permission mode + destination can be a directory
#copy2() copy() + copies meta data(files creation and modification time

shutil.copyfile("C:\\Users\\ROHAN\\OneDrive\\Desktop\\pp.txt",'copy.txt')


