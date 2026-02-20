class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
    def getdata(self):
        return self.data
    def setnext(self,next):
        self.next  = next
    def getnext(self):
        return self.next
    def setprev(self,prev):
        self.prev = prev
    def getprev(self):
        return self.prev
    
head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)

head.setnext(node1)
head.setprev(None)
    
node1.setnext(node2)
node1.setprev(head)

node2.setnext(node3)
node2.setprev(node1)

node3.setnext(node4)
node3.setprev(node2)

node4.setnext(None)
node4.setprev(node3)

def forward_traversal(head):
    temp = head
    if head == None:
        return None
    while temp:
         print(temp.getdata(),end='->')
         temp = temp.getnext()
    print(None)
    
def delete_first(head):
    temp = head
    if temp.getnext() == None:
        return None
    next_node =temp.getnext()
    temp = next_node
    next_node.setprev(None)
    return next_node


head1 = delete_first(head)

forward_traversal(head1)