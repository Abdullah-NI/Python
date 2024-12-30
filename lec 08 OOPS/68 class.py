# class Student:
#     name="karan"


# s1=Student()
# print(s1)
# print(s1.name)

# s2=Student()
# print(s2.name)


# class Car:
#     color="blue"
#     brand="mercedes"

# car1=Car()
# print(car1.color)
# print(car1.brand)



# class Student:
#    name="karan"
#    #constructer     jab constructer nhi banate hai to tab bhi ye apne aap call hota hai jab ham object banate hai
#    def __init__(self):   # self yaha current object ko point kar raha hai
#       print("Creating object")
   
# s1=Student()



class Student:    # start with capital later but not neccessary
   #String name;  ya in python name="KUCH Bhi"

   #default constructer
   def __init__(self):  # jon sa hamare arugument ke hisab se match wo call hoga ,chahe ise mat banao ye apne aap hi ban jata hai
      pass              # ya apne hisab se bana do
   
   #parameterized constructer
   def __init__(self,name,marks):  #chahe yaha fullname  likho
      self.name=name    # yaha name naam ka ek new varibale create hua class me
      self.marks=marks
      print("addding new student in database")                      # self ki jagha khuch aur bhi use kar sakte hai
s1=Student("karan",97)
#print(s1)
print(s1.name,s1.marks)

s2=Student("rahul",78)
print(s2.name,s2.marks)
