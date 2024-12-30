list1=[1,2,3,4,5,6]
for ele in list1:     #jab iterater per kaam karana hai value update karna stpoing cond hai to while loop
    print(ele)      # jab data type per traverse karna hai to for loop list,tuple etc

list2=["apple","mango","banana"]
for ele in list2:
    print(ele)

name="abdullah"
for char in name:
    print(char)

print()
name="affan"
for char in name:
    print(char)
else:             # loop pura hone ke bbad ye else wala statment run hoga
    print("end")   # yadi loop puri na hui means last tak nhi vhali hmne break use kara hoga to else wala tab run nhi hoga
                   # yadi han ye END witout else likhte to ye loop per depend nhi karta har case me chalta
print()

str="abcde"
for ch in str:
    if(ch=='c'):
        print(ch," found")  # if c mila to end print nhi hoga if c nhi mila to end print hoga
        break
else:
    print("END")    
