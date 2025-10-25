# COSC 520 Assignment 2: Advanced Data Structures Analysus

This project implements and benchmarks three self-balancing binary search tree data structures: AVL Tree, Red-Black Tree, and Splay Tree.

## Project Structure

```
├── datasets/     # datasets hanling and generation
  ├──  dataset_generator.py

├── src/ 
  ├── avl_tree.py          # AVL Tree implementation
  ├── rb_tree.py           # Red-Black Tree implementation
  ├── splay_tree.py        # Splay Tree implementation

├── tests/                 # unittests for all 
  ├── test_avl.py
  ├── test_rb.py
  ├── test_splay.py

├── benchmark.py         # Comprehensive benchmarking
├── demo.py         # A user friendly demo file

├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Requirements

- Python 3.8 or higher
- Required packages (install via `pip install -r requirements.txt`):

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dina-adel/Advanced_Data_Structures_Analysis.git
cd Advanced_Data_Structures_Analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Code

### Unit Tests

Run all unit tests to verify implementations:
```bash
pytest
```

### Demo 
You can run a demo using:
```bash
python demo.py
```
You will be prompted to choose from a list as follows:
```bash
--- 🌳 Tree Benchmark Demo ---
Please choose a benchmark to run:
  [1] Insert - Random Data
  [2] Insert - Sequential Data
  [3] Search - Random Data
  [4] Search - Sequential Data
  [5] Delete - Random Data
  [6] Delete - Sequential Data
  [7] Mixed Workload (Random): 60% insert, 30% search, 10% delete operations
  ------------------------------
  [q] Quit
---------------------------------
Enter your choice: |
```
Then you can specify the size of your test:
```bash
Enter your choice: 1
  ... Enter dataset size (e.g., 50000): xxxx
```

### Benchmarks

Run the complete benchmark suite (may take hours depending on hardware):
```bash
python benchmark.py
```
Or you can specify an output file as follows:
```bash
python benchmark.py benchmark_results.json
```

This will:
- Test datasets from 10,000 to 10,000,000 elements
- Benchmark insert, search, and delete operations
- Test random, skew and sequential data patterns
- Generate performance plots (saved as PNG files)
- Save results to `benchmark_results.json` or any specified file

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

## Dataset
The benchmark file generates synthetic datasets of various sizes. Datasets and results can be found:
- Dataset link: 
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

- Dina A. Elkholy
- COSC 520 - Advanced Data Structures
- University of British Columbia



This project is for academic purposes as part of COSC 520 coursework.
