import random
import string

# print(string.ascii_letters)  //all are string formate
# print(string.digits)
# print(string.punctuation)

charvalues=string.ascii_letters+string.digits+string.punctuation
#print(random.choice(charvalues))

# val=random.choice([1,2,3,4,"hj","t",9])  //ya list bhi pass kar sakte hai
# print(val)

n=int(input("enter length of passward :"))
password=""
for i in range(1,n+1):
    password+=random.choice(charvalues)

#using list comprehension method [function for i in range()]
#password="".join([random.choice(charvalues) for i in range(1,n+1)])  # "*".join() jo bhi value list me aati rahegi wo is star se 
                                                                      # join hokar judti rahefgi
print("you pass is :",password)