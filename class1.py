class Car():
    # Initializer / Constructor
    def __init__(self, model, make,color,year):
        self.model = model
        self.make = make
        self.color = color
        self.year = year
    def describe_car(self):
        print(f"Model: {self.model}, Make: {self.make}, Color: {self.color}, Year: {self.year}")
    def get_make(self):
        return self.make
    def set_make(self, new_make):
        self.make = new_make
    def get_model(self):
        return self.make
    def set_model(self, new_model):
        self.model = new_model
    def get_year(self):
        return self.year
    def set_year(self, new_year):
        self.year = new_year
    def get_color(self):
        return self.color
    def set_color(self, new_color):
        self.color = new_color


c1 = Car('Civic', 'Honda', 'Black', 2020)
c1.describe_car()
c1.get_year()


class ElectricCar(Car):
    def __init__(self, model, make, color, year, seats, battery_size=80):
        super().__init__(model, make, color, year)
        self.__seats = seats
        self.__battery_size = battery_size

    def get_seats(self):
        return self.seats
    def set_seats(self, new_seats):
        self.seats = new_seats
    def get_battery_size(self):
        return self.battery_size
    def set_battery_size(self, new_battery_size):
        self.battery_size = new_battery_size

    def describe_car(self):
        print(f"Model: {self.model}, Make: {self.make}, Color: {self.color}, Year: {self.year}, Seats: {self.seats}, Battery Size: {self.battery_size}")

    def drive(self):
        print('driving')

c1 = describe_car('Civic', 'Honda', 'Black', 2020)
c1.describe_car()