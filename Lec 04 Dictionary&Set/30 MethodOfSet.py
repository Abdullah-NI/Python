collection=set()
print(collection)
print(type(collection))
#print(set)

#--->1
collection.add(45)   # set is mutable but set element is immutable isliye ham list and dic set me add nhi kar sakte hai
collection.add(67)
collection.add(67)
collection.add("myyyy")
collection.add((1,2,3,4,5,6,7,))
#collection.add([1,2,3,4,5])   not add 
print(collection,"\n")

#--->
collection.remove(45)
#collection.remove(888)  error bcz not persent
print(collection,'\n')

#---->
print(len(collection))
collection.clear()
print(len(collection))

print()
#--->
coll2={"hello","my","java","c"}
print(coll2.pop())  # random value pop karega iska use tab hai jab ham random value genarte karna cha rahe hai
print(coll2.pop())
print(coll2)   #rest value yaha bachi

print()

#---> unoin and intersection
set1={1,2,3}
set2={2,3,4,5}
print(set1.union(set2))#{1,2,3,4,5}
print(set1.intersection(set2))  #{2,3}