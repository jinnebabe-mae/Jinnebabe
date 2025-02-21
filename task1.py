# Define the Car class
class Car:
    # Constructor to initialize the car's brand, model, and year
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    # Method to display the car's details
    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Create two car objects
car1 = Car("lexus","RX",1989)
car2 = Car("Ford", "Mustang", 2021)

# Display their details
car1.display_info()
print()  # For separating the outputs
car2.display_info()
