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

def insert_node(head,data):
    new_node = Node(data)
    new_node.setnext(None)
    temp = head
    if head == None:
        head = new_node
    while temp:
        if temp.getnext() == None:
            temp.setnext(new_node)
            return True
        temp = temp.getnext()

def traversal(head):
    temp = head
    while temp:
        print(temp.getdata(),end="->")
        temp = temp.getnext()
    print(None)

        
insert_node(head,6)

traversal(head)