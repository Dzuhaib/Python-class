class Cars:
    wheels = 4
    def __init__(self):
       self.mileage = 10 
       self.company = 'BMW'

    def drive(self):

        print('driving')

# # c1 = Cars(4,30,'Honda')
# c2 = Cars(6,40,'BMW')
# print(c1.wheels)
# print(c1.mileage)
# print(c1.company)
# c1.drive()

# print(c2.wheels)
# print(c2.mileage)
# print(c2.company)
# c2.drive()

# c1.avg()

# c1.wheels = 20
# print(c1.wheels)


class School:
    def __init__(self, name, student, teacher):
        self.name = name
        self.student = student
        self.teacher = teacher

    def __str__(self):
        return f"Name: {self.name}\nStudent: {self.student}\nTeacher: {self.teacher}"

    def __repr__(self):
        return f"Name: {self.name}\nStudent: {self.student}\nTeacher: {self.teacher}"

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name


school = School('Zuhaib', 'Yes', 'No')
print(school)
