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

def traversal(head):
    temp =head
    while temp:
        print(temp.getdata(),end='->')
        temp = temp.getnext()
    print(None)

def insert_at_pos(head,data,pos):
    new_node = Node(data)
    if pos == 1:
        new_node.setnext(head)
        head = new_node
        return head
    count = 1
    temp = head
    while temp and count<pos-1:
        temp = temp.getnext()
        count += 1
        
    if not temp:
        print('position is beyond the length')
    
    next_node = temp.getnext()
    new_node.setnext(next_node)
    temp.setnext(new_node)
    new_node.setprev(temp)
    if next_node:
        next_node.setprev(new_node)
    return head        
        
    
head1 = insert_at_pos(head,3,2)
traversal(head1)