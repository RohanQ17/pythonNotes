def add(*args):
    sum =0
    for i in args:
        sum +=i
    return sum

# *args packs multiple arguments in a tuple
# **kwargs packs elements into a dictionary
print(add(1,2,3,4,5))


num = 3.2459

print("the number is : {:.2f}".format(num))