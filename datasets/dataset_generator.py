"""
Dataset generator for benchmarking.
Generates test datasets and saves them for reproducibility.
"""

import random
import json
import pickle
import os


def generate_datasets(output_dir='datasets'):
    """
    Generate all test datasets used in benchmarking.
    
    Input: output_dir - directory to save datasets
    Output: None (saves files to disk)
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    sizes = [10000, 50000, 100000, 500000, 1000000, 5000000, 10000000]
    
    datasets = {}
    
    print("Generating datasets...")
    
    for size in sizes:
        print(f"Generating dataset of size {size:,}...")
        
        # Random data
        random_data = random.sample(range(size * 10), size)
        datasets[f'random_{size}'] = random_data
        
        # Sequential data
        sequential_data = list(range(size))
        datasets[f'sequential_{size}'] = sequential_data
        
        # Save individual files for large datasets
        with open(f'{output_dir}/random_{size}.json', 'w') as f:
            json.dump(random_data, f)
        
        with open(f'{output_dir}/sequential_{size}.json', 'w') as f:
            json.dump(sequential_data, f)
    
    # Save metadata
    metadata = {
        'sizes': sizes,
        'description': 'Test datasets for AVL, Red-Black, and Splay tree benchmarking',
        'random_range': 'Random samples from [0, size*10)',
        'sequential_range': 'Sequential integers from 0 to size-1'
    }
    
    with open(f'{output_dir}/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=2)
    
    print(f"\nDatasets saved to '{output_dir}/' directory")
    print("Upload these files to cloud storage (Google Drive, Dropbox, etc.)")
    print("Then update the README with the link")


def load_dataset(filename):
    """
    Load a dataset from file.
    
    Input: filename - path to dataset file
    Output: list of integers
    """
    with open(filename, 'r') as f:
        return json.load(f)


def generate_sample_dataset(output_file='sample_dataset.txt'):
    """
    Generate a small sample dataset for demonstration.
    
    Input: output_file - path to output file
    Output: None (saves to file)
    """
    size = 1000
    data = random.sample(range(size * 10), size)
    
    with open(output_file, 'w') as f:
        f.write(f"Sample dataset with {size} elements\n")
        f.write("=" * 50 + "\n\n")
        f.write("First 20 elements:\n")
        f.write(str(data[:20]) + "\n\n")
        f.write("Statistics:\n")
        f.write(f"  Min: {min(data)}\n")
        f.write(f"  Max: {max(data)}\n")
        f.write(f"  Mean: {sum(data) / len(data):.2f}\n")
    
    print(f"Sample dataset saved to '{output_file}'")


if __name__ == '__main__':
    print("=" * 60)
    print("Dataset Generator for COSC 520 Assignment 2")
    print("=" * 60)
    print()
    
    # Generate all datasets
    generate_datasets()
    
    # Generate sample for quick inspection
    generate_sample_dataset()
    
    print("\nDone!")
