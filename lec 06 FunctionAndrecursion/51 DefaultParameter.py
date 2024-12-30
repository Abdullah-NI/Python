# def cal_prod(a,b):   #give error bcz a nd b has no value to 
#     print(a*b)
#     return a*b

# cal_prod()

def cal_prod(a=1,b=1):   #ham inhe default value de dete hai ja ham argument pass nhi katre hai tab ye chal jate hai
    print(a*b)
    return a*b

cal_prod()   

def cal_prod(a,b=1):   
    print(a*b)
    return a*b

cal_prod(4)   # ye a ke ander jaga  jab ek  argument ho to default parameter last se banate hua aate hai bcz ye value stating se
              # fill hona suru hoti hai