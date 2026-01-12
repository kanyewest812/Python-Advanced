class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_role(self):
        return "Employee"


class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus

def print_employees(employees):
    for emp in employees:
        print(f"{emp.get_role()} earns {emp.get_salary()} tenge")

emp1 = Employee(120000)
emp2 = Manager(250000, 60000)

staff = [emp1, emp2]

print_employees(staff)
