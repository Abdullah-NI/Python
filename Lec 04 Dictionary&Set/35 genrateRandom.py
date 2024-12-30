set1={4,7,1,8,3,5,5,1,9,4,2,5}
ans=set1.pop()   #alway gerate 1
print(ans)

n=int(input("enter a random number bw 1 to 10 :"))
count=1
while n!=ans:
    if(n<ans):
        print("you are  lagin:")
        n=int(input("so enter again"))
        count+=1
    elif(n>ans):
        print("you are  leading:")
        n=int(input("so enter again"))
        count+=1

print("Congratulation you find ",ans," in the ",count," attempet")   
