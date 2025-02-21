class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Create two car objects
car1 = Car("Toyota", "Vios", 2025)
car2 = Car("Honda", "CR-V", 2018)

# Display their details
car1.display_info()
car2.display_info(
