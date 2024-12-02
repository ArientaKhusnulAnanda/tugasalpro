class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            print("Rotasi kanan pada node:", root.key)
            return self.right_rotate(root)
        
        # Right Right Case
        if balance < -1 and key > root.right.key:
            print("Rotasi kiri pada node:", root.key)
            return self.left_rotate(root)
        
        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            print("Rotasi Kanan pada node:", root.key)
            return self.right_rotate(root)
        
        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            print("Rotasi kiri pada node:", root.key)
            return self.left_rotate(root)
        return root
    
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y
    
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def pre_order(self, root):
        if not root:
            return
        print("{0}".format(root.key), end=" ")
        self.pre_order(root.left)
        self.pre_order(root.right)
        
    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left)
        print("{0}".format(root.key), end=" ")
        self.in_order(root.right)
    
    def post_order(self, root):
        if not root:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print("{0}".format(root.key), end=" ")

    def print_tree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.key))
            self.print_tree(root.left, level + 1, "L--- ")
            self.print_tree(root.right, level + 1, "R--- ")

# Main program
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    
    values = [3, 6, 7, 14, 26, 31, 46, 50, 57, 58, 60, 61, 64, 68, 69, 71, 77, 78, 92, 96]
    for value in values:
        print(f"\nMenyisipkan {value} ke dalam AVL Tree:")
        root = avl_tree.insert(root, value)
        avl_tree.print_tree(root)  


    print("\nPre-order traversal dari AVL tree yang sudah seimbang: ")
    avl_tree.pre_order(root)
    print()  
    
    print("\nIn-order traversal dari AVL tree yang sudah seimbang: ")
    avl_tree.in_order(root)
    print()  
    
    print("\nPost-order traversal dari AVL tree yang sudah seimbang: ")
    avl_tree.post_order(root)
    print()  
