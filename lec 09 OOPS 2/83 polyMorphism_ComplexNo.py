class complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def shownNumber(self):
        print(self.real,"i +",self.imag,"j")

    # def add(self,num2): #self1,self2
    #     newreal=self.real+num2.real
    #     newimag=self.imag+num2.imag
    #     return complex(newreal,newimag)

    def __add__(self,num2): #dunder function ye add ka hai jab ham num1 + num2 karege to ye function ke ander ka kaam karega chahe
        newreal=self.real+num2.real # ham ander -,* / hi ku na kara fir ye + likhne se waho kam karega jo ham kahege
        newimag=self.imag+num2.imag  # means ham + ka logic apni clASS ME DEFINE KAR rahe hai
        return complex(newreal,newimag)
    
    def __sub__(self,num2): # yha dunder fun sub use kara magar kaam hame multiply karaya to ab num1-num2 karne se multiply hoha
        newreal=self.real*num2.real 
        newimag=self.imag*num2.imag
        return complex(newreal,newimag)


num1=complex(1,3)
num1.shownNumber()

num2=complex(4,6)
num2.shownNumber()

# num3=num1.add(num2)
# num3.shownNumber()

num3=num1+num2
num3.shownNumber()

num4=num1-num2
num4.shownNumber()