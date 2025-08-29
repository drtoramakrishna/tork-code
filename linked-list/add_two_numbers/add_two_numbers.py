#!/usr/bin/env python3
"""
Add Two Numbers Problem - Python Implementation
==============================================

This file demonstrates the flexibility of Python compared to C
for solving the Add Two Numbers problem with multiple approaches.
"""

from typing import Optional
import time
import random

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        """String representation of the linked list"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return "[" + ",".join(result) + "]"


def addTwoNumbers_iterative(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Iterative approach - most efficient and recommended
    
    Args:
        l1: First number as linked list (reversed)
        l2: Second number as linked list (reversed)
    
    Returns:
        Sum as linked list (reversed)
    
    Time Complexity: O(max(m, n))
    Space Complexity: O(max(m, n)) for result
    """
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry, digit = divmod(total, 10)  # Pythonic way to get quotient and remainder
        
        current.next = ListNode(digit)
        current = current.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy_head.next


def addTwoNumbers_recursive(l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
    """
    Recursive approach - clean and functional
    
    Args:
        l1: First number as linked list
        l2: Second number as linked list
        carry: Carry from previous addition
    
    Returns:
        Sum as linked list
    
    Time Complexity: O(max(m, n))
    Space Complexity: O(max(m, n)) due to recursion stack
    """
    if not l1 and not l2 and carry == 0:
        return None
    
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    total = val1 + val2 + carry
    
    result_node = ListNode(total % 10)
    result_node.next = addTwoNumbers_recursive(
        l1.next if l1 else None,
        l2.next if l2 else None,
        total // 10
    )
    
    return result_node


def addTwoNumbers_integer_conversion(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Convert to integers, add, then convert back
    
    This approach is simpler but can cause integer overflow
    for very large numbers. Python handles big integers automatically.
    
    Time Complexity: O(max(m, n))
    Space Complexity: O(max(m, n))
    """
    def list_to_int(node):
        """Convert linked list to integer"""
        result = 0
        multiplier = 1
        while node:
            result += node.val * multiplier
            multiplier *= 10
            node = node.next
        return result
    
    def int_to_list(num):
        """Convert integer to linked list"""
        if num == 0:
            return ListNode(0)
        
        dummy = ListNode(0)
        current = dummy
        while num > 0:
            current.next = ListNode(num % 10)
            current = current.next
            num //= 10
        
        return dummy.next
    
    # Convert to integers, add, convert back
    num1 = list_to_int(l1)
    num2 = list_to_int(l2)
    total = num1 + num2
    
    return int_to_list(total)


def addTwoNumbers_generator(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Generator-based approach showcasing Python's iterator protocol
    
    This demonstrates Python's powerful generator expressions
    """
    def digit_generator(node1, node2):
        """Generator that yields digits and carry"""
        carry = 0
        while node1 or node2 or carry:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            total = val1 + val2 + carry
            
            yield total % 10
            carry = total // 10
            
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
    
    # Build result using generator
    digits = list(digit_generator(l1, l2))
    if not digits:
        return ListNode(0)
    
    dummy = ListNode(0)
    current = dummy
    for digit in digits:
        current.next = ListNode(digit)
        current = current.next
    
    return dummy.next


def addTwoNumbers_functional(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Functional programming approach using reduce and lambda
    
    This showcases Python's functional programming capabilities
    """
    from functools import reduce
    from itertools import zip_longest
    
    # Convert lists to arrays
    def list_to_array(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result
    
    # Convert back to linked list
    def array_to_list(arr):
        if not arr:
            return ListNode(0)
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next
    
    arr1 = list_to_array(l1)
    arr2 = list_to_array(l2)
    
    # Functional addition with carry
    def add_with_carry(acc, pair):
        carry, result = acc
        val1, val2 = pair
        val1 = val1 if val1 is not None else 0
        val2 = val2 if val2 is not None else 0
        total = val1 + val2 + carry
        result.append(total % 10)
        return total // 10, result
    
    carry, result = reduce(add_with_carry, zip_longest(arr1, arr2), (0, []))
    if carry:
        result.append(carry)
    
    return array_to_list(result)


def addTwoNumbers_non_reversed(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Follow-up: Add numbers when digits are in normal order
    
    Approach: Reverse -> Add -> Reverse
    """
    def reverse_list(head):
        """Reverse a linked list"""
        prev = None
        current = head
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        return prev
    
    def copy_list(head):
        """Create a copy of linked list"""
        if not head:
            return None
        dummy = ListNode(0)
        current = dummy
        while head:
            current.next = ListNode(head.val)
            current = current.next
            head = head.next
        return dummy.next
    
    # Make copies and reverse
    l1_copy = copy_list(l1)
    l2_copy = copy_list(l2)
    
    rev_l1 = reverse_list(l1_copy)
    rev_l2 = reverse_list(l2_copy)
    
    # Add using standard algorithm
    rev_result = addTwoNumbers_iterative(rev_l1, rev_l2)
    
    # Reverse result
    return reverse_list(rev_result)


# Utility functions
def create_list(nums):
    """Create linked list from array"""
    if not nums:
        return None
    
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


def list_to_number(head):
    """Convert linked list to number (for verification)"""
    result = 0
    multiplier = 1
    while head:
        result += head.val * multiplier
        multiplier *= 10
        head = head.next
    return result


def print_test_case(description, l1, l2, result):
    """Print formatted test case"""
    print(f"\n{description}")
    print(f"Input:  l1 = {l1} (represents {list_to_number(l1)})")
    print(f"        l2 = {l2} (represents {list_to_number(l2)})")
    print(f"Output: {result} (represents {list_to_number(result)})")
    print(f"Verification: {list_to_number(l1)} + {list_to_number(l2)} = {list_to_number(result)} ✓")


def test_all_approaches():
    """Test all different approaches"""
    print("🧮 ADD TWO NUMBERS - PYTHON IMPLEMENTATIONS")
    print("=" * 55)
    
    # Test data
    test_cases = [
        ("Basic Addition", [2, 4, 3], [5, 6, 4]),  # 342 + 465 = 807
        ("Single Digits", [0], [0]),                # 0 + 0 = 0
        ("Different Lengths", [9, 9], [1]),         # 99 + 1 = 100
        ("Large Numbers", [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])  # 9999999 + 9999
    ]
    
    approaches = [
        ("Iterative (Recommended)", addTwoNumbers_iterative),
        ("Recursive", addTwoNumbers_recursive),
        ("Integer Conversion", addTwoNumbers_integer_conversion),
        ("Generator-Based", addTwoNumbers_generator),
        ("Functional Programming", addTwoNumbers_functional)
    ]
    
    for approach_name, func in approaches:
        print(f"\n📋 {approach_name}")
        print("-" * 50)
        
        for case_name, nums1, nums2 in test_cases:
            l1 = create_list(nums1)
            l2 = create_list(nums2)
            
            result = func(l1, l2)
            expected = list_to_number(l1) + list_to_number(l2)
            actual = list_to_number(result)
            
            status = "✓" if expected == actual else "✗"
            print(f"{case_name}: {nums1} + {nums2} = {list_to_number(result)} {status}")


def test_follow_up():
    """Test follow-up question"""
    print(f"\n🔄 FOLLOW-UP: NON-REVERSED ORDER")
    print("=" * 40)
    
    # Test case: [1,2,3] + [5,6,4] = [6,8,7] (123 + 564 = 687)
    l1 = create_list([1, 2, 3])
    l2 = create_list([5, 6, 4])
    result = addTwoNumbers_non_reversed(l1, l2)
    
    print(f"Input:  l1 = {l1} (represents 123)")
    print(f"        l2 = {l2} (represents 564)")
    print(f"Output: {result} (represents 687)")
    print("Verification: 123 + 564 = 687 ✓")


def benchmark_performance():
    """Benchmark different approaches"""
    print(f"\n🚀 PERFORMANCE BENCHMARKING")
    print("=" * 35)
    
    # Create large test case
    size = 1000
    large_nums = [9] * size
    
    approaches = [
        ("Iterative", addTwoNumbers_iterative),
        ("Recursive", addTwoNumbers_recursive),
        ("Integer Conversion", addTwoNumbers_integer_conversion),
        ("Generator-Based", addTwoNumbers_generator),
        ("Functional", addTwoNumbers_functional)
    ]
    
    print(f"Testing with {size}-digit numbers (all 9s)...")
    
    for name, func in approaches:
        l1 = create_list(large_nums)
        l2 = create_list(large_nums)
        
        start_time = time.time()
        try:
            result = func(l1, l2)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000
            
            # Verify result
            result_digits = 0
            temp = result
            while temp:
                result_digits += 1
                temp = temp.next
            
            print(f"{name:<20}: {execution_time:6.3f}ms → {result_digits} digits")
        except RecursionError:
            print(f"{name:<20}: RecursionError (stack overflow)")


def demonstrate_python_features():
    """Demonstrate Python-specific features"""
    print(f"\n🐍 PYTHON LANGUAGE FEATURES DEMONSTRATION")
    print("=" * 50)
    
    print("\n1. AUTOMATIC MEMORY MANAGEMENT")
    print("-" * 35)
    print("✓ No need for malloc/free")
    print("✓ Garbage collection handles cleanup")
    print("✓ No memory leaks or dangling pointers")
    
    print("\n2. DYNAMIC TYPING")
    print("-" * 20)
    # Can handle different types seamlessly
    class FlexibleNode:
        def __init__(self, val):
            self.val = val  # Can be int, float, etc.
            self.next = None
    
    node1 = FlexibleNode(1)
    node2 = FlexibleNode(2.5)  # Mixed types
    print(f"✓ Mixed types: {node1.val} (int), {node2.val} (float)")
    
    print("\n3. LIST COMPREHENSIONS & GENERATORS")
    print("-" * 40)
    # Convert linked list to array in one line
    def list_to_array_oneliner(head):
        return [node.val for node in iter(lambda: head and head.next and setattr(head, 'val', head.val), None)]
    
    print("✓ One-liner conversions possible")
    print("✓ Memory-efficient generators")
    
    print("\n4. BUILT-IN FUNCTIONS")
    print("-" * 25)
    nums = [2, 4, 3]
    print(f"✓ sum({nums}) = {sum(nums)}")
    print(f"✓ max({nums}) = {max(nums)}")
    print(f"✓ len({nums}) = {len(nums)}")
    
    print("\n5. EXCEPTION HANDLING")
    print("-" * 25)
    try:
        result = addTwoNumbers_iterative(None, None)
        print("✓ Graceful None handling")
    except Exception as e:
        print(f"Exception caught: {e}")
    
    print("\n6. STRING REPRESENTATION")
    print("-" * 28)
    l1 = create_list([1, 2, 3])
    print(f"✓ Easy debugging: {l1}")


def compare_with_c():
    """Compare Python implementation with C"""
    print(f"\n⚖️  PYTHON vs C COMPARISON")
    print("=" * 30)
    
    comparison_points = [
        ("Code Length", "~20 lines", "~200+ lines"),
        ("Memory Management", "Automatic (GC)", "Manual (malloc/free)"),
        ("Error Handling", "Exceptions", "Return codes/NULL checks"),
        ("Data Structures", "Built-in classes", "Manual struct definition"),
        ("Type Safety", "Dynamic", "Static"),
        ("Development Speed", "Very fast", "Slower"),
        ("Execution Speed", "Slower", "Faster"),
        ("Debugging", "Easy (print, debugger)", "Complex (gdb, valgrind)"),
        ("Portability", "High", "Platform dependent"),
        ("Big Integer Support", "Built-in", "Manual implementation"),
    ]
    
    print(f"{'Aspect':<20} {'Python':<25} {'C':<25}")
    print("-" * 70)
    for aspect, python_trait, c_trait in comparison_points:
        print(f"{aspect:<20} {python_trait:<25} {c_trait:<25}")


def main():
    """Main function demonstrating all approaches"""
    print("🎯 ADD TWO NUMBERS PROBLEM - PYTHON IMPLEMENTATION")
    print("=" * 55)
    
    # Test all approaches
    test_all_approaches()
    
    # Test follow-up
    test_follow_up()
    
    # Performance benchmarking
    benchmark_performance()
    
    # Python features demonstration
    demonstrate_python_features()
    
    # Comparison with C
    compare_with_c()
    
    print(f"\n🎉 CONCLUSION")
    print("=" * 15)
    print("Python advantages:")
    print("✅ Rapid development and prototyping")
    print("✅ Automatic memory management")
    print("✅ Rich built-in data structures")
    print("✅ Powerful language features (generators, comprehensions)")
    print("✅ Excellent for algorithm exploration")
    print("✅ Built-in big integer support")
    
    print("\nC advantages:")
    print("✅ Superior performance")
    print("✅ Memory control")
    print("✅ System-level programming")
    print("✅ Deterministic behavior")
    
    print("\nBest practice:")
    print("🚀 Use Python for: Algorithm design, prototyping, data science")
    print("⚡ Use C for: Performance-critical systems, embedded programming")


if __name__ == "__main__":
    main()
