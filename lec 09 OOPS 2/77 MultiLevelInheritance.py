class car:   #parant class 
    color="black"
    @staticmethod
    def start():
        print("car is started ...")

    @staticmethod
    def stop():
        print("car is dtop.")


class ToyotaCar(car):  #child class  # ab car class ke sabhi attribute is class me aa gaye hai
    def __init__(self,brand):
        self.name=brand
       
class Fourtuner(ToyotaCar):
    def __init__(self,type):
        self.type=type

car1=Fourtuner("diseal")
car1.start()
