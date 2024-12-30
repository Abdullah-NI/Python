tup=(1,4,9,16,25,36,49,64,81,100)
#n=len(tup)

x=int(input("enter no which you want to find"))

# i=0
# while i< len(tup):
#     if(tup[i]==x):
#         print("finnd at indx",i)
#     else:
#         print("finding..")
#     i+=1

i=0
while i< len(tup):
    if(tup[i]==x):
        print("finnd at indx",i)
        break
    else:
       print("Finding...")
    i+=1

print()
i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

