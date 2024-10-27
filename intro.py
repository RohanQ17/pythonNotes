
name = "bro"
age = 19
print("hello " + name)
#print(type(name))
print(type(age))
print("your age is : "+ str(age))  #typecasting
# you cannot concat diff data types but can convert it into suitable one and then cat
height = 175.5
print(type(height))
age_1 = 'a'             #a single char is also a string
print(type(age_1))
human = True   # in py only use Truth n False for bool not 0 or 1
print(type(human))


#multiple assignment
name,age,attractive = "rohan",20,True
spongebob=patrick=sandy = 300

for i in range( 1, 11):
    if i == 7:
       pass;
    print(i)