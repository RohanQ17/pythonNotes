# if __name__ == '__main__'

# y tho , 1.module can be run as a standalone program
# or module can be imported and used by other modules

#python interpreter sets "special variables", one of which is __name__
#python will assign the __name__ variable a value of '__main__'
#if its the initial module being run

if __name__ == '__main__':
    print("running this module directly")
else: print("running other module indirectly")

