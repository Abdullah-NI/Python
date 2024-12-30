class person:
    name="Anonymous"

    # def changeName(self,name):
    #    # self.name=name  # self likha hai isliye object ka name change karaga

    #     #person.name=name # person likha ha means class ka name attribute change hoga isliye ab puri class ka name me ye name aa jayga
    #     #ya ese
    #     self.__class__.name=name  #means self ki class ke name attribute (means person class ka name attribute ) me ab ye name aayga 
    #     # ya yahi kaam class method se kar sakte hai

    @classmethod
    def changeName(cls,name):   #class method me yaha self ki jagha cls likha means ye class ke attribute ko change karega
        cls.name=name

p1=person()
print(p1.name)
person.changeName("rahul kumar")
print(p1.name)
print(person.name)
