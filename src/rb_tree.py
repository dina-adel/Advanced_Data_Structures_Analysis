"""
Red-Black Tree Implementation
A self-balancing binary search tree with color-based balancing properties.
"""

class Color:
    """Color constants for Red-Black Tree nodes."""
    RED = 0
    BLACK = 1


class RBNode:
    """
    Node class for Red-Black Tree.
    
    Attributes:
        key: The value stored in the node
        color: Color of the node (RED or BLACK)
        left: Reference to left child
        right: Reference to right child
        parent: Reference to parent node
    """
    def __init__(self, key, color=Color.RED):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    """
    Red-Black Tree implementation with insert, search, and delete operations.
    Maintains the following properties:
    1. Every node is either red or black
    2. Root is black
    3. All leaves (NIL) are black
    4. Red nodes have black children
    5. All paths from node to leaves have same number of black nodes
    """
    
    def __init__(self):
        """Initialize an empty Red-Black tree with NIL sentinel."""
        self.NIL = RBNode(key=None, color=Color.BLACK)
        self.root = self.NIL
        self.size = 0
    
    def rotate_left(self, x):
        """
        Perform left rotation around node x.
        
        Input: x - RBNode (node to rotate around)
        Output: None (modifies tree structure)
        """
        y = x.right
        x.right = y.left
        
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def rotate_right(self, y):
        """
        Perform right rotation around node y.
        
        Input: y - RBNode (node to rotate around)
        Output: None (modifies tree structure)
        """
        x = y.left
        y.left = x.right
        
        if x.right != self.NIL:
            x.right.parent = y
        
        x.parent = y.parent
        
        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        
        x.right = y
        y.parent = x
    
    def insert(self, key):
        """
        Insert a key into the Red-Black tree.
        
        Input: key - int value to insert
        Output: None (modifies tree structure)
        """
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL
        
        parent = None
        current = self.root
        
        # Standard BST insertion
        while current != self.NIL:
            parent = current
            if node.key < current.key:
                current = current.left
            elif node.key > current.key:
                current = current.right
            else:
                # Duplicate key
                return
        
        node.parent = parent
        
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
        
        self.size += 1
        
        # Fix Red-Black tree properties
        self._insert_fixup(node)
    
    def _insert_fixup(self, z):
        """
        Fix Red-Black tree properties after insertion.
        
        Input: z - RBNode (newly inserted node)
        Output: None (modifies tree structure)
        """
        while z.parent and z.parent.color == Color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                
                if y.color == Color.RED:
                    # Case 1: Uncle is red
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        # Case 2: z is right child
                        z = z.parent
                        self.rotate_left(z)
                    
                    # Case 3: z is left child
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                
                if y.color == Color.RED:
                    # Case 1: Uncle is red
                    z.parent.color = Color.BLACK
                    y.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        # Case 2: z is left child
                        z = z.parent
                        self.rotate_right(z)
                    
                    # Case 3: z is right child
                    z.parent.color = Color.BLACK
                    z.parent.parent.color = Color.RED
                    self.rotate_left(z.parent.parent)
        
        self.root.color = Color.BLACK
    
    def search(self, key):
        """
        Search for a key in the tree.
        
        Input: key - int value to search for
        Output: bool - True if key exists, False otherwise
        """
        current = self.root
        
        while current != self.NIL:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        
        return False
    
    def _transplant(self, u, v):
        """
        Replace subtree rooted at u with subtree rooted at v.
        
        Input: u - RBNode to replace, v - RBNode replacement
        Output: None (modifies tree structure)
        """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        """
        Find node with minimum key in subtree.
        
        Input: node - root of subtree
        Output: RBNode - node with minimum key
        """
        while node.left != self.NIL:
            node = node.left
        return node
    
    def delete(self, key):
        """
        Delete a key from the Red-Black tree.
        
        Input: key - int value to delete
        Output: None (modifies tree structure)
        """
        z = self._search_node(key)
        if z == self.NIL:
            return
        
        self.size -= 1
        y = z
        y_original_color = y.color
        
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == Color.BLACK:
            self._delete_fixup(x)
    
    def _search_node(self, key):
        """
        Search for a node with given key.
        
        Input: key - int value to find
        Output: RBNode - node with the key, or NIL if not found
        """
        current = self.root
        
        while current != self.NIL and key != current.key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
        
        return current
    
    def _delete_fixup(self, x):
        """
        Fix Red-Black tree properties after deletion.
        
        Input: x - RBNode (node that replaced deleted node)
        Output: None (modifies tree structure)
        """
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                w = x.parent.right
                
                if w.color == Color.RED:
                    # Case 1: Sibling is red
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.rotate_left(x.parent)
                    w = x.parent.right
                
                if w.left.color == Color.BLACK and w.right.color == Color.BLACK:
                    # Case 2: Sibling's children are black
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.right.color == Color.BLACK:
                        # Case 3: Sibling's right child is black
                        w.left.color = Color.BLACK
                        w.color = Color.RED
                        self.rotate_right(w)
                        w = x.parent.right
                    
                    # Case 4: Sibling's right child is red
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.right.color = Color.BLACK
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                
                if w.color == Color.RED:
                    # Case 1: Sibling is red
                    w.color = Color.BLACK
                    x.parent.color = Color.RED
                    self.rotate_right(x.parent)
                    w = x.parent.left
                
                if w.right.color == Color.BLACK and w.left.color == Color.BLACK:
                    # Case 2: Sibling's children are black
                    w.color = Color.RED
                    x = x.parent
                else:
                    if w.left.color == Color.BLACK:
                        # Case 3: Sibling's left child is black
                        w.right.color = Color.BLACK
                        w.color = Color.RED
                        self.rotate_left(w)
                        w = x.parent.left
                    
                    # Case 4: Sibling's left child is red
                    w.color = x.parent.color
                    x.parent.color = Color.BLACK
                    w.left.color = Color.BLACK
                    self.rotate_right(x.parent)
                    x = self.root
        
        x.color = Color.BLACK
    
    def get_size(self):
        """
        Get number of nodes in the tree.
        
        Input: None
        Output: int - number of nodes
        """
        return self.size
