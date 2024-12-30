class Car:
    def __init__(self):
        self.acc=False # acc=accelater
        self.br=False  # braek
        self.clutch=False
                            
    def start(self):
        self.clutch=True   # yha hamne unneccesary chize ide kar di
        self.acc=True
        print("car starts...")


car1=Car()
car1.start()
    

