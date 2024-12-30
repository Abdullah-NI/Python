class Student:
    college_name="ABCD"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def welcome(self):  # every method me self likha jaroro hai 
        print("welcome student ",self.name)

    def get_marks(self):
        return self.marks
    
    @staticmethod
    def helo():   # satic method yaha self likhne ki jarorat nhi hai ye clas leve er kaam karta hai  au chahe class name se bhi acces kar lo
        print("hello")

s1=Student("karan",78)
s1.welcome()
print(s1.get_marks())
s1.helo()
Student.helo()

