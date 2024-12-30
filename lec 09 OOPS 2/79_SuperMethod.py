class car:   #parant class 
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car is started ...")

    @staticmethod
    def stop():
        print("car is dtop.")


class ToyotaCar(car):  #child class  # ab car class ke sabhi attribute is class me aa gaye hai
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)   #use to aces method of parant class in child class
        super().start()

    def print(self):
        print("uyuyuyuyu")  # 
        super().start()

car1=ToyotaCar("prius","elevtrical")
car1.print()
print(car1.type)

        
 