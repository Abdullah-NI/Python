# count=0
# with open("lec 07 FileInputAndOutPut\Ipractice.txt") as f:
#     data=f.read()
#     print(data)
#     num=""
#     for i in range(len(data)):
#         if(data[i]==","):
#             n=int(num)
#             print(n)
#             if(n%2==0): count+=1
#             num=""
#         else:
#             num+=data[i]
#     n=int(num)
#     print(n)   # for last value chuki last me comma nhi hai
#     if(n%2==0): count+=1

#     print("no of even no is ",count)


count=0
with open("lec 07 FileInputAndOutPut\Ipractice.txt") as f:
    data=f.read()
    print(data)

    nums=data.split(",")
    print(nums)       #list bani hai string ki
    for val in nums:
        if(int(val)%2==0):
            count+=1

print("no of even no is ",count)
    