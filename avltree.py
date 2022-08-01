class Node:


    def __init__(self, data , parent): ## parent and data are injected from outside
        self.data  = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0

class AVLTree:

    def __init__(self):
        # we can access the root node exclusively
        self.root = None

    def remove(self, data,):
        if self.root:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)  ## considering left  sub-tree
        elif data > node.data:
            self.remove_node(data, node.right_node)  ## considering right sub-tree
        else:
            # we have found the node we wanted to remove
            # there are 3 options
            # case 1) if the node is a leaf node

            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node ... %d" % node.data)
                parent = node.parent
                print(f"this is {node.parent}")

                if parent is not None and parent.left_node == None:
                    parent.left_node = None
                if parent is not None and parent.right_node == None:
                    parent.right_node = None

                if parent is None:
                    self.root == None

                del node

            # case 2) if the node has a single child
            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with the single right child...")
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node  # updateing the parent to child
                if parent is None:
                    self.root = None

                node.right_node.parent = parent  # updating the child to parent
                del node
            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with the single right child...")
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node  # updateing the parent to child
                else:
                    self.root = node.left_node

                node.right_node.parent = parent
                del node

                self.handle_vilation(parent)
            # when the node can have two children
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
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data , node):
        # we have to consider the left subtree
        if data < node.data:
            # we have to check if the left node is a none
            # when the left child is not a None
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node) # heere node is the parent node.
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
        else:
            # we have to check if the right node is a none
            # when the right child is not a None
            if node.right_node:
                self.insert_node(data, node.left_node)
            else:
                node.right_node = Node(data, node)  # heere node is the parent node.
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1

            # after every insertion we need to check whether the AVL properties are violated or not
        self.handle_violations(node)

