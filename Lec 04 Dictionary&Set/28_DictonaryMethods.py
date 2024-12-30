student={
    "name":"rahul",
    "subject":{
        "phy":96,
        "chem":89,
        "maths":78,
    }   ,
    "age":18,
    2:"His roo no"
}

# 1------>
print(student.keys())
print(len(student))   #no of keys 
#ya
print(list(student.keys()))  #type castinf in the key list
print(len(list(student.keys())),"\n")

# 2--->
print(student.values())
print(list(student.values()),"\n")

# 3--->
print(student.items())
print(list(student.items()),"\n")
pairs=list(student.items())
print(pairs[0],"\n")

# 4--->
print(student["name"])  # if dic me name present nhi hoga to ye error dega isliye niche ka code nhi chalega upeer ka to chal jayega
print(student.get("naxme"),"\n")   #ye error nhi dega None print kara dega

#5 --->
student.update({"city": "delhi"})
print(student)

#ya
new_dic={"rating":"good","isSincere":True,"name":"neha"}  #Here name is Overwite by neha istead of adding new key value pair bcz duplicate key is not allow
student.update(new_dic)
print(student)


#note write dicnary Name . vs code tell you all method
