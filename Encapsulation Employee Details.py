class Employee:
    def __init__(self, name,salary):
        self.__name = name
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

Employee = Employee("john", 500000)
print(f"Salary: {Employee.get_salary()}") 
Employee.set_salary(55000)
print(f"Updated salary:{Employee.get_salary()}")           