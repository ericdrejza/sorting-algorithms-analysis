class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


class BST:
    def __init__(self, *nodes):
        self.head = None
        for n in nodes:
            if isinstance(n, int):
                self.insert(n)
            elif isinstance(n, list):
                for i in n:
                    self.insert(i)
        
    def insert(self, node):
        if isinstance(node, int):
            node = Node(node)

        if self.head == None:
            self.head = node
            return
        
        curr = self.head
        placed = False
        while not placed:
            if node.value <= curr.value:
                if curr.left == None:
                    curr.set_left(node)
                    placed = True
                    return
                else:
                    curr = curr.left
            else:
                if curr.right == None:
                    curr.set_right(node)
                    placed = True
                    return
                else:
                    curr = curr.right

    def in_order_traveral(self, root, array):
        if self.head == None:
            print("Tree is empty")
            return
        
        # Go Left
        if root.left != None:
            self.in_order_traveral(root.left, array)
        
        # Add current node value to the sorted array
        array.append(root.value)

        # Go Right
        if root.right != None:
            self.in_order_traveral(root.right, array)
    

def bst_sort(array):
    bst = BST(array)
    array.clear()
    bst.in_order_traveral(bst.head, array)


if __name__ == "__main__":
    L = [2, 5, 3, 8, 1, 9, 4]
    print(L)
    bst_sort(L)
    print(L)
    # print(str(n.value) + "; right = " + str(n.right.value))
