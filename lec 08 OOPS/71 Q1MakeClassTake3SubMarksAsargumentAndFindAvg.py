# class Student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3

#     def print_avarage(self):
#         avg=(self.marks1+self.marks2+self.marks3)/3
#         print(avg)
    
# s1=Student("karan",80,90,100)
# s1.name="kkkkk"   # value update karna
# print(s1.name)
# s1.print_avarage()


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def print_avarage(self):
        sum=0
        for ele in self.marks:
            sum+=ele
        print("hi",self.name,"your score is:",sum/3)
    
s1=Student("karan",[80,90,100])
s1.print_avarage()

# s1.name="kkkkk"   # value update karna
# print(s1.name)