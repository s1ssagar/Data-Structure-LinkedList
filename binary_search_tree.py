from datetime import datetime
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
    
    def inorder(self):
        return self.print_inorder(self.btree)
    
    def print_inorder(self,node):
        if node != None:
            self.print_inorder(node.left)
            if node != None:
                self.arr.append(node.data)
            self.print_inorder(node.right)
        return self.arr

b_tree = bst()
for x in range(100,1,-1):
    b_tree.add(x)
time = datetime.now()
print b_tree.inorder()
