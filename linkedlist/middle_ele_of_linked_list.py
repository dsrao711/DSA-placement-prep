class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
 
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
 
 
def FindMiddle(list):
    current = list.head
    length = 0
    while current:
        current = current.next
        length = length + 1
 
    current = list.head
    for i in range((length - 1)//2):
        current = current.next
 
    if current:
        if length % 2 == 0:
            print(current.next.data)
        else:
            print(current.data)
    else:
        print('No data found')
 
 
MyList = LinkedList()
 
MyList.append(10)
MyList.append(20)
MyList.append(30)
MyList.append(40)
MyList.append(50)
MyList.append(60)
 
FindMiddle(MyList)