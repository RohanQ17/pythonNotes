import os
source ="test.txt"
destination = "C:\\Users\\ROHAN\\OneDrive\\Desktop\\test.txt"
try:
    if(os.path.exists(destination)):
        print("there is already a file")
    else:
        os.replace(source,destination)
except FileNotFoundError:
    print("source was not found")


    # ccan be used to change directory as well


    # deleting files
os.remove(destination)


