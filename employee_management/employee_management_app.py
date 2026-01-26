from employee_management.organization import Organization
from employee_management.employee import Employee

print('*** Employee system ***')

organization1 = Organization('My Organization')

organization1.hire_employee('John Smith', 'IT')
organization1.hire_employee('Carl Green', 'IT')
organization1.hire_employee('Anne Tobias', 'HR')

print(f'Total employees: {Employee.count_employees}')
print(f'Total in IT: {organization1.department_employees('IT')}')
print(f'Total in HR: {organization1.department_employees('HR')}')
print('\n')
organization1.get_total_employees()
