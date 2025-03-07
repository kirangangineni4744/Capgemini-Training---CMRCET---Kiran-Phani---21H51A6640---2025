class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  

    def display(self):  
        print("ID:",self.id)
        print("Name:",self.name)

emp1 = Employee("John", 7298)  
emp2 = Employee("David", 7299)  

emp1.display()
emp2.display()