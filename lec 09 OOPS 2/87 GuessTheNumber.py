import random

random=random.randint(1,100)
#print(random)
count=1
while True:
    userchoice=input("guess the target or quit:")
    if(userchoice=="quit"):
        break
    userchoice=int(userchoice)
    if(userchoice==random):
       print("success: correct gauss in",count,"attempt")
       break   
    elif(userchoice<random):
        print("your no is small  gauss again")
        count+=1
    else:
       print("your no is large gauu again")
       count+=1

print("------GAME OVER------")