
#Nomor 2
class CreateNode:
    def __init__(self, data):
        self.data = data
        self.children_left = None
        self.children_right = None

# Root node
Root = CreateNode(41)

# Level 1
Root.children_left = CreateNode(20)
Root.children_right = CreateNode(65)

# Level 2 (KIRI)
Root.children_left.children_left = CreateNode(11)
Root.children_left.children_right = CreateNode(29)

# Level 2 (KANAN)
Root.children_right.children_left = CreateNode(50)
Root.children_right.children_right = CreateNode(91)

# Level 3 (KIRI)
#Root.children_left.children_left.children_left = CreateNode()
#Root.children_left.children_left.children_right = CreateNode()
#Root.children_left.children_right.children_left = CreateNode()
Root.children_left.children_right.children_right = CreateNode(32)

# Level 3 (KANAN)
#Root.children_right.children_left.children_left = CreateNode()
#Root.children_right.children_left.children_right = CreateNode()
Root.children_right.children_right.children_left = CreateNode(72)
Root.children_right.children_right.children_right = CreateNode(99)

# Pre-Order Traversal
def pre_order_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        pre_order_traversal(node.children_left)
        pre_order_traversal(node.children_right)

# In-Order Traversal
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.children_left)
        print(node.data, end=" ")
        in_order_traversal(node.children_right)

# Post-Order Traversal
def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.children_left)
        post_order_traversal(node.children_right)
        print(node.data, end=" ")

# Menampilkan hasil traversal
print("Pre-Order Traversal:")
pre_order_traversal(Root)
print("\nIn-Order Traversal:")
in_order_traversal(Root)
print("\nPost-Order Traversal:")
post_order_traversal(Root)

#Nomor 1
class CreateNode:
    def __init__(self, data):
        self.data = data
        self.children_left = None
        self.children_right = None

# Root node
Root = CreateNode(73)

# Level 1
Root.children_left = CreateNode(35)
Root.children_right = CreateNode(82)

# Level 2 (KIRI)
Root.children_left.children_left = CreateNode(14)
Root.children_left.children_right = CreateNode(50)

# Level 2 (KANAN)
#Root.children_right.children_left = CreateNode()
Root.children_right.children_right = CreateNode(83)

# Level 3 (KIRI)
#Root.children_left.children_left.children_left = CreateNode()
Root.children_left.children_left.children_right = CreateNode(29)
#Root.children_left.children_right.children_left = CreateNode()
Root.children_left.children_right.children_right = CreateNode(62)

# Level 3 (KANAN)
#Root.children_right.children_right.children_left = CreateNode()
Root.children_right.children_right.children_right = CreateNode(94)

# Level 4 (KIRI)
#Root.children_left.children_left.children_left.children_left = CreateNode()
#Root.children_left.children_left.children_left.children_right = CreateNode()
Root.children_left.children_left.children_right.children_left = CreateNode(15)
#Root.children_left.children_left.children_right.children_right = CreateNode()
#Root.children_left.children_right.children_left.children_left = CreateNode()
#Root.children_left.children_right.children_left.children_right = CreateNode()
Root.children_left.children_right.children_right.children_left = CreateNode(15)
#Root.children_left.children_right.children_right.children_right = CreateNode()

# Level 4 (KANAN)
# Level 4 (KANAN)  
#Root.children_right.children_left.children_left.children_left = CreateNode()
#Root.children_right.children_left.children_left.children_right = CreateNode()
#Root.children_right.children_left.children_right.children_left = CreateNode()
#Root.children_right.children_left.children_right.children_right = CreateNode()
#Root.children_right.children_right.children_left.children_left = CreateNode()
#Root.children_right.children_right.children_left.children_right = CreateNode()
Root.children_right.children_right.children_right.children_left = CreateNode(93)
Root.children_right.children_right.children_right.children_right = CreateNode(97)

# Pre-Order Traversal
def pre_order_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        pre_order_traversal(node.children_left)
        pre_order_traversal(node.children_right)

# In-Order Traversal
def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.children_left)
        print(node.data, end=" ")
        in_order_traversal(node.children_right)

# Post-Order Traversal
def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.children_left)
        post_order_traversal(node.children_right)
        print(node.data, end=" ")

# Menampilkan hasil traversal
print("Pre-Order Traversal:")
pre_order_traversal(Root)
print("\nIn-Order Traversal:")
in_order_traversal(Root)
print("\nPost-Order Traversal:")
post_order_traversal(Root)