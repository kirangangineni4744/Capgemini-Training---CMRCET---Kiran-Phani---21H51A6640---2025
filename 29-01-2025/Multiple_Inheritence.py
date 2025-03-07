# Parent Class-1
class Bird:
    def fly(self):
        return "This bird can fly"

# Parent Class-2
class Mammal:
    def walk(self):
        return "This mammal can walk"

# Child Class
class Bat(Bird,Mammal):
    def dance(self):
        return "Ayudha Pooja"

bat=Bat()
print(bat.fly())
print(bat.walk())
print(bat.dance())


