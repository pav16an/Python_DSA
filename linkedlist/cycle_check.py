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
        temp =  temp.getnext()
    print("None")
    
#traversal(head)
        

# def find_cycle(head):
#     seen = set()
#     temp = head
#     while temp:
#         if temp in seen:
#             print(f"cycle find at {temp.getdata()} ")
#             return True
#         seen.add(temp)
#         temp = temp.getnext()

def find_cycle(head):
    slow = head
    fast = head
    while fast and fast.getnext():
        slow = slow.getnext()
        fast = fast.getnext().getnext()
        if slow == fast:
            print(f"cycle is find at {slow.getdata()}")
            return True
    
find_cycle(head)

    
        