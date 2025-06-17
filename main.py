# ------------------ Base Class ------------------ #
class Car:
    # Class variable to track number of Car instances
    total_car = 0

    def __init__(self, make, model, brand):
        # Public attribute
        self.make = make
        # Private attributes using name mangling
        self.__model = model
        self.__brand = brand
        Car.total_car += 1  # Increment car count when a new object is created

    # Return full descriptive info about the car
    def full_info(self):
        return f'{self.__brand} {self.__model} {self.make}'

    # Getter for brand (encapsulation)
    def get_brand(self):
        return self.__brand

    # Setter for brand (allows safe update)
    def set_brand(self, value):
        self.__brand = value
        return f'Brand updated to: {self.__brand}'

    # Regular method to show fuel type
    def fuel_type(self):
        return 'Petrol or Diesel'

    # Static method does not depend on object state
    @staticmethod
    def general_description():
        return 'Car is a Car'

    # Property: Read-only access to private model attribute
    @property
    def get_model(self):
        return self.__model


# ------------------ Subclass (Single Inheritance) ------------------ #
class ElectricCar(Car):
    total_car = 0  # Separate count for ElectricCar

    def __init__(self, brand, make, model, battery_size):
        # Using super() to inherit from parent
        super().__init__(make, brand, model)
        self.battery_size = battery_size
        ElectricCar.total_car += 1

    # Method overriding (polymorphism)
    def full_info(self):
        return f'{super().full_info()} with battery: {self.battery_size}'

    # Overridden method with specific behavior for electric cars
    def fuel_type(self):
        return "Electric Charge"


# ------------------ Additional Classes for Multiple Inheritance ------------------ #
class Battery:
    def battery_info(self):
        return 'This is a battery'


class Engine:
    def engine_info(self):
        return 'This is an engine'


# ------------------ Subclass (Multiple Inheritance) ------------------ #
class ElectricCarTwo(Battery, Engine, Car):
    pass  # No override yet, but inherits all methods


# ------------------ Instance Creation & Testing ------------------ #
my_tesla2 = ElectricCarTwo('2025', 'cybercabnew', 'Tesla')

print(my_tesla2.battery_info())    # Output: This is a battery
print(my_tesla2.engine_info())     # Output: This is an engine
