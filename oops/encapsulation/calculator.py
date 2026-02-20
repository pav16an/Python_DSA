class calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def add(self):
        print(self.x + self.y)
    def sub(self):
        print(self.x - self.y)
    def div(self):
        print(self.x/self.y)
    def mul(self):
        print(self.x * self.y)
        
        
x = 5
y = 20
cal = calculator(x,y)
cal.add()
cal.sub()
cal.mul()
cal.div()