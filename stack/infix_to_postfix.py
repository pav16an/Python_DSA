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
         
    
    
def priority(op):
       if op == '^':
          return 3
       if op in ['*', '/']:
          return 2
       if op in ['+', '-']:
          return 1
       return 0
         

def infix_to_postfix(s):
    stack = Stack()
    ans = ''
    for ch in s:
        if ch == ' ':
            continue
        if ch.isalnum():
            ans += ch
        elif ch == '(':
            stack.push(ch)
        elif ch == ')':
            while not stack.is_empty() and stack.top() != '(':
                ans += stack.pop()
            stack.pop()
        else:
            while (not stack.is_empty() and priority(ch) <= priority(stack.top())):
                ans+=stack.pop()
            stack.push(ch)
    while not  stack.is_empty():
        ans += stack.pop()
    
    return ans
               
        
s = 'a+b*c-d'
result = infix_to_postfix(s)
print(result)
        
