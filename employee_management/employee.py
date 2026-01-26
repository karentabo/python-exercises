class Employee:
    count_employees = 0

    def __init__(self, name, department):
        Employee.count_employees += 1
        self.name = name
        self.department = department
        self.id = Employee.count_employees

    @classmethod
    def get_count_employees(cls):
        return cls.count_employees

#encapasulement removed

    # @property
    # def name(self):
    #     return self._name
    #
    # @property
    # def department(self):
    #     return self._department
    #
    # @name.setter
    # def name(self, name):
    #     self._name = name
    #
    # @department.setter
    # def department(self, department):
    #     self._department = department