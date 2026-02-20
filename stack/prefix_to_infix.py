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
         
def prefix_to_infix(s):
    stack = Stack()
    for ch in s[::-1]:
        if ch.isalnum():
            stack.push(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            t = (f"({op1}{ch}{op2})")
            
            stack.push(t)
    return stack.pop()

s = '*+pq-ab'
res = prefix_to_infix(s)
print(res)
        