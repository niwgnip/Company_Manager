class Employee():    
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_salary(self):
        pass

class HourlyEmployee(Employee):
    
    def __init__(self, id, employee_name, hourly_rate, weekly_working_hours):
        Employee.__init__(self, id, employee_name)
        self.hourly_rate = hourly_rate
        self.weekly_working_hours = weekly_working_hours
        
    def calculate_salary(self):
        return self.weekly_working_hours*self.hourly_rate
     
    def change_hourly_rate(self, new_rate):
        self.hourly_rate = new_rate
    
    def employee_raise(self, new_income):
        return SalariedEmployee(self.name, new_income)

class SalariedEmployee(Employee):
    """Input name (string), age(int), salary per week (number)"""
    
    def __init__(self, id, employee_name, weekly_salary):
        Employee.__init__(self, id, employee_name)
        self.weekly_salary = weekly_salary

    def calculate_salary(self):
        return self.weekly_salary
            
class Manager(SalariedEmployee):
    """""Input name(string), age (int), salary_weekly (number)"""""

    def __init__(self, id, employee_name, weekly_salary, comission):
        SalariedEmployee.__init__(self, id, employee_name, weekly_salary)
        self.comission = comission       
        
    def calculate_salary(self):
        basic = super().calculate_salary()
        return basic + self.comission
        
class Executive(Manager):
    
    def __init__(self, id, employee_name, weekly_salary, comission):
        Manager.__init__(self, id, employee_name, weekly_salary, comission)

    def calculate_salary(self):
            return self.weekly_salary + self.comission