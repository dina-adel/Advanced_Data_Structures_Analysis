"""
Comprehensive benchmarking suite for AVL, Red-Black, and Splay Trees.
Measures performance across different operations and workload patterns.
"""

import time
import random
import numpy as np 
import sys
import os
import matplotlib.pyplot as plt
import json
from src.avl_tree import AVLTree
from src.rb_tree import RedBlackTree
from src.splay_tree import SplayTree


class Benchmark:
    """
    Benchmark class for comparing tree data structures.
    Measures insert, search, and delete operations.
    """
    
    def __init__(self):
        """Initialize benchmark with empty results dictionary."""
        self.results = {
            'avl': {'insert': {}, 'search': {}, 'delete': {}, 'mixed': {}},
            'rb': {'insert': {}, 'search': {}, 'delete': {}, 'mixed': {}},
            'splay': {'insert': {}, 'search': {}, 'delete': {}, 'mixed': {}}
        }
    
    def generate_random_data(self, size):
        """
        Generate random integer dataset.
        
        Input: size - int (number of elements)
        Output: list of unique random integers
        """
        return random.sample(range(size * 10), size)
    
    def generate_sequential_data(self, size):
        """
        Generate sequential integer dataset.
        
        Input: size - int (number of elements)
        Output: list of sequential integers
        """
        return list(range(size))
    
    def generate_skewed_search_keys(self, data_list, num_searches, skew_factor=1.1):
        """
        Generate search keys following a Zipfian (skewed) distribution.
        A few items will be searched for very often.
        
        Input: data_list - list of unique items in the tree
               num_searches - total number of search operations to generate
               skew_factor - 'a' parameter for Zipf dist. > 1. Closer to 1 = more skew.
        Output: list of search keys
        """
        num_unique_items = len(data_list)
        
        # 1. Create the probabilities for each item
        # Ranks from 1 to N
        ranks = np.arange(1, num_unique_items + 1)
        # Probabilities following P ~ 1 / rank^a
        probabilities = 1.0 / (ranks ** skew_factor)
        # Normalize probabilities so they sum to 1
        probabilities /= np.sum(probabilities)
        
        # 2. Use numpy.random.choice to pick items based on their probability
        # This will pick from data_list, num_searches times, using the
        # probabilities we just calculated.
        search_keys = np.random.choice(data_list, size=num_searches, p=probabilities)
        
        return list(search_keys)
    
    def benchmark_insert(self, tree_class, data, tree_name):
        """
        Benchmark insert operation.
        
        Input: tree_class - class to instantiate
               data - list of values to insert
               tree_name - string identifier for results
        Output: float - elapsed time in seconds
        """
        tree = tree_class()
        
        start_time = time.perf_counter()
        for value in data:
            tree.insert(value)
        end_time = time.perf_counter()
        
        return end_time - start_time
    
    def benchmark_search(self, tree_class, data, search_keys, tree_name):
        """
        Benchmark search operation.
        
        Input: tree_class - class to instantiate
               data - list of values to insert first
               search_keys - list of keys to search for
               tree_name - string identifier for results
        Output: float - elapsed time in seconds
        """
        tree = tree_class()
        
        # First insert all data
        for value in data:
            tree.insert(value)
        
        # Then measure search time
        start_time = time.perf_counter()
        for key in search_keys:
            tree.search(key)
        end_time = time.perf_counter()
        
        return end_time - start_time
    
    def benchmark_delete(self, tree_class, data, delete_keys, tree_name):
        """
        Benchmark delete operation.
        
        Input: tree_class - class to instantiate
               data - list of values to insert first
               delete_keys - list of keys to delete
               tree_name - string identifier for results
        Output: float - elapsed time in seconds
        """
        tree = tree_class()
        
        # First insert all data
        for value in data:
            tree.insert(value)
        
        # Then measure delete time
        start_time = time.perf_counter()
        for key in delete_keys:
            tree.delete(key)
        end_time = time.perf_counter()
        
        return end_time - start_time
    
    def benchmark_mixed_workload(self, tree_class, operations, tree_name):
        """
        Benchmark mixed workload (insert, search, delete).
        
        Input: tree_class - class to instantiate
               operations - list of (op_type, value) tuples
               tree_name - string identifier for results
        Output: float - elapsed time in seconds
        """
        tree = tree_class()
        
        start_time = time.perf_counter()
        for op_type, value in operations:
            if op_type == 'insert':
                tree.insert(value)
            elif op_type == 'search':
                tree.search(value)
            elif op_type == 'delete':
                tree.delete(value)
        end_time = time.perf_counter()
        
        return end_time - start_time
    
    def run_insert_benchmark_random(self, sizes):
        """
        Run insert benchmark with random data.
        
        Input: sizes - list of dataset sizes to test
        Output: None (stores results in self.results)
        """
        print("Running random insert benchmarks...")
        
        for size in sizes:
            print(f"  Size: {size:,}")
            data = self.generate_random_data(size)
            
            # AVL Tree
            time_avl = self.benchmark_insert(AVLTree, data, 'avl')
            self.results['avl']['insert'][f'random_{size}'] = time_avl
            print(f"    AVL: {time_avl:.4f}s")
            
            # Red-Black Tree
            time_rb = self.benchmark_insert(RedBlackTree, data, 'rb')
            self.results['rb']['insert'][f'random_{size}'] = time_rb
            print(f"    RB:  {time_rb:.4f}s")
            
            # Splay Tree
            time_splay = self.benchmark_insert(SplayTree, data, 'splay')
            self.results['splay']['insert'][f'random_{size}'] = time_splay
            print(f"    Splay: {time_splay:.4f}s")
    
    def run_insert_benchmark_sequential(self, sizes):
        """
        Run insert benchmark with sequential data.
        
        Input: sizes - list of dataset sizes to test
        Output: None (stores results in self.results)
        """
        print("Running sequential insert benchmarks...")
        
        for size in sizes:
            print(f"  Size: {size:,}")
            data = self.generate_sequential_data(size)
            
            # AVL Tree
            time_avl = self.benchmark_insert(AVLTree, data, 'avl')
            self.results['avl']['insert'][f'sequential_{size}'] = time_avl
            print(f"    AVL: {time_avl:.4f}s")
            
            # Red-Black Tree
            time_rb = self.benchmark_insert(RedBlackTree, data, 'rb')
            self.results['rb']['insert'][f'sequential_{size}'] = time_rb
            print(f"    RB:  {time_rb:.4f}s")
            
            # Splay Tree
            time_splay = self.benchmark_insert(SplayTree, data, 'splay')
            self.results['splay']['insert'][f'sequential_{size}'] = time_splay
            print(f"    Splay: {time_splay:.4f}s")
    
    # --- UPDATED METHOD ---
    def run_search_benchmark(self, sizes, pattern='random'):
        """
        Run search benchmark.
        
        Input: sizes - list of dataset sizes to test
               pattern - 'random', 'sequential', or 'skewed'
        Output: None (stores results in self.results)
        """
        print(f"Running {pattern} search benchmarks...")
        
        for size in sizes:
            print(f"  Size: {size:,}")
            
            # --- Data Generation ---
            # 1. Generate the base data to build the tree
            if pattern == 'sequential':
                data = self.generate_sequential_data(size)
            else:
                # For both 'random' and 'skewed', we build from random data
                data = self.generate_random_data(size)

            # 2. Generate the search keys based on the pattern
            num_searches = min(size // 10, 10000)
            
            if pattern == 'random':
                search_keys = random.sample(data, num_searches)
            elif pattern == 'sequential':
                # Note: data is sequential, but we still pick random keys to search
                search_keys = random.sample(data, num_searches)
            elif pattern == 'skewed':
                # This is the new part
                search_keys = self.generate_skewed_search_keys(data, num_searches)
            else:
                print(f"Warning: Unknown pattern '{pattern}'. Defaulting to 'random'.")
                search_keys = random.sample(data, num_searches)
            # --- End Data Generation ---

            # AVL Tree
            time_avl = self.benchmark_search(AVLTree, data, search_keys, 'avl')
            self.results['avl']['search'][f'{pattern}_{size}'] = time_avl
            print(f"    AVL: {time_avl:.4f}s")
            
            # Red-Black Tree
            time_rb = self.benchmark_search(RedBlackTree, data, search_keys, 'rb')
            self.results['rb']['search'][f'{pattern}_{size}'] = time_rb
            print(f"    RB:  {time_rb:.4f}s")
            
            # Splay Tree
            time_splay = self.benchmark_search(SplayTree, data, search_keys, 'splay')
            self.results['splay']['search'][f'{pattern}_{size}'] = time_splay
            print(f"    Splay: {time_splay:.4f}s")
    # --- END UPDATED METHOD ---

    def run_delete_benchmark(self, sizes, pattern='random'):
        """
        Run delete benchmark.
        
        Input: sizes - list of dataset sizes to test
               pattern - 'random' or 'sequential'
        Output: None (stores results in self.results)
        """
        print(f"Running {pattern} delete benchmarks...")
        
        for size in sizes:
            print(f"  Size: {size:,}")
            
            if pattern == 'random':
                data = self.generate_random_data(size)
                delete_keys = random.sample(data, min(size // 10, 10000))
            else:
                data = self.generate_sequential_data(size)
                delete_keys = random.sample(data, min(size // 10, 10000))
            
            # AVL Tree
            time_avl = self.benchmark_delete(AVLTree, data, delete_keys, 'avl')
            self.results['avl']['delete'][f'{pattern}_{size}'] = time_avl
            print(f"    AVL: {time_avl:.4f}s")
            
            # Red-Black Tree
            time_rb = self.benchmark_delete(RedBlackTree, data, delete_keys, 'rb')
            self.results['rb']['delete'][f'{pattern}_{size}'] = time_rb
            print(f"    RB:  {time_rb:.4f}s")
            
            # Splay Tree
            time_splay = self.benchmark_delete(SplayTree, data, delete_keys, 'splay')
            self.results['splay']['delete'][f'{pattern}_{size}'] = time_splay
            print(f"    Splay: {time_splay:.4f}s")
    
    def run_mixed_workload_benchmark(self, sizes):
        """
        Run mixed workload benchmark (60% insert, 30% search, 10% delete).
        
        Input: sizes - list of dataset sizes to test
        Output: None (stores results in self.results)
        """
        print("Running mixed workload benchmarks...")
        
        for size in sizes:
            print(f"  Size: {size:,}")
            
            # Generate mixed operations
            operations = []
            values = self.generate_random_data(size)
            
            for i in range(size):
                rand = random.random()
                if rand < 0.6:  # 60% insert
                    operations.append(('insert', values[i]))
                elif rand < 0.9:  # 30% search
                    if i > 0:
                        operations.append(('search', random.choice(values[:i])))
                else:  # 10% delete
                    if i > 0:
                        operations.append(('delete', random.choice(values[:i])))
            
            # AVL Tree
            time_avl = self.benchmark_mixed_workload(AVLTree, operations, 'avl')
            self.results['avl']['mixed'][f'mixed_{size}'] = time_avl
            print(f"    AVL: {time_avl:.4f}s")
            
            # Red-Black Tree
            time_rb = self.benchmark_mixed_workload(RedBlackTree, operations, 'rb')
            self.results['rb']['mixed'][f'mixed_{size}'] = time_rb
            print(f"    RB:  {time_rb:.4f}s")
            
            # Splay Tree
            time_splay = self.benchmark_mixed_workload(SplayTree, operations, 'splay')
            self.results['splay']['mixed'][f'mixed_{size}'] = time_splay
            print(f"    Splay: {time_splay:.4f}s")
    
    def save_results(self, filename='benchmark_results.json'):
        """
        Save benchmark results to JSON file.
        
        Input: filename - string path to output file
        Output: None (writes to file)
        """
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\nResults saved to {filename}")
    
    def plot_results(self, sizes, operation, pattern='random', output_dir='plots'):
        """
        Plot benchmark results.
        
        Input: sizes - list of dataset sizes
               operation - 'insert', 'search', or 'delete'
               pattern - 'random', 'sequential', 'skewed', 'mixed'
               output_dir - directory to save plots
        Output: None (saves plot to file)
        """
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        avl_times = []
        rb_times = []
        splay_times = []
        
        for size in sizes:
            key = f'{pattern}_{size}'
            avl_times.append(self.results['avl'][operation].get(key, 0))
            rb_times.append(self.results['rb'][operation].get(key, 0))
            splay_times.append(self.results['splay'][operation].get(key, 0))
        
        plt.figure(figsize=(10, 6))
        plt.plot(sizes, avl_times, marker='o', label='AVL Tree', linewidth=2)
        plt.plot(sizes, rb_times, marker='s', label='Red-Black Tree', linewidth=2)
        plt.plot(sizes, splay_times, marker='^', label='Splay Tree', linewidth=2)
        
        plt.xlabel('Dataset Size', fontsize=12)
        plt.ylabel('Time (seconds)', fontsize=12)
        plt.title(f'{operation.capitalize()} Operation - {pattern.capitalize()} Data', fontsize=14)
        plt.legend(fontsize=11)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        output_path = os.path.join(output_dir, f'{operation}_{pattern}_benchmark.png')
        plt.savefig(output_path, dpi=300)
        plt.close()
        print(f"Plot saved: {output_path}")


def main():
    """
    Main function to run all benchmarks.
    """
    # Dataset sizes to test
    sizes = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]  

    # Create output directory for plots
    output_dir = 'plots'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}/")

    if len(sys.argv) > 1:
        base_filename = f'results/{sys.argv[1]}'
        print(f"Using base filename from argument: '{base_filename}'")
    else:
        base_filename = 'results/benchmark_results.json' # Default filename
        print(f"  No filename argument provided. Defaulting to: {base_filename}")
    
    tests_to_run = [
        # ('insert', 'random'),
        # ('insert', 'sequential'),
        # ('search', 'random'),
        # ('search', 'sequential'),
        ('search', 'skewed'),
        # ('delete', 'random'),
        # ('delete', 'sequential'),
        # ('mixed', 'mixed'),
    ]

    benchmark = Benchmark()
    
    print("--- Starting Benchmarks ---")
    
    for op, pat in tests_to_run:
        if op == 'insert':
            if pat == 'random':
                benchmark.run_insert_benchmark_random(sizes)
            elif pat == 'sequential':
                benchmark.run_insert_benchmark_sequential(sizes)
        elif op == 'search':
            benchmark.run_search_benchmark(sizes, pat)
        elif op == 'delete':
            benchmark.run_delete_benchmark(sizes, pat)
        elif op == 'mixed':
            benchmark.run_mixed_workload_benchmark(sizes)
        else:
            print(f"Warning: Unknown operation '{op}'. Skipping.")
        benchmark.plot_results(operation=op, pattern=pat, output_dir=output_dir)
            
    print("\n--- All Benchmarks Complete ---")
    benchmark.save_results(filename=base_filename)
    print(f"\nAll plots saved to '{output_dir}/' directory")
    
    

if __name__ == '__main__':
    main()