from employee_management.employee import Employee

class Organization:

    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire_employee(self, name, department):
        employee = Employee(name, department)
        self.employees.append(employee)

    def department_employees(self, department):
        count_employess_department = 0
        for employee in self.employees:
            if employee.department == department:
                count_employess_department += 1
        return count_employess_department

    def get_total_employees(self):
        print(f"Company Name: {self.name}")
        print(f'Total employess: {Employee.count_employees}')
        print('*' * 20)
        for employee in self.employees:
            print(f'Associate ID: {employee.id}')
            print(f'Name: {employee.name}')
            print(f'Department: {employee.department}\n')



