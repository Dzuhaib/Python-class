class Student():
    # Initializer / Constructor
    def __init__(self,name,age,city,course):
        self.name = name
        self.age = age
        self.city = city
        self.course = course

    # Functions / Methods
    def apper_in_exam(sefl):
        print(f"{sefl.name} is appearing in exam")

    # Functions / Methods
    def pay_fees(sefl):
        print(f"{sefl.name} is paying fee")

s4 = Student('Zuhaib', 20, 'Karachi', 'Python')
s4.apper_in_exam()
s4.pay_fees()

s5 = Student('Hamza', 22, 'Karachi', 'IT')
s5.apper_in_exam()
s5.pay_fees()



class Car():
    # Initializer / Constructor
    def __init__(self, model, make,color):
        self.model = model
        self.make = make
        self.color = color

    # Functions / Methods
    def describe_car(self):
        print(f"""
                Model Name: {self.model}
                Car Make: {self.make}
                Car Color: {self.color}
                """)
        
c1 = Car('2020', 'Honda', 'Black')
c1.describe_car()

c2 = Car('2024', 'Corolla', 'White')
c2.describe_car()
