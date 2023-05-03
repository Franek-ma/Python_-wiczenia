class Employee:
    
    pay_r = 1.1
    number_of_emp = 0

    def __init__(self,name,position, wage):
        self.name = name
        self.position = position
        self.wage = wage
        Employee.number_of_emp += 1

    def pay_rise_company(self):
        self.wage =  self.wage * Employee.pay_r

    def pay_rise_emp(self):
        self.wage =  self.wage * self.pay_r



emp1 = Employee("Tom", "programmer", 4000)

print(emp1.wage)

emp1.pay_rise_company()
emp2 = Employee("Barbra","programmer",3000)

emp2.pay_r = 1.2
emp2.pay_rise_emp()
emp3 = Employee("Patric","dev-ops",5000)


print(emp1.wage)
print(emp2.wage)

print(Employee.number_of_emp)


