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
    
def delete_at_pos(head, pos):
    if head is None:
        return None

    temp = head
    count = 1

    # Case 1: Delete the head node
    if pos == 1:
        new_head = head.getnext()
        if new_head:  # if list has more than one node
            new_head.setprev(None)
        return new_head

    # Traverse to the node at position pos
    while temp and count < pos:
        temp = temp.getnext()
        count += 1

    # If position is invalid (pos > length)
    if temp is None:
        print("Position out of range")
        return head

    prev = temp.getprev()
    next_node = temp.getnext()

    # Update links
    if prev:
        prev.setnext(next_node)
    if next_node:
        next_node.setprev(prev)

    return head

    
head1 = delete_at_pos(head,5)
forward_traversal(head1)