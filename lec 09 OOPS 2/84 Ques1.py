class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
       return (22/7)*self.radius*self.radius

    def parameter(self):
        return 2*(22/7)*self.radius

c1=circle(7)
print(c1.area())
print(c1.parameter())