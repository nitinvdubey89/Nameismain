class TreeComparator:

    def compare(self, node1, node2):
         # check the basse case(so node1 and node2 maybe the  nodes of leaf node
         # node1 may be none  or node2 maybe none
         #
         if not node1 or not node2:
             return node1 == node2

         # we have to check the values in the nodes
         if node1.data is not node2.data:
             return False

         # check all the left and right subtrees(children) recursiverly
         return self.compare(node1.left_node, node2.left_node) and \
                self.compare(node1.right_node, node2.right_node)



class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        # when implementing the remove function
        self.parent = parent

class BinarySearchTree:

    def __init__(self):
        # we can access the root node exclusively
        self.root =  None

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        # first we have to find the node we have to remove
        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)## considering left  sub-tree
        elif data > node.data:
            self.remove_node(data, node.right_node) ## considering right sub-tree
        else:
            # we have found the node we wanted to remove
            #there are 3 options
            # LEAF NODE CASE
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node ... %d" %node.data)
                parent = node.parent
                print("this is {node.parent}")

                if parent is not None and parent.left_node == None:
                    parent.left_node = None
                if parent is not None and parent.right_node == None:
                    parent.right_node = None

                if parent is None:
                    self.root == None

                del node


            # When there is a single child
            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with the single right child...")
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node # updateing the parent to child
                if parent is None:
                    self.root = None

                node.right_node.parent = parent # updating the child to parent
                del node
            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with the single right child...")
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node # updateing the parent to child


                else:
                    self.root = node.left_node

                node.right_node.parent = parent
            else:
                print("Removing node with two children")
                predecessor = self.get_predecessor(node.left_node)

                # swap the node and predecessor
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)


    def get_predecessor(self, node):
       if node.right_node:
           return self.get_predecessor(node.right_node)

       return node




    def insert(self, data):
        # this is the first node in the binary search tree, # r oot node nodes not have parent
        if self.root is None:
            self.root = Node(data)
        # the BST is not empty
        else:
            self.insert_node(data, self.root)

    def insert_node(self,data,node):
        # we have to go to the left subtree
        #print(f"{node.data}, just checking the flow for node")
        #(f"{data}, just checking the flow for data ")
        if data < node.data:
            if node.left_node: # this line is same as " if node.left_node is not None"
                print(f"{node.left_node} nanananana")
                print(f"{node.data} dadadadada")
                self.insert_node(data,node.left_node)

            else:
                # there is no left child therefore we create one
                print(f"{node.left_node} nanananana")
                print(f"{node.data} dadadadada")
                node.left_node = Node(data,node)
        else:
            #print(f"{data} and {node.data} is the else category")
            if node.right_node:
                self.insert_node(data, node.right_node)
                print(f"{node.left_node} nanananana")
                print(f"{node.data} dadadadada")

            else:
                #print(f"{node.data} and {data} and {node} is when node.righ_node is none")
                node.right_node = Node(data, node)

    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self,node):
        if node.left_node: # this means that node is not a None
           return self.get_min_value(node.left_node)  # recursion
        return  node.data

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self,node):
        if node.right_node: # this means that node is not a None
            self.get_max_value(node.right_node)
        return  node.data

    def traverse(self):
        if self.root: # this is to check whether self.root is   not null
            self.traverse_in_order(self.root)

    # it has O(N) linear runnning  time complexity
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)
        print(node.data)
        if node.right_node:
            self.traverse_in_order(node.right_node)






if  __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)

          #     1
          #         2
          #             3
          #                4
          #                    5

    bst.remove(5)

    bst1 = BinarySearchTree()
    bst1.insert(5)

    bst2 = BinarySearchTree()
    bst2.insert(5)
    
    comparator = TreeComparator()
    print(comparator.compare(bst1.root,bst2.root))

    print('Max value : %s' % bst.get_max())
    print('Max value : %s' % bst.get_min())

    bst.traverse()

