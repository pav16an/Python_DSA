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
node4.setnext(node2)


def traversal(head):
    temp = head
    while temp:
        print(temp.getdata(),end='->')
        temp = temp.getnext()

    
def remove_cycle(head):
    visited = set()
    prev = None
    temp = head
    
    while temp:
        if temp in visited:  # cycle detected
            prev.setnext(None)  # break the cycle
            break
        visited.add(temp)
        prev = temp
        temp = temp.getnext()
    
    return head
  
head1 = remove_cycle(head)
traversal(head1)
        
