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
         
def balanced_or_not(s):
    stack = Stack()
    
    for ch in s:
        if ch in ['[', '(', '{']:
            stack.push(ch)
        elif ch in [']', ')', '}']:
            if stack.is_empty():
                return False  # More closing brackets than opening
            
            top = stack.top()  # Peek last pushed opening bracket
            
            # Check if current closing matches last opening
            if (ch == ')' and top == '(') or \
               (ch == ']' and top == '[') or \
               (ch == '}' and top == '{'):
                stack.pop()
            else:
                return False  # Mismatched brackets
        

    # If stack is empty after processing, it's balanced
    return stack.is_empty()

s = '({[]})'

print(balanced_or_not(s))  
