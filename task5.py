class Employee:
    def __init__(self, name, position, salary):
        
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def display_employee(
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary}")

employee1 = Employee("Rod Jette", "IT Manager", 120,000)
employee1.give_raise(5000)

employee1.display_employee()
