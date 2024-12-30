list=[2,1,3,]
print(list)

#--->1
list.append(4)  #ye bhi kuch return nhi karta
print(list)   #mutating of list menas list ko change karna

#--->2
print(list.sort()) #ye kuch return nhi karta isliye none print hua  isne list ko hamesha ke liye sort kar diya
print(list)

list.sort(reverse=True)
print(list,"\n")

listOther=["banana","litchi","apple"]
listOther.sort()   #AT method tabhi work karega jab only list me 1 typr ka varibale ho,only string ya charcter ya dono,
print(listOther) #only int or  flot ya dono
print()

#--->3 reverse
list=[3,1,5,1,6,]
list.reverse()
print(list)

#--->4
list.insert(3,577)
print(list)

#--->5
list.remove(1)
print(list)

#-->
list.pop(0)
print(list.pop(0))
print(list)

#--.extra
my=[]
print(my)
my.append(8)
print(my)
print(my[0])


