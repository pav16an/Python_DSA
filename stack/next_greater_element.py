class Stack:
    def __init__(self):
       self.stack = []
       self.peek = -1
    def push(self,data):
        self.stack.append(data)
        self.peek+=1
    
    def top(self):
       if self.is_empty:
           print('stack is empty')
       return self.stack[self.peek]

    def is_empty(self):
        if self.peek == -1:
            return True
        else:
            return False
        
    def pop(self):
        if self.is_empty():
            print("stack is under flow")
            return None
        poped_element = self.stack.pop()
        self.peek -=1
        return poped_element
        
    def display(self):
        if self.is_empty():
            print('stack is empty')
        else:
            for  i in range(self.peek,-1,-1):
                print(self.stack[i])
         
def next_greater_element(l):
    n = len(l)
    l1 = []
    for i in range(n):
        for j in range(i+1,n):
            if l[j] > l[i]:
                l1.append(l[j])
        else:
                l1.append(-1)
    return l1

l = [2,9,4,7,3,6,9,5]
res = next_greater_element(l)
print(res)