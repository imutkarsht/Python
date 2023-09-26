class person:
    name="utkarsh"
    occupation="student"
    networth=0
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
a=person()

#? Creatinng a new Instance of class....

b=person()

# ! Changing the name
# a.name="tiwari"


b.name="Nikita"
b.occupation="teacher"

print(a.name)
print(a.occupation)    

a.info()
b.info()