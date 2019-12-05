class PayrollSystem:
    def calculate_salary(self, employee_list):
        print('Calculating Payroll')
        print('===================')
        for employee in employee_list:
            print(f'Payroll for last week:\n- {employee.employee_name}')
            print(f'- Check amount: {employee.calculate_salary()}')
            print(f'- Position: {employee.position}')
            print('')

        m = input("Press Enter to Continue")