from src.splay_tree import SplayTree
import unittest


class TestSplayTree(unittest.TestCase):
    """Test cases for Splay Tree implementation."""
    
    def setUp(self):
        """Initialize a new Splay tree for each test."""
        self.tree = SplayTree()
    
    def test_insert_single(self):
        """Test inserting a single element."""
        self.tree.insert(10)
        self.assertTrue(self.tree.search(10))
        self.assertEqual(self.tree.get_size(), 1)
    
    def test_insert_multiple(self):
        """Test inserting multiple elements."""
        values = [10, 20, 30, 40, 50]
        for val in values:
            self.tree.insert(val)
        
        for val in values:
            self.assertTrue(self.tree.search(val))
        self.assertEqual(self.tree.get_size(), len(values))
    
    def test_search_nonexistent(self):
        """Test searching for non-existent element."""
        self.tree.insert(10)
        self.assertFalse(self.tree.search(20))
    
    def test_delete_single(self):
        """Test deleting a single element."""
        self.tree.insert(10)
        self.tree.delete(10)
        self.assertFalse(self.tree.search(10))
        self.assertEqual(self.tree.get_size(), 0)
    
    def test_delete_multiple(self):
        """Test deleting multiple elements."""
        values = [10, 20, 30, 40, 50]
        for val in values:
            self.tree.insert(val)
        
        self.tree.delete(20)
        self.tree.delete(40)
        
        self.assertFalse(self.tree.search(20))
        self.assertFalse(self.tree.search(40))
        self.assertTrue(self.tree.search(10))
        self.assertTrue(self.tree.search(30))
        self.assertTrue(self.tree.search(50))
    
    def test_sequential_insert(self):
        """Test inserting elements sequentially."""
        for i in range(100):
            self.tree.insert(i)
        
        for i in range(100):
            self.assertTrue(self.tree.search(i))
        self.assertEqual(self.tree.get_size(), 100)
    
    def test_duplicate_insert(self):
        """Test inserting duplicate elements."""
        self.tree.insert(10)
        self.tree.insert(10)
        self.assertEqual(self.tree.get_size(), 1)
    
    def test_empty_tree_operations(self):
        """Test operations on empty tree."""
        self.assertFalse(self.tree.search(10))
        self.assertEqual(self.tree.get_size(), 0)
    
    def test_splay_behavior(self):
        """Test that frequently accessed elements move to root."""
        values = [10, 20, 30, 40, 50]
        for val in values:
            self.tree.insert(val)
        
        # Search for 30 multiple times
        for _ in range(5):
            self.tree.search(30)
        
        # After searching, 30 should be at the root
        self.assertEqual(self.tree.root.key, 30)


if __name__ == '__main__':
    unittest.main()
