def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)


#---. fac

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)   # jaha recrence relation hota hai waha recursion use karte hai
    
print(fact(5))