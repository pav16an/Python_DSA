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
node1 = Node(3)
node2 = Node(5)
node3 = Node(7)
node4 = Node(10)


head.setnext(node1)
node1.setnext(node2)
node2.setnext(node3)
node3.setnext(node4)
node4.setnext(None)
    

l2 = Node(2)
nodel1 = Node(4)
nodel2 = Node(6 )
nodel3 = Node(9)

l2.setnext(nodel1)
nodel1.setnext(nodel2)
nodel2.setnext(nodel3)
nodel3.setnext(None)

def traversal(head):
    temp = head
    while temp:
        print(temp.getdata(),end='->')
        temp = temp.getnext()
    print(None)

def merge_ll(l1,l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    temp = l1
    while temp.getnext():
        temp = temp.getnext()
    temp.setnext(l2)
    return l1
        
        
def merge_sorted_ll(l1,l2):
    
    dummy = Node(0)
    temp = dummy
    while l1 and l2:
        if l1.getdata() <= l2.getdata():
            temp.setnext(l1)
            l1 = l1.getnext()
        else:
            l1.getdata() >= l2.getdata()
            temp.setnext(l2)
            l2 = l2.getnext()
        temp = temp.getnext()
    
    if l1 :
        temp.setnext(l1)
    if l2 :
        temp.setnext(l2)
    
    
    return dummy.getnext()

head1 = merge_sorted_ll(head,l2)
traversal(head1)



    
