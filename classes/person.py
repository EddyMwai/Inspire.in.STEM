class Person:
    def __init__(self, _name, _age):
        self.name= _name
        self.age= _age
    def sayHi(self):
        print("Hello, my name is " + str(self.name) + " and I am " + str(self.age) + " years old.")
person1=Person('Bob',16)
person1.sayHi()
person2=Person('James',24)
person2.sayHi()


###########################3
#have name and salary
class Employee:
    def __init__(self, _name, _salary):
        self.name=_name
        self.salary=_salary
    def say_hello(self):
        print("My name is " + self.name + " I work at a bank salaried Kshs." + self.salary + ".")
employee1=Employee('Dylan Oti', str(24000))
employee1.say_hello()
employee2=Employee('Roddy Rich', str(550000))
employee2.say_hello()

