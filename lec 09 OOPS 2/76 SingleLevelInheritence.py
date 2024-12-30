class car:   #parant class 
    color="black"
    @staticmethod
    def start():
        print("car is started ...")

    @staticmethod
    def stop():
        print("car is dtop.")

    # def car_no(self):
    #     print("car no is ",self.carno)  # yaha carno toyatacar ka attricute hai isliye uske object ke liye chal raha hai is class
    #                                     #is class ke object ke liye nhi chalega
    def carQualit(self):
        print("quility good")


class ToyotaCar(car):  #child class  # ab car class ke sabhi attribute is class me aa gaye hai
    def __init__(self,name,carno):
        self.name=name
        self.carno=carno
            
car1=ToyotaCar("fortuner","183")
print(car1.name)
print(car1.color)
car1.start()
car1.carQualit()

