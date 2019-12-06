# Company Manager - Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. 
# Every one's pay is calculated differently, research a bit about it. 
# After you've established an employee hierarchy, create a Company class that allows you to manage the employees. 
# You should be able to hire, fire and raise employees.
import employee
import hr
import comp

from os import system, name
from time import sleep

## Setting starting lists/dicts needed for later use
positions = ('Executive', 'Manager', 'Salaried Employee', 'Hourly Employee')
payment = hr.PayrollSystem()
process = False
emp_dict = {}
emp_list = []

#Adding employees to the list and dictionary used in other methods/functions
def add_to_list_dict(new_emp):
	emp_list.append(new_emp)
	emp_dict.update({new_emp.employee_name:new_emp.position})

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
# functions for choosing what to do from main menu
def what_to_do():
	print (f'What would you like to do?\n')
	print (f'0. Hire new employee.\n')
	print (f'1. Fire current employee.\n')
	print (f'2. Raise employee.\n')
	print (f'3. Check payroll for all employees.\n')
	print (f'4. I want to exit the program.')
	print ('Choose 0-4.')
	while True:
		try:
			decision = int(input())
			if decision < 0 or decision > 4:
				print("Use only the provided selections")
			else:
				break
		except:
			print('Invalid input.')
	return decision
# decide an action based on input
def action(x, passw, company,emp_list):
	if x == 0 and passw == True:
		data = my_company.hire_new()
		add_to_list_dict(data)
		sleep(2)
		input("\nPress Enter to continue...")
	elif x ==1 and passw == True:
		iteration = my_company.fire_employee(emp_list)
		if iteration >= 0:
			del emp_list[iteration]
		sleep(2)
		input("\nPress Enter to continue...")
	elif x == 2 and passw == True:
		my_company.rise_employee(emp_list,emp_dict)
		sleep(2)
		input("\nPress Enter to continue...")
	elif x == 3:
		payment.calculate_salary(emp_list)
		input("\nPress Enter to continue...")
	elif x == 4:
		print("Exit protocol iniciated")
		sleep(1)
		input("\nPress Enter to continue...")
	else:
		pass
# check if password for access is correct
def security():
	p = input(f'\nEnter Password to Access:')
	return p == "1"

def choose_emp(list_of_emps):
	for x in range(len(list_of_emps)):
		print (list_of_emps[x].employee_name)

	emp0 = input("\nPlease input name of employee: ")
	return emp0

# Name of the company
clear()
my_company = comp.Company('Pingux')
sleep(2)

# Setting starting employees for the Company
emp1 = employee.HourlyEmployee('Simon', 25, 33)
emp_dict.update({emp1.employee_name:emp1.position})
emp_list.append(emp1)

emp2 = employee.SalariedEmployee('Kate', 1100)
emp_dict.update({emp2.employee_name:emp2.position})
emp_list.append(emp2)

emp3 = employee.Manager('John', 2000, 450)
emp_dict.update({emp3.employee_name:emp3.position})
emp_list.append(emp3)

emp4 = employee.Executive('Mike', 3000, 700)
emp_dict.update({emp4.employee_name:emp4.position})
emp_list.append(emp4)

emp5 = employee.HourlyEmployee('Bernard', 25, 33)
emp_dict.update({emp5.employee_name:emp5.position})
emp_list.append(emp5)

# Start of code
while True:
# Decision from main menu
	# 	print ("\033[H\033[J")
	x = what_to_do()
	if x == 0 or x == 1 or x == 2:
		permission = security()
		if permission == True:
			action(x,permission, my_company,emp_list)
		else:
			print ("Wrong password, access not granted")
			sleep(1)
	elif x == 3:
		permission = False
		action(x,permission, my_company,emp_list)
	elif x == 4:
		permission = False
		action(x,permission, my_company,emp_list)
		print ("End of application")
		break