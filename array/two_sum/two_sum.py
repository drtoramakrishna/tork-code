#!/usr/bin/env python3
"""
Two Sum Problem - Python Implementation
=======================================

This file demonstrates the flexibility of Python compared to C
for solving the Two Sum problem with multiple approaches.
"""

from typing import List, Dict
import time
import random

def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach - check every pair
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List containing indices of the two numbers that sum to target
        
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(nums)
    
    # Check every possible pair
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []  # No solution found


def two_sum_hash_table(nums: List[int], target: int) -> List[int]:
    """
    Hash table approach - optimal solution
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        List containing indices of the two numbers that sum to target
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen: Dict[int, int] = {}  # value -> index mapping
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[num] = i
    
    return []  # No solution found


def two_sum_two_pointers(nums: List[int], target: int) -> List[int]:
    """
    Two pointers approach (requires sorting, so original indices are lost)
    This approach returns the values, not indices, to demonstrate the concept.
    
    Args:
        nums: List of integers (will be sorted internally)
        target: Target sum to find
        
    Returns:
        List containing the two numbers that sum to target
        
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for the sorted array with indices
    """
    # Create list of (value, original_index) pairs
    indexed_nums = [(nums[i], i) for i in range(len(nums))]
    
    # Sort by value
    indexed_nums.sort(key=lambda x: x[0])
    
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            # Return original indices in sorted order
            indices = sorted([indexed_nums[left][1], indexed_nums[right][1]])
            return indices
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


def two_sum_pythonic(nums: List[int], target: int) -> List[int]:
    """
    Pythonic one-liner approach using generator expression
    
    This showcases Python's expressiveness but isn't optimal for performance.
    It's essentially a more concise version of brute force.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    return next(([i, j] for i in range(len(nums)) 
                       for j in range(i + 1, len(nums)) 
                       if nums[i] + nums[j] == target), [])


def benchmark_solutions():
    """
    Benchmark different solutions to compare performance
    """
    print("🚀 PERFORMANCE BENCHMARKING")
    print("=" * 50)
    
    # Generate test data
    test_sizes = [100, 500, 1000]
    
    for size in test_sizes:
        print(f"\n📊 Array size: {size}")
        print("-" * 30)
        
        # Generate random array
        nums = [random.randint(-1000, 1000) for _ in range(size)]
        
        # Ensure there's always a solution by adding two numbers that sum to target
        target = 42
        nums[0] = 20
        nums[1] = 22  # 20 + 22 = 42
        
        solutions = [
            ("Hash Table (Optimal)", two_sum_hash_table),
            ("Two Pointers", two_sum_two_pointers),
        ]
        
        # Only test brute force for smaller arrays (it's too slow for large ones)
        if size <= 500:
            solutions.append(("Brute Force", two_sum_brute_force))
            solutions.append(("Pythonic", two_sum_pythonic))
        
        for name, func in solutions:
            start_time = time.time()
            result = func(nums, target)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            print(f"{name:20}: {execution_time:6.3f}ms → {result}")


def demonstrate_python_flexibility():
    """
    Demonstrate Python's flexibility compared to C
    """
    print("🐍 PYTHON LANGUAGE FLEXIBILITY DEMONSTRATION")
    print("=" * 55)
    
    # Test data
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([-1, -2, -3, -4, -5], -8),
        ([0, 4, 3, 0], 0)
    ]
    
    print("\n1. BUILT-IN DATA STRUCTURES")
    print("-" * 35)
    for nums, target in test_cases[:3]:
        result = two_sum_hash_table(nums, target)
        print(f"Input: {nums}, Target: {target} → Output: {result}")
    
    print("\n2. LIST COMPREHENSIONS & GENERATORS")
    print("-" * 40)
    # Demonstrate finding all pairs that sum to target (not just first one)
    nums = [1, 2, 3, 4, 5, 6]
    target = 7
    all_pairs = [[i, j] for i in range(len(nums)) 
                       for j in range(i + 1, len(nums)) 
                       if nums[i] + nums[j] == target]
    print(f"All pairs in {nums} that sum to {target}: {all_pairs}")
    
    print("\n3. DYNAMIC TYPING & FLEXIBILITY")
    print("-" * 38)
    # Python can handle different number types seamlessly
    mixed_nums = [1, 2.5, 3, 4.5]  # Mixed int and float
    # Note: This would require careful handling in C
    print(f"Mixed types work seamlessly: {mixed_nums}")
    
    print("\n4. EXCEPTION HANDLING")
    print("-" * 25)
    try:
        result = two_sum_hash_table([], 5)  # Edge case
        print(f"Empty array handled gracefully: {result}")
    except Exception as e:
        print(f"Error handled: {e}")
    
    print("\n5. MULTIPLE RETURN TYPES")
    print("-" * 30)
    def two_sum_flexible(nums, target, return_values=False):
        """Flexible function that can return indices or values"""
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                if return_values:
                    return [complement, num]  # Return actual values
                else:
                    return [seen[complement], i]  # Return indices
            seen[num] = i
        return []
    
    nums = [2, 7, 11, 15]
    target = 9
    indices = two_sum_flexible(nums, target, return_values=False)
    values = two_sum_flexible(nums, target, return_values=True)
    print(f"Indices: {indices}, Values: {values}")


def compare_with_c():
    """
    Compare Python implementation with C characteristics
    """
    print("\n⚖️  PYTHON vs C COMPARISON")
    print("=" * 35)
    
    comparison_points = [
        ("Lines of Code", "Python: ~15 lines", "C: ~80+ lines"),
        ("Memory Management", "Automatic (GC)", "Manual (malloc/free)"),
        ("Hash Table", "Built-in dict", "Manual implementation"),
        ("Error Handling", "Try/except", "Manual checks"),
        ("Type Safety", "Dynamic typing", "Static typing"),
        ("Development Speed", "Very fast", "Slower"),
        ("Execution Speed", "Slower (interpreted)", "Faster (compiled)"),
        ("Portability", "High", "Platform dependent"),
    ]
    
    print(f"{'Aspect':<20} {'Python':<25} {'C':<25}")
    print("-" * 70)
    for aspect, python_trait, c_trait in comparison_points:
        print(f"{aspect:<20} {python_trait:<25} {c_trait:<25}")


def main():
    """
    Main function demonstrating all approaches
    """
    print("🎯 TWO SUM PROBLEM - PYTHON IMPLEMENTATION")
    print("=" * 50)
    
    # Test all approaches
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
    ]
    
    approaches = [
        ("Brute Force O(n²)", two_sum_brute_force),
        ("Hash Table O(n)", two_sum_hash_table),
        ("Two Pointers O(n log n)", two_sum_two_pointers),
        ("Pythonic O(n²)", two_sum_pythonic),
    ]
    
    for approach_name, func in approaches:
        print(f"\n📋 {approach_name}")
        print("-" * 40)
        
        for nums, target in test_cases:
            result = func(nums, target)
            print(f"Input: {nums}, Target: {target} → {result}")
    
    # Performance benchmarking
    print("\n")
    benchmark_solutions()
    
    # Flexibility demonstration
    print("\n")
    demonstrate_python_flexibility()
    
    # Comparison with C
    compare_with_c()
    
    print("\n🎉 CONCLUSION")
    print("=" * 15)
    print("Python offers:")
    print("✅ Rapid development")
    print("✅ Built-in data structures")
    print("✅ Automatic memory management")
    print("✅ Rich standard library")
    print("✅ Multiple programming paradigms")
    print("\nBest for: Prototyping, data analysis, web development")
    print("Best C for: System programming, performance-critical applications")


if __name__ == "__main__":
    main()
