class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
        

class manager(employee):
    def __init__(slef,name,salary):
        super().__init__(name,salary)
       
    def display(self):
        print(f"employee name is {self.name} and he is salary is {self.salary}")       
        
        
m = manager("pavna",200000)
m.display()