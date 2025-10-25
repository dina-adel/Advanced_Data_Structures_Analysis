# COSC 520 Assignment 2: Advanced Data Structures Comparison

This project implements and benchmarks three self-balancing binary search tree data structures: AVL Tree, Red-Black Tree, and Splay Tree.

## Project Structure

```
.
├── avl_tree.py          # AVL Tree implementation
├── rb_tree.py           # Red-Black Tree implementation
├── splay_tree.py        # Splay Tree implementation
├── test_trees.py        # Unit tests for all trees
├── benchmark.py         # Comprehensive benchmarking suite
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Requirements

- Python 3.8 or higher
- Required packages (install via `pip install -r requirements.txt`):
  - numpy
  - matplotlib

## Installation

1. Clone the repository:
```bash
git clone <your-github-repo-url>
cd <repo-name>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Code

### Unit Tests

Run all unit tests to verify implementations:
```bash
python test_trees.py
```

Run tests with verbose output:
```bash
python test_trees.py -v
```

### Benchmarks

Run the complete benchmark suite (may take 10-30 minutes depending on hardware):
```bash
python benchmark.py
```

This will:
- Test datasets from 10,000 to 10,000,000 elements
- Benchmark insert, search, and delete operations
- Test both random and sequential data patterns
- Generate performance plots (saved as PNG files)
- Save results to `benchmark_results.json`

### Individual Tree Usage

You can also use the trees individually in your own code:

```python
from avl_tree import AVLTree
from rb_tree import RedBlackTree
from splay_tree import SplayTree

# Create a tree
tree = AVLTree()  # or RedBlackTree() or SplayTree()

# Insert elements
tree.insert(10)
tree.insert(20)
tree.insert(5)

# Search for elements
found = tree.search(10)  # Returns True

# Delete elements
tree.delete(20)

# Get tree size
size = tree.get_size()
```

## Implementation Details

### AVL Tree (avl_tree.py)
- Strictly balanced binary search tree
- Balance factor: {-1, 0, 1}
- Uses single and double rotations
- Guarantees O(log n) height

### Red-Black Tree (rb_tree.py)
- Self-balancing BST with color properties
- Nodes colored RED or BLACK
- Maintains 5 key properties for balance
- More relaxed balancing than AVL

### Splay Tree (splay_tree.py)
- Self-adjusting BST
- Move-to-root heuristic via splaying
- Amortized O(log n) performance
- Recently accessed elements near root

## Code Quality

All code follows best practices:
- **Naming**: Clear, descriptive variable and method names
- **Documentation**: Every method includes docstring with input/output description
- **Comments**: Complex logic explained with inline comments
- **Testing**: Comprehensive unit tests for all operations
- **Clean code**: Modular design with single responsibility principle

## Dataset

The benchmark suite generates synthetic datasets of various sizes. Datasets and results can be found:
- Dataset link: [Will be added after upload to GitHub/cloud storage]
- Results: `benchmark_results.json`
- Plots: `*_benchmark.png` files

## Performance Summary

Expected complexity for all three trees:

| Operation | AVL Tree | Red-Black Tree | Splay Tree |
|-----------|----------|----------------|------------|
| Insert    | O(log n) | O(log n)       | O(log n)* |
| Search    | O(log n) | O(log n)       | O(log n)* |
| Delete    | O(log n) | O(log n)       | O(log n)* |

*Amortized complexity for Splay Tree

## Authors

- [Your Name]
- COSC 520 - Advanced Data Structures
- University of British Columbia

## References

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.
2. Adelson-Velsky, G., & Landis, E. M. (1962). An algorithm for the organization of information. *Soviet Mathematics Doklady*, 3, 1259-1263.
3. Bayer, R. (1972). Symmetric binary B-trees: Data structure and maintenance algorithms. *Acta Informatica*, 1(4), 290-306.
4. Sleator, D. D., & Tarjan, R. E. (1985). Self-adjusting binary search trees. *Journal of the ACM*, 32(3), 652-686.

## License

This project is for academic purposes as part of COSC 520 coursework.
