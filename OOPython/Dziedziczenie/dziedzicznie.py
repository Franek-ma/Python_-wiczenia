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
    
class Student2(Person):
    def get_name(self):
        return "Student2" + self.name


class Student3(Person):
    def __init__(self,age,gender,name,python_skills):
        self.python_skills = python_skills
        super().__init__(age,gender,name)

    def describe(self):
        return [self.name,self.age,self.gender,self.python_skills]



mat = Person(41,"m","Mateusz") 
fra = Student(13,"m","Franciszek")
thrd = Student2(13,"m","Dominika")

super1 = Student3(25,"m","Bartek",5)



print(fra.get_name())
print(thrd.get_name())
print(super1.describe())



