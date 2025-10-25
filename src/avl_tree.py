"""
AVL Tree Implementation
A self-balancing binary search tree with strict balance factor constraint.
"""

class AVLNode:
    """
    Node class for AVL Tree.
    
    Attributes:
        key: The value stored in the node
        left: Reference to left child
        right: Reference to right child
        height: Height of the subtree rooted at this node
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """
    AVL Tree implementation with insert, search, and delete operations.
    Maintains balance factor of -1, 0, or 1 for all nodes.
    """
    
    def __init__(self):
        """Initialize an empty AVL tree."""
        self.root = None
        self.size = 0
    
    def get_height(self, node):
        """
        Get height of a node.
        
        Input: node - AVLNode or None
        Output: int - height of the node (0 if None)
        """
        if not node:
            return 0
        return node.height
    
    def get_balance(self, node):
        """
        Calculate balance factor of a node.
        
        Input: node - AVLNode
        Output: int - balance factor (left height - right height)
        """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        """
        Update height of a node based on children's heights.
        
        Input: node - AVLNode
        Output: None (modifies node.height in place)
        """
        if node:
            node.height = 1 + max(self.get_height(node.left), 
                                  self.get_height(node.right))
    
    def rotate_right(self, z):
        """
        Perform right rotation around node z.
        
        Input: z - AVLNode (root of subtree to rotate)
        Output: AVLNode - new root of rotated subtree
        """
        y = z.left
        T3 = y.right
        
        # Perform rotation
        y.right = z
        z.left = T3
        
        # Update heights
        self.update_height(z)
        self.update_height(y)
        
        return y
    
    def rotate_left(self, z):
        """
        Perform left rotation around node z.
        
        Input: z - AVLNode (root of subtree to rotate)
        Output: AVLNode - new root of rotated subtree
        """
        y = z.right
        T2 = y.left
        
        # Perform rotation
        y.left = z
        z.right = T2
        
        # Update heights
        self.update_height(z)
        self.update_height(y)
        
        return y
    
    def insert(self, key):
        """
        Insert a key into the AVL tree.
        
        Input: key - int value to insert
        Output: None (modifies tree structure)
        """
        self.root, inserted = self._insert_helper(self.root, key)
        if inserted:
            self.size += 1

    
    def _insert_helper(self, node, key):
        """
        Recursive helper for insertion with balancing.
        
        Input: node - current node, key - value to insert
        Output: AVLNode - root of balanced subtree
                inserted - a flag to signify if it was inserted or not
        """
        # Standard BST insertion
        if not node:
            return AVLNode(key), True
        
        if key < node.key:
            node.left, inserted = self._insert_helper(node.left, key)
        elif key > node.key:
            node.right, inserted = self._insert_helper(node.right, key)
        else:
            # Duplicate keys not allowed
            return node, False
        
        # Update height
        self.update_height(node)
        
        # Get balance factor
        balance = self.get_balance(node)
        
        # Left-Left Case
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node), inserted
        
        # Right-Right Case
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node), inserted
        
        # Left-Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node), inserted
        
        # Right-Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node), inserted
        
        return node, inserted
    
    def search(self, key):
        """
        Search for a key in the tree.
        
        Input: key - int value to search for
        Output: bool - True if key exists, False otherwise
        """
        return self._search_helper(self.root, key)
    
    def _search_helper(self, node, key):
        """
        Recursive helper for search operation.
        
        Input: node - current node, key - value to find
        Output: bool - True if found, False otherwise
        """
        if not node:
            return False
        
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_helper(node.left, key)
        else:
            return self._search_helper(node.right, key)
    
    def get_min_node(self, node):
        """
        Find the node with minimum key in a subtree.
        
        Input: node - root of subtree
        Output: AVLNode - node with minimum key
        """
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, key):
        """
        Delete a key from the AVL tree.
        
        Input: key - int value to delete
        Output: None (modifies tree structure)
        """
        self.root = self._delete_helper(self.root, key)
        self.size -= 1
    
    def _delete_helper(self, node, key):
        """
        Recursive helper for deletion with balancing.
        
        Input: node - current node, key - value to delete
        Output: AVLNode - root of balanced subtree
        """
        # Standard BST deletion
        if not node:
            return node
        
        if key < node.key:
            node.left = self._delete_helper(node.left, key)
        elif key > node.key:
            node.right = self._delete_helper(node.right, key)
        else:
            # Node with one child or no child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            # Node with two children
            temp = self.get_min_node(node.right)
            node.key = temp.key
            node.right = self._delete_helper(node.right, temp.key)
        
        # Update height
        self.update_height(node)
        
        # Get balance factor
        balance = self.get_balance(node)
        
        # Left-Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        
        # Left-Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        # Right-Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        
        # Right-Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def get_size(self):
        """
        Get number of nodes in the tree.
        
        Input: None
        Output: int - number of nodes
        """
        return self.size
