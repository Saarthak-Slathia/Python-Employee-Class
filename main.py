class Employee:
    def set_data(self, n, a, s):
        self._name = n
        self._age = a
        self._salary = s

    def department_data(self, d_name, d_id):
        self._department_name = d_name
        self._department_id = d_id

    def display_data(self):
        print(self._name)
        print(self._age)
        print(self._salary)
        print()
        print(self._department_name)
        print(self._department_id)

employee = Employee()
employee.set_data("Siddharth", 42, 1120000)
employee.department_data("Computer Engineering", 7421)
employee.display_data()