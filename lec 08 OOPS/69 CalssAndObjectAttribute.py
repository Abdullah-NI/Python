class Student:
    college_name="abcd"  # class atribute sabhi object ke liye sam and store once time in memory
    #name="Anonymus"     #precedence object atrribute ki hogi  chahe ye niche bhi likho
    def __init__(self,name):
        self.name="karan"  #object attribute or instance atribute  ,ye self ke sath likha jata hai,ye har object ke liye alag se stre hoga

s1=Student("karan")
print(s1.name)
print(s1.college_name)
#or
print(Student.college_name)
