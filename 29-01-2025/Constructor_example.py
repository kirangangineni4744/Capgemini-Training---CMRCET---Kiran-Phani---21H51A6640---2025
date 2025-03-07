class Example1:
    def __init__(self,name):
        print(f"First constructor: Hello {name}")

    def __init__(self,age):
        print(f"Second constructor: Age is {age}")

# creating an object
obj=Example1("Kiran")






class Arguments:
    def __init__(self,*args):
        if len(args)==1:
            print(f"Hello {args[0]}")
        elif len(args)==2:
            print(f"Hello {args[0]}, you are {args[1]} years old.")

obj=Arguments("Kiran",21)






class Example2:
    def __init__(self,**kwargs):
        if "name" in kwargs and "age" in kwargs:
            print(f"Hello {kwargs['name']},you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"Hello {kwargs['name']}")
            self.xfield=kwargs['name']   
            
obj1=Example2(name="Kiran",age=22)   