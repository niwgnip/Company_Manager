# Company Manager - Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. 
# Every one's pay is calculated differently, research a bit about it. 
# After you've established an employee hierarchy, create a Company class that allows you to manage the employees. 
# You should be able to hire, fire and raise employees.
import employee
import hr

employees = []


emp1 = employee.HourlyEmployee(1, 'Simon', 25, 33)
emp2 = employee.SalariedEmployee(2, 'Kate', 1100)
emp3 = employee.Manager(3, 'John', 2000, 450)
emp4 = employee.Executive(4, 'Mike', 3000, 700)

employees = [emp1, emp2, emp3, emp4]

payment = hr.PayrollSystem()
payment.calculate_salary(employees)

