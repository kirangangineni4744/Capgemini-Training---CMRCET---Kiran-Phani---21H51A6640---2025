# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def display(self):
#         print(f"This car is a {self.brand}'s {self.model}.")

# car1=Car("Toyota","Hyundai")
# car2=Car("Suzuki","Swift")
# car1.display()
# car2.display()





class Employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
        
    def set_salary(self,salary):
        self._salary=salary

    def get_salary(self):
        return self._name,self._salary

emp=Employee("Alice",50000)
print(f"Salary before update:\n",emp.get_salary())
emp.set_salary(55000)
print(f"Salary after update:\n",emp.get_salary())
