class person():
    
    # constructor (dunder Method)
        #? It Will get called Everytime We make A function
        #! Parameterised Constructor --> taking arguments with self
         
    def __init__(self,name,occ):
        print("Hey I'm a Person")
        self.name=name
        self.occ=occ
        
    name="utkarsh"
    occ="student"
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
# a=person()      #! Will call constructor for a first time
# b=person()      #! Will call constructor for a first time

#? Initialization using constructor

a=person("utkarsh","student")
b=person("Pawan","teacher")
 
a.info()
b.info()        