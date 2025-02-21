class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"Salary increased by {amount}. \nNew salary: {self.salary}")

    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")

employee1 = Employee("Ruffa Mae Olimpay", "Web Developer", 900000)
employee1.give_raise(2000)
employee1.display_employee()
