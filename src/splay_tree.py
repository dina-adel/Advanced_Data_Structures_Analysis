"""
Splay Tree Implementation
A self-adjusting binary search tree with move-to-root heuristic.
"""

class SplayNode:
    """
    Node class for Splay Tree.
    
    Attributes:
        key: The value stored in the node
        left: Reference to left child
        right: Reference to right child
        parent: Reference to parent node
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    """
    Splay Tree implementation with insert, search, and delete operations.
    Uses splaying operation to move accessed nodes to the root.
    Provides amortized O(log n) performance for operations.
    """
    
    def __init__(self):
        """Initialize an empty Splay tree."""
        self.root = None
        self.size = 0
    
    def rotate_right(self, x):
        """
        Perform right rotation around node x.
        
        Input: x - SplayNode (node to rotate around)
        Output: None (modifies tree structure)
        """
        y = x.left
        x.left = y.right
        
        if y.right:
            y.right.parent = x
        
        y.parent = x.parent
        
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.right = x
        x.parent = y
    
    def rotate_left(self, x):
        """
        Perform left rotation around node x.
        
        Input: x - SplayNode (node to rotate around)
        Output: None (modifies tree structure)
        """
        y = x.right
        x.right = y.left
        
        if y.left:
            y.left.parent = x
        
        y.parent = x.parent
        
        if not x.parent:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def splay(self, x):
        """
        Splay operation: move node x to the root using rotations.
        
        Input: x - SplayNode (node to splay to root)
        Output: None (modifies tree structure)
        """
        while x.parent:
            if not x.parent.parent:
                # Zig step: x's parent is root
                if x == x.parent.left:
                    self.rotate_right(x.parent)
                else:
                    self.rotate_left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # Zig-Zig step: x and parent are both left children
                self.rotate_right(x.parent.parent)
                self.rotate_right(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # Zig-Zig step: x and parent are both right children
                self.rotate_left(x.parent.parent)
                self.rotate_left(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # Zig-Zag step: x is right child, parent is left child
                self.rotate_left(x.parent)
                self.rotate_right(x.parent)
            else:
                # Zig-Zag step: x is left child, parent is right child
                self.rotate_right(x.parent)
                self.rotate_left(x.parent)
    
    def insert(self, key):
        """
        Insert a key into the Splay tree.
        
        Input: key - int value to insert
        Output: None (modifies tree structure)
        """
        node = SplayNode(key)
        
        if not self.root:
            self.root = node
            self.size += 1
            return
        
        current = self.root
        parent = None
        
        # Standard BST insertion
        while current:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                # Duplicate key, splay it and return
                self.splay(current)
                return
        
        node.parent = parent
        
        if key < parent.key:
            parent.left = node
        else:
            parent.right = node
        
        self.size += 1
        
        # Splay the newly inserted node to root
        self.splay(node)
    
    def search(self, key):
        """
        Search for a key in the tree.
        
        Input: key - int value to search for
        Output: bool - True if key exists, False otherwise
        """
        current = self.root
        
        while current:
            if key == current.key:
                # Found the key, splay it to root
                self.splay(current)
                return True
            elif key < current.key:
                if not current.left:
                    # Key not found, splay last accessed node
                    self.splay(current)
                    return False
                current = current.left
            else:
                if not current.right:
                    # Key not found, splay last accessed node
                    self.splay(current)
                    return False
                current = current.right
        
        return False
    
    def _subtree_minimum(self, node):
        """
        Find node with minimum key in subtree.
        
        Input: node - root of subtree
        Output: SplayNode - node with minimum key
        """
        while node.left:
            node = node.left
        return node
    
    def _subtree_maximum(self, node):
        """
        Find node with maximum key in subtree.
        
        Input: node - root of subtree
        Output: SplayNode - node with maximum key
        """
        while node.right:
            node = node.right
        return node
    
    def delete(self, key):
        """
        Delete a key from the Splay tree.
        
        Input: key - int value to delete
        Output: None (modifies tree structure)
        """
        # First, search for the node (this splays it to root)
        if not self.search(key):
            return
        
        # At this point, the node with key is at the root
        if not self.root.left:
            # No left subtree
            self.root = self.root.right
            if self.root:
                self.root.parent = None
        elif not self.root.right:
            # No right subtree
            self.root = self.root.left
            if self.root:
                self.root.parent = None
        else:
            # Both subtrees exist
            # Find maximum in left subtree
            left_subtree = self.root.left
            right_subtree = self.root.right
            
            # Disconnect right subtree
            right_subtree.parent = None
            
            # Make left subtree the new root
            self.root = left_subtree
            self.root.parent = None
            
            # Find maximum in left subtree (will be splayed to root)
            max_node = self._subtree_maximum(self.root)
            self.splay(max_node)
            
            # Attach right subtree to the new root
            self.root.right = right_subtree
            right_subtree.parent = self.root
        
        self.size -= 1
    
    def get_size(self):
        """
        Get number of nodes in the tree.
        
        Input: None
        Output: int - number of nodes
        """
        return self.size
