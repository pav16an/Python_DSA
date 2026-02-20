class student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        
    def display_info(self):
        print(f"stduent name is {self.name} he is roll_no is {self.roll_no} and he got {self.marks} marks")
        
        

name = 'pavan'
num = 21
marks = 95

s1 = student(name,num,marks)
s1.display_info()
