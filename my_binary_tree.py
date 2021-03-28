class node:

    def __init__(self):
        self.child_left = None
        self.child_right = None
        self.value = None

class my_tree:
    
    def __init__(self):
        self.tree_root = node()

    def add_number(self, curr_node, number):

        if((curr_node.child_left == None) 
        and (curr_node.child_right == None)
        and (curr_node.value == None)):
            
            curr_node.value = number

        elif((curr_node.child_left == None) and (curr_node.child_right == None)):
            if (curr_node.value >= number):
                curr_node.child_left = node()
                self.add_number(curr_node.child_left, number)
            else:
                curr_node.child_right = node()
                self.add_number(curr_node.child_right, number)
        
        elif(curr_node.child_left == None):
            if (curr_node.value >= number):
                curr_node.child_left = node()
                self.add_number(curr_node.child_left, number)
            else:
                self.add_number(curr_node.child_right, number)

        elif(curr_node.child_right == None):
            if (curr_node.value >= number):
                self.add_number(curr_node.child_left, number)
            else:
                curr_node.child_right = node()
                self.add_number(curr_node.child_right, number)

        else:
            if (curr_node.value >= number):
                
                self.add_number(curr_node.child_left, number)
            else:
                
                self.add_number(curr_node.child_right, number)
    
    def add_2_tree(self, number):
        self.add_number(self.tree_root, number)

    def print_tree(self):
        self.print_node(self.tree_root)

    def print_node(self, c_node):
        if(c_node.child_left != None):
            self.print_node(c_node.child_left)

        print(c_node.value)

        if(c_node.child_right != None):
            self.print_node(c_node.child_right)

    def invert_tree(self):
        self.invert_node(self.tree_root)
        self.print_tree()

    def invert_node(self, c_node):

        new_node = c_node.child_left
        c_node.child_left = c_node.child_right
        c_node.child_right = new_node
        
        if(c_node.child_left != None):
            self.invert_node(c_node.child_left)

        if(c_node.child_right != None):
            self.invert_node(c_node.child_right)
        

if __name__ == '__main__':
    
    cool_tree = my_tree()

    cool_tree.add_2_tree(5)
    cool_tree.add_2_tree(9)
    cool_tree.add_2_tree(2)
    cool_tree.add_2_tree(8)
    cool_tree.add_2_tree(7)
    cool_tree.add_2_tree(3)
    cool_tree.add_2_tree(6)
    cool_tree.add_2_tree(1)
    cool_tree.add_2_tree(4)

    cool_tree.print_tree()
    
    print('invert!')
    cool_tree.invert_tree()