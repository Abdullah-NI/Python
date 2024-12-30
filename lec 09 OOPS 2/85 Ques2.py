class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showDetail(self):
        print("role=",self.role)
        print("department=",self.department)
        print("salary=",self.salary)

# class engineer(employee):
#     def __init__(self,name,age,role,department,salary):
#         self.name=name
#         self.age=age
#         super().__init__(role,department,salary)

#     def showDetail(self):
#         print("name=",self.name)
#         print("age=",self.age)
#         super().showDetail()

class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","it","75,000")
       
e1=employee("account","Finance","50,000")
e1.showDetail()

print()

# eng1=engineer("abcd",30,"maneger","ec","565656")
# eng1.showDetail()

eng1=engineer("abcd",30)
eng1.showDetail()
