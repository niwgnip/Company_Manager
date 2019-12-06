import employee

class Company:

	def __init__(self,name):
		self.name = name
		print (f'\n\n#######################')
		print (f'The Company {self.name} was created.')
		print (f'#######################\n\n\n')
# check if input is int and > 0
	def numberinput(self, message):
		while True:
			try:
				userinput = int(input(message))
				if userinput <= 0:
					print ("Please use value bigger than 0\n")
					continue
				else:
					return int(userinput)
			except ValueError:
				print("The value has to be integer! Please try again\n")
			else:
				return int(userinput)

#  hiring new employee
	def hire_new(self):
		print("\nWhat is his/her name?")
		while True:
			new_name = input()
			if new_name.isalpha():
				break
			else:
				print("Please use only letters and no spaces, try again")

		print ('\nWhat is his/her position? (1-4)\n1. Hourly Employee\n2. Salaried Employee\n3. Manager\n4. Executive\n')
		while True:
			try:
				new_pos = int(input())
				if new_pos < 1 or new_pos > 4:
					print("Use only the provided selections")
				else:
					break
			except:
				print('Invalid input.')
		if new_pos == 1:
			# new_hour_rate = int(input("What will be his/her hour rate?"))
			new_hour_rate = self.numberinput('What will be his/her hour rate')
			new_working_time = self.numberinput("How many hours will he work per week?")
			new_emp = employee.HourlyEmployee(new_name, new_hour_rate, new_working_time)
			print(f"You hired new employee - {new_name} on a position -> {new_emp.position}")
			
		elif new_pos == 2:
			new_salary = self.numberinput("What will be his/her salary?")
			new_emp = employee.SalariedEmployee(new_name, new_salary)
			print(f"You hired new employee - {new_name} on a position -> {new_emp.position}")
		elif new_pos == 3:
			new_salary = self.numberinput("What will be his/her salary?")
			new_commission = self.numberinput("What will be his/her commission?")
			new_emp = employee.Manager(new_name, new_salary, new_commission)
			print(f"You hired new employee - {new_name} on a position -> {new_emp.position}")
		elif new_pos == 4:
			new_salary = self.numberinput("What will be his/her salary?")
			new_commission = self.numberinput("What will be his/her commission?")
			new_emp = employee.Executive(new_name, new_salary, new_commission)
			print(f"You hired new employee - {new_name} on a position -> {new_emp.position}")
		else:
			pass

		return new_emp
# method to fire employee (need to input proper name)
	def fire_employee(self, list_of_emps):
		number = -1
		for x in range(len(list_of_emps)):
			print (list_of_emps[x].employee_name)

		print("\nPlease input name of employee you want to fire: ")
		while True:
			name = input()
			if name.isalpha():
				break
			else:
				print("Please use only letters and no spaces, try again.")
				
		for i in range(len(list_of_emps)):
			if list_of_emps[i].employee_name == name:
				print (f"\n\n{list_of_emps[i].employee_name} is FIRED!")
				process = True
				number = i
				break	
			else:
				process = False

		if process == False:
			print (f"\n\nThere is no employee {name} in  this company")

		return number

	def rise_employee(self, emp_list,emp_dict):
		print("\nOkey. Who should get promotion?")
		for x in range(len(emp_list)):
			print (emp_list[x].employee_name)
		check = 0
		print("\nPlease input name of employee: ")
		while True:
			name = input()
			if name.isalpha():
				break
			else:
				print("Please use only letters and no spaces, try again.")

		for i in range(len(emp_list)):
			if emp_list[i].employee_name == name and emp_list[i].position == 'Hourly Employee':
				new_salary = self.numberinput("Provide new salary after promotion to Salaried Employee (per week)")
				new_name = name
				new_emp = employee.SalariedEmployee(name, new_salary)
				emp_list.insert(i+1,new_emp)
				emp_dict.update({new_emp.employee_name:new_emp.position})
				del emp_list[i]
				del emp_dict[name]
				print(f"{new_emp.employee_name} has been promoted to Salaried Employee!")
				break
			elif emp_list[i].employee_name == name and emp_list[i].position == 'Salaried Employee':
				new_salary = self.numberinput("Provide new salary after promotion to Manager (per week)")
				new_commission = self.numberinput ("Provide commission for Manager: ")
				new_name = name
				new_emp = employee.Manager(new_name,new_salary,new_commission)
				emp_list.insert(i+1,new_emp)
				emp_dict.update({new_emp.employee_name:new_emp.position})
				del emp_list[i]
				del emp_dict[name]
				print(f"{new_emp.employee_name} has been promoted to Manager!")
				break
			elif emp_list[i].employee_name == name and emp_list[i].position == 'Manager':
				new_salary = self.numberinput("Provide new salary after promotion to Executive (per week)")
				new_commission = self.numberinput ("Provide commission for Executive: ")
				new_name = name
				new_emp = employee.Executive(new_name,new_salary,new_commission)
				emp_list.insert(i+1,new_emp)
				emp_dict.update({new_emp.employee_name:new_emp.position})
				del emp_list[i]
				del emp_dict[name]
				print(f"{new_emp.employee_name} has been promoted to Executive!")
				break
			elif emp_list[i].employee_name == name and emp_list[i].position == 'Executive':
				print(f"You can not raise {emp_list[i].employee_name} any higher!")
				break
			else:
				check += 1
				continue

		if check == len(emp_list):
			print(f'There is no employee {name} in this company.')
			input("\nPress Enter to continue...")


