import time
import random
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.btree = None
        self.arr = []
    
    def add(self,data):
        self.add_node(self.btree, data)

    def add_node(self,node,data):
        if self.btree == None:
            node_ = Node(data)
            self.btree = node_
        else:
            if data <= node.data:
                if node.left == None:
                    temp_node = Node(data)
                    node.left = temp_node
                else:
                    self.add_node(node.left,data)
            else:
                if node.right == None:
                    temp_node = Node(data)
                    node.right = temp_node
                else:
                    self.add_node(node.right, data)
    
    def add_no_recur(self,data):
        self.add_node_no_recur(self.btree, data)
    
    def add_node_no_recur(self, node, data):
        if self.btree == None:
            node_ = Node(data)
            self.btree = node_
        else:
            while 1:
                if data <= node.data:
                    if node.left == None:
                        temp_node = Node(data)
                        node.left = temp_node
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        temp_node = Node(data)
                        node.right = temp_node
                        break
                    else:
                        node = node.right
    
    def inorder(self):
        return self.print_inorder(self.btree)
    
    def print_inorder(self,node):
        if node != None:
            self.print_inorder(node.left)
            if node != None:
                self.arr.append(node.data)
            self.print_inorder(node.right)
        return self.arr

    def search_data(self,node,data):
        i = 0
        start_time = time.time()
        while node != None:
            if node.data == data:
                print i,"\niterations\n"
                print '{:.6f}'.format((time.time() - start_time))
                return True
            elif data > node.data:
                node = node.right
            else:
                node = node.left
            i += 1
        return False
    
    def search(self,data):
        return self.search_data(self.btree,data)

b_tree = bst()
arr = []
print "\nMaking array\n"
while len(arr[:]) < 10000:
    num = random.randint(1, 10000)
    if num not in arr:
        arr.append(num)
for x in arr:
    b_tree.add_no_recur(x)
print b_tree.search(25)
start_time = time.time()
if 25 in arr:
    print arr.index(25)
print '{:.6f}'.format((time.time() - start_time))
