import time

name = input("whats yo name ")
print(len(name))
print(name.find("e"))
print(name.capitalize())  # only the first letter of the string
name.upper()
name.lower()
print(name.isdigit())   # can check for any data type
name.isalpha()  # if only chars no spaces then returns true
name.count("o")
print(name.replace("o","a"))


# slicing

pname = "sponge bob"
first_name = pname[0:6:1]   # [start:stop:step] stop index is exclusive , can only write a single index
print(first_name)

reversed_name = pname[::-1]
print(reversed_name)
website = "http://apple.com"
slice = slice(7,-4)  # every string has a negative index too so use that -1 as stopping index
print(website[slice])

if len(pname) !=3 :
    print("cool")

for seconds in range(10):
    print(seconds)
    time.sleep(2)

