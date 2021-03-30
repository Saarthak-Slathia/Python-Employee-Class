class Employee:
    count = 0

    def properties(self, n, a, s, c):
        self._name = n
        self._age = a
        self._salary = s
        self._company = c

e1 = Employee()
e1.properties("Saarthak", 11, 21000, 'ISRO')
Employee.count = 1
print(Employee.count)