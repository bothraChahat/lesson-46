#Write a program to create a class with the name employee and create a constructor and destructor. Then, create an object for that class and delete the object.

class Employee:
    #contructor
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    #destructor
    def __del__(self):
        print("calling destructor to delete the objective")

empl=Employee("Akaay","100k")
print("Employee {} has salary {} per month".format(empl.name,empl.salary))
del empl




