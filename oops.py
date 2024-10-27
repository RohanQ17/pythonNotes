#duck typing = concept where the class of an object is less important than the methods
#               class type is not checked if minimum no of atttributes ir methods are present
#               if it walks like a duck and quaks like aduck then it must be one\

class Duck:

    def walk(self):
        print("this duck is walking ")

    def talk(self):
        print("this duck is quacking")

class chicken :

    def walk(self):
        print("this chicken is walking ")

    def talk(self):
        print("this chicken is clucking")

class person :

    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")

duck = Duck()
chicken = chicken()
person = person()

person.catch(chicken)

