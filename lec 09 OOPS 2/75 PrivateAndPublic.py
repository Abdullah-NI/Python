class Account:
    bank_name="ABCDE"
    __bank_code="45678"   #private
    def __init__(self,acc_no,acc_pas):
        self.acc_no=acc_no        # by default public hai means class ke bhar 
        self.__acc_pas=acc_pas    ## ab acc_pas private ban gaya ye only isi class me accec ho sakta hai

    def reset_pass(self):
        print(self.__acc_pas)

    def __codeDetail(self):    #private   ham private isliye banate hai taki koi ur function in fuction ko use kar sake aur user na kare
        print("Cde is here and value",self.__bank_code)

    def codeAcess(self):
        self.__codeDetail()



acc1=Account("12345","abcde")
print(acc1.acc_no)
#print(acc1.acc_pas)
acc1.reset_pass()

acc1.codeAcess()
