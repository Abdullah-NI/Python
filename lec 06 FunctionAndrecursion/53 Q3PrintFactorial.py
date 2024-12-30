def fac(n):
    fac=1
    for i in range(1,n+1):  #ek trah se ye for(i=1;i<n+1 ,i++)   chuki by default ek ek incriment ho raha hai
        fac=fac*i
    return fac

print("factorial is ;",fac(5))