class Student:
    def useLibrary(self):
        print('\n\n Studnet Fields')
        print('Reading Books')
        print('Making notes')
        print('Solving problems')
s1 = Student()

class Teacher:
    def useLibrary(self):
        
        print('\n\n Teacher Fields')
        print('Reading Books')
        print('Making notes')
        print('Prepare Question Paper')
t1 =Teacher()


class Library:
    def welcome(self, obj):
        obj.useLibrary()

l1 = Library()
l1.welcome(s1)
l1.welcome(t1)