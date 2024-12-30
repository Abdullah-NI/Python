class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
       # self.percentage=str((self.phy+self.chem+self.math)/3)+"%" # esa karne se ye object creation ke time hi fix ho jagi kuki 
                                                                  # constructer me hai ise change karne ke liye alag se method banao 
                                                                  #  Ya property decorater use karo
    # def calcuPercentage(self):
    #     self.percentage=str((self.phy+self.chem+self.math)/3)+"%"

    @property
    def percentage(self):    # vaise to percentage method ka name but property decorater ise property(means attribute me change kar dega)
        return str((self.phy+self.chem+self.math)/3)+"%"

stud1=student(98,97,99)
print(stud1.percentage)

stud1.phy=80
#stud1.calcuPercentage()
print(stud1.percentage)