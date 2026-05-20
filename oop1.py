class student:
    
    def __init__(self, fullname):
        self.name= fullname
        print("Adding new student in database...")
    def hello(self):
        print("Hello", self.name)
        print("You are welcomed here, ", self.name )

s1 = student("Harsh")
print(s1.name)
s1.hello()
s2= student("Het")
print(s2.name)
s2.hello()