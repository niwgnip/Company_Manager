class Employee:    
    def __init__(self, employee_name, payment = 0):
        self.employee_name = employee_name
        self.payment = payment

    def calculate_salary(self):
        pass

    def __str__(self):
        return f"Employee's name: {self.employee_name}\nSalary: {self.payment}PLN\n"

class HourlyEmployee(Employee):
    
    def __init__(self, employee_name, hourly_rate, weekly_working_hours, position = 'Hourly Employee'):
        Employee.__init__(self, employee_name)
        self.hourly_rate = hourly_rate
        self.weekly_working_hours = weekly_working_hours
        self.position = position
        
    def calculate_salary(self):
        result = self.weekly_working_hours*self.hourly_rate
        return result
     
    def change_hourly_rate(self, new_rate):
        self.hourly_rate = new_rate
    
    def __str__(self):
        return super().__str__() + f"Position: {self.position}\n"

class SalariedEmployee(Employee):
    """Input name (string), age(int), salary per week (number)"""
    
    def __init__(self, employee_name, weekly_salary, position = 'Salaried Employee'):
        Employee.__init__(self, employee_name)
        self.weekly_salary = weekly_salary
        self.position = position

    def calculate_salary(self):
        return self.weekly_salary

    def __str__(self):
        return super().__str__() + f"Position: {self.position}\n"
            
class Manager(SalariedEmployee):
    """""Input name(string), age (int), salary_weekly (number)"""""

    def __init__(self, employee_name, weekly_salary, comission, position = "Manager"):
        SalariedEmployee.__init__(self, employee_name, weekly_salary)
        self.comission = comission
        self.position = position       
        
    def calculate_salary(self):
        basic = super().calculate_salary()
        return basic + self.comission

    def __str__(self):
        return super().__str__()
        
class Executive(Employee):
    
    def __init__(self, employee_name, weekly_salary, comission, position = "Executive"):
        Manager.__init__(self, employee_name, weekly_salary, comission)
        self.position = position

    def calculate_salary(self):
        return int(self.weekly_salary) + int(self.comission)

    def __str__(self):
        return super().__str__() + f"Position: {self.position}\n"