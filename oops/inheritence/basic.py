class parent:
    def __init__(self,first,second):
        self.fname = first
        self.lname = second
    def display(self):
        print(self.fname, self.lname)

class child(parent):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        
    def display(self):
        print(f"my name is {self.fname}")
        
    

p1 = child("pavan","reddy")
p1.display()