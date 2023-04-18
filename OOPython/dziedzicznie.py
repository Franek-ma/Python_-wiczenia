class Person:
    def __init__(self,age,gender,name):
        self.name = name
        self.age = age
        self.gender = gender


    def get_name(self):
        return self.name


class Student(Person):
    def get_name(self):
        return "Uczeń : " + self.name
    



mat = Person(41,"m","Mateusz") 
fra = Student(13,"m","Franciszek")


print(fra.get_name())



