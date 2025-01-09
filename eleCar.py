class Battery:
    def __init__(self,):
        self.battery_size = 80

class ElecCar:
    def __init__(self, make, moder, year, engine):
        
        self.make = make
        self.moder = moder
        self.year = year
        self.engine = engine


class A:
    def Feature1():
        print("This is feature1")

    def Feature2():
        print("This is feature2")

c1 = A()
c1.Feature1()
c1.Feature2()

class B(A):
    def Feature3():
        print("This is feature3")

c2 = B()
c2.Feature1()
c2.Feature2()
c2.Feature3()

class C(B):
    def Feature4():
        print("This is feature4")

c3 = C()
c3.Feature1()
c3.Feature2()
c3.Feature3()
c3.Feature4()

class C(A,B):
    def Feature5():
        print("This is feature5")

c4 = C()
c4.Feature1()
c4.Feature2()
c4.Feature3()
c4.Feature4()
c4.Feature5()
