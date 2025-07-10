class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        cur = self.head
        if cur and cur.data == data:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != data:
            prev = cur
            cur = cur.next
        if not cur:
            return
        prev.next = cur.next

    def remove(self, index):
        if index < 0:
            raise IndexError("Invalid index")
        cur = self.head
        if index == 0:
            if not cur:
                raise IndexError("Index out of range")
            self.head = cur.next
            return
        prev = None
        i = 0
        while cur and i < index:
            prev = cur
            cur = cur.next
            i += 1
        if not cur:
            raise IndexError("Index out of range")
        prev.next = cur.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")



ll = LinkedList()
for v in [4, 3, 6, 5]:
    ll.append(v)
ll.prepend(2)
ll.prepend(7)


ll.remove(0)   
ll.remove(2)  
ll.remove(3)   
ll.print_list()  
