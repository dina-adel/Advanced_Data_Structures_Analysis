import sys
try:
    # This script assumes your benchmark file is saved as 'benchmark.py'
    from benchmark import Benchmark
except ImportError:
    print("Error: Could not find 'benchmark.py'.")
    print("Please make sure 'benchmark.py' is in the same folder as this demo.")
    sys.exit()
except Exception as e:
    print(f"An error occurred importing benchmark.py: {e}")
    print("This demo assumes your tree implementations (AVL, RB, Splay) are in a 'src/' folder.")
    sys.exit()

def print_menu():
    """Displays the main menu of benchmark choices."""
    print("\n--- 🌳 Tree Benchmark Demo ---")
    print("Please choose a benchmark to run:")
    print("  [1] Insert - Random Data")
    print("  [2] Insert - Sequential Data")
    print("  [3] Search - Random Data")
    print("  [4] Search - Sequential Data")
    print("  [5] Delete - Random Data")
    print("  [6] Delete - Sequential Data")
    print("  [7] Mixed Workload (Random): 60% insert, 30% search, 10% delete operations")
    print("  ------------------------------")
    print("  [q] Quit")
    print("---------------------------------")

def prompt_for_size():
    """
    Asks the user for a single integer size.
    Returns: A single integer.
    """
    while True:
        try:
            size_str = input("  ... Enter dataset size (e.g., 50000): ").strip()
            if not size_str:
                continue
                
            size_int = int(size_str)
            if size_int <= 0:
                print("      ❌ Size must be a positive number.")
            else:
                return size_int # Return the single integer
        except ValueError:
            print("      ❌ Invalid input. Please enter a whole number.")

def main():
    """
    Main demo loop that prompts the user to select
    a benchmark and a size, then shows the results.
    """
    print(f"NOTE: This demo will run your benchmarks and print")
    print(f"the timing results directly to the console.")
    print("--------------------------------------------------\n")
    
    # We create one Benchmark instance to run the tests
    # We will NOT use its plotting or saving methods.
    benchmark = Benchmark()
    
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'q':
            print("Goodbye!")
            break
        
        ran_test = False
        
        if choice == '1':
            size = prompt_for_size()
            print(f"\nRunning [Insert - Random] for size {size:,}...")
            # We pass [size] as a list, as the benchmark function expects a list
            benchmark.run_insert_benchmark_random([size])
            ran_test = True
        
        elif choice == '2':
            size = prompt_for_size()
            print(f"\nRunning [Insert - Sequential] for size {size:,}...")
            benchmark.run_insert_benchmark_sequential([size])
            ran_test = True

        elif choice == '3':
            size = prompt_for_size()
            print(f"\nRunning [Search - Random] for size {size:,}...")
            benchmark.run_search_benchmark([size], 'random')
            ran_test = True
        
        elif choice == '4':
            size = prompt_for_size()
            print(f"\nRunning [Search - Sequential] for size {size:,}...")
            benchmark.run_search_benchmark([size], 'sequential')
            ran_test = True
        
        elif choice == '5':
            size = prompt_for_size()
            print(f"\nRunning [Delete - Random] for size {size:,}...")
            benchmark.run_delete_benchmark([size], 'random')
            ran_test = True
        
        elif choice == '6':
            size = prompt_for_size()
            print(f"\nRunning [Delete - Sequential] for size {size:,}...")
            benchmark.run_delete_benchmark([size], 'sequential')
            ran_test = True
        
        elif choice == '7':
            size = prompt_for_size()
            print(f"\nRunning [Mixed Workload] for size {size:,}...")
            benchmark.run_mixed_workload_benchmark([size])
            ran_test = True
        
        else:
            print(f"❌ Invalid choice '{choice}'. Please try again.")
        
        if ran_test:
            print("\n✅ Benchmark complete. Results are shown above.")

if __name__ == '__main__':
    main()