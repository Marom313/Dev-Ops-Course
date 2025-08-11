# Inheritance and Polymorphism


class Vehicle:
    def __init__(self, color='', fuel_type=''):
        self.color = color
        self.fuel_type = fuel_type

    def drive(self):
        print("The vehicle is in motion")


class Car(Vehicle):
    def __init__(self, color, fuel_type, brand=''):
        super().__init__(color, fuel_type)
        self.brand = brand

    def print_info(self):
        print("Instance of a car:")
        if self.color != '':
            print("- Color: " + self.color)
        if self.fuel_type != '':
            print("- Fuel type: " + self.fuel_type)
        if self.brand != '':
            print("- Brand: " + self.brand)

        print("\n\n")


def run7():
    A = Car(color="red", fuel_type="gasoline", brand="Toyota")
    B = Car("blue", "truck")
    A.print_info()
    A.drive()
    B.print_info()
    B.drive()
