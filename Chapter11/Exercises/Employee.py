class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = int(annual_salary)

    def give_raise(self, salary_raise=""):
        if salary_raise:
            self.annual_salary = self.annual_salary + int(salary_raise)
            type(self.annual_salary)
        else:
            self.annual_salary = self.annual_salary + 5000
