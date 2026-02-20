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
                
def find_min(s):
    stack = Stack()
    min_stack = Stack()
    for num in s:
        stack.push(num)
        if min_stack.is_empty():
            min_stack.push(num)
            curr_min = min_stack.top()
        else:
            if min_stack.top() > num:
                min_stack.push(num)
            else:
                min_stack.push(curr_min)
    return stack.top(),min_stack.top()
                

s = [2,5,3,6,1,7,9]
res = find_min(s)
print(res)