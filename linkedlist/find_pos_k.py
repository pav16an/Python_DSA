class Node :
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
    def setdata(self,data):
        self.data = data

    def getdata(self):
        return self.data
    
    def setnext(self,next):
        self.next = next

    def getnext(self):
        return self.next
    

head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)


head.setnext(node1)
node1.setnext(node2)
node2.setnext(node3)
node3.setnext(node4)
node4.setnext(None)

def traversal(head,):
    temp = head
    while temp:
        print(temp.getdata(),end='->')
        temp = temp.getnext()
    
def pos_k(head,k):
    first = head
    second = head
    for _ in range(k):
        if  not  first:
            return None
        first = first.getnext()
        
    while first:
        first = first.getnext()
        second = second.getnext()
    return second.getdata()
        
print(pos_k(head,3))
    
        