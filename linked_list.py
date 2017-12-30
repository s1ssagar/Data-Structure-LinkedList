class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node
        
    def __str__(self):
        p = self.head
        s = ''
        while p.next != None:
            s += p.data
            p = p.next
        s += p.data
        return s

    def search_data(self,data):
        n = self.head
        while n.next != None:
            if n.data == data:
                return True
            n = n.next
        return False
    
    def remove_data(self,data):
        n = self.head
        while n.next != None:
            if n.data == data:
                n.prev.next = n.next
                n.next.prev = n.prev
                break
            n = n.next
        print "%s not found in linked list"%(data)


l = LinkedList()
l.add('x')
l.add('y')
l.add('z')
print str(l)[::-1]
print l.search_data('t')
l.remove_data('t')
print l