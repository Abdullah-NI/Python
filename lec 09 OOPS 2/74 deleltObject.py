class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
s1=student("Abdullah",45)
print(s1.name)
print(s1.roll)

del s1.name  # delet object attribute
print(s1.roll)
print(s1.name)

del s1  #delet object
print(s1.name)
print(s1.roll)