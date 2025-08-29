#!/usr/bin/env python3
"""
LeetCode #3: Longest Substring Without Repeating Characters

Problem: Given a string s, find the length of the longest substring 
without repeating characters.

Multiple Python implementations showcasing different approaches,
from basic to advanced optimizations and Pythonic solutions.
"""

import time
from typing import Dict, List, Tuple, Set
from collections import defaultdict, deque
import itertools

# =============================================================================
# Approach 1: Brute Force - Check all substrings
# Time: O(n^3), Space: O(min(m,n))
# =============================================================================

def lengthOfLongestSubstring_bruteforce(s: str) -> int:
    """
    Brute Force: Check all possible substrings for uniqueness.
    Most intuitive but least efficient approach.
    """
    def all_unique(substring: str) -> bool:
        return len(set(substring)) == len(substring)
    
    n = len(s)
    max_length = 0
    
    # Check all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all_unique(s[i:j]):
                max_length = max(max_length, j - i)
    
    return max_length

# =============================================================================
# Approach 2: Sliding Window with Set
# Time: O(2n) = O(n), Space: O(min(m,n))
# =============================================================================

def lengthOfLongestSubstring_sliding_window(s: str) -> int:
    """
    Sliding Window: Use two pointers and a set to track unique characters.
    Expand right pointer, contract left when duplicates found.
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window from left until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character and update max length
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# =============================================================================
# Approach 3: Optimized Sliding Window with Dictionary
# Time: O(n), Space: O(min(m,n))
# =============================================================================

def lengthOfLongestSubstring_optimized(s: str) -> int:
    """
    Optimized Sliding Window: Use dictionary to store character indices.
    Jump left pointer directly instead of incrementing one by one.
    """
    char_index = {}  # Character -> last seen index
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If character seen and within current window, jump left pointer
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        # Update character index and max length
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

# =============================================================================
# Approach 4: Pythonic with dict.get()
# Time: O(n), Space: O(min(m,n))
# =============================================================================

def lengthOfLongestSubstring_pythonic(s: str) -> int:
    """
    Pythonic approach using dict.get() for cleaner code.
    """
    seen = {}
    left = max_length = 0
    
    for right, char in enumerate(s):
        # Use dict.get() with default -1 for unseen characters
        left = max(left, seen.get(char, -1) + 1)
        seen[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

# =============================================================================
# Approach 5: Using Deque (Educational)
# Time: O(n^2), Space: O(n)
# =============================================================================

def lengthOfLongestSubstring_deque(s: str) -> int:
    """
    Using deque to maintain current window of unique characters.
    Educational approach showing different data structure usage.
    """
    if not s:
        return 0
    
    max_length = 0
    window = deque()
    
    for char in s:
        # Remove characters from left until no duplicate
        while char in window:
            window.popleft()
        
        window.append(char)
        max_length = max(max_length, len(window))
    
    return max_length

# =============================================================================
# Approach 6: Functional Programming Style
# Time: O(n^2), Space: O(n)
# =============================================================================

def lengthOfLongestSubstring_functional(s: str) -> int:
    """
    Functional programming approach using generator expressions.
    Less efficient but demonstrates different programming paradigm.
    """
    if not s:
        return 0
    
    def expand_from_position(start: int) -> int:
        """Expand substring starting from given position."""
        seen = set()
        for i in range(start, len(s)):
            if s[i] in seen:
                break
            seen.add(s[i])
        return len(seen)
    
    return max(expand_from_position(i) for i in range(len(s)))

# =============================================================================
# Approach 7: Using List Comprehension (Advanced Python)
# Time: O(n^2), Space: O(n)
# =============================================================================

def lengthOfLongestSubstring_list_comprehension(s: str) -> int:
    """
    Advanced Python using list comprehension and itertools.
    Demonstrates Python's powerful built-in functions.
    """
    if not s:
        return 0
    
    # Generate all possible starting positions
    def unique_length_from(start: int) -> int:
        chars = []
        for char in s[start:]:
            if char in chars:
                break
            chars.append(char)
        return len(chars)
    
    return max([unique_length_from(i) for i in range(len(s))])

# =============================================================================
# Approach 8: Generator-based (Memory Efficient)
# Time: O(n^2), Space: O(k) where k is max unique chars
# =============================================================================

def lengthOfLongestSubstring_generator(s: str) -> int:
    """
    Generator-based approach for memory efficiency.
    Useful for very long strings where memory is a concern.
    """
    def generate_substrings():
        """Generator that yields lengths of unique substrings."""
        for i in range(len(s)):
            seen = set()
            length = 0
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                length += 1
            yield length
    
    return max(generate_substrings()) if s else 0

# =============================================================================
# Approach 9: Recursive with Memoization
# Time: O(n^2), Space: O(n^2) for memoization
# =============================================================================

def lengthOfLongestSubstring_recursive_memo(s: str) -> int:
    """
    Recursive approach with memoization for educational purposes.
    Shows how to apply recursion to sliding window problems.
    """
    memo = {}
    
    def helper(start: int, seen: frozenset) -> int:
        if start >= len(s):
            return 0
        
        # Memoization key
        key = (start, seen)
        if key in memo:
            return memo[key]
        
        current_char = s[start]
        
        if current_char in seen:
            # Character already seen, can't extend current substring
            result = helper(start + 1, frozenset())
        else:
            # Two choices: include current char or start new substring
            include = 1 + helper(start + 1, seen | {current_char})
            exclude = helper(start + 1, frozenset())
            result = max(include, exclude)
        
        memo[key] = result
        return result
    
    return helper(0, frozenset()) if s else 0

# =============================================================================
# Helper Functions for Testing and Analysis
# =============================================================================

def find_longest_substring_details(s: str) -> Tuple[int, str, int, int]:
    """
    Return length, actual substring, start index, and end index.
    """
    if not s:
        return 0, "", 0, 0
    
    char_index = {}
    left = 0
    max_length = 0
    best_left = 0
    best_right = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        
        if right - left + 1 > max_length:
            max_length = right - left + 1
            best_left = left
            best_right = right
    
    substring = s[best_left:best_right + 1]
    return max_length, substring, best_left, best_right

def analyze_string_patterns(s: str) -> Dict[str, any]:
    """
    Analyze string to provide insights about character distribution.
    """
    if not s:
        return {"empty": True}
    
    char_count = defaultdict(int)
    for char in s:
        char_count[char] += 1
    
    return {
        "length": len(s),
        "unique_chars": len(char_count),
        "max_char_frequency": max(char_count.values()),
        "most_frequent_char": max(char_count.items(), key=lambda x: x[1]),
        "has_repeats": any(count > 1 for count in char_count.values()),
        "all_unique": len(char_count) == len(s)
    }

# =============================================================================
# Testing Framework
# =============================================================================

def test_all_approaches():
    """Comprehensive testing of all approaches."""
    print("=== Python Implementation: Longest Substring Without Repeating Characters ===\n")
    
    # Test cases from problem statement and edge cases
    test_cases = [
        "abcabcbb",    # Expected: 3 ("abc")
        "bbbbb",       # Expected: 1 ("b") 
        "pwwkew",      # Expected: 3 ("wke")
        "",            # Expected: 0
        "au",          # Expected: 2 ("au")
        "dvdf",        # Expected: 3 ("vdf")
        "abcdef",      # Expected: 6 ("abcdef")
        "aab",         # Expected: 2 ("ab")
        "tmmzuxt",     # Expected: 5 ("mzuxt")
        "abba",        # Expected: 2 ("ab" or "ba")
        "nfpdmpi",     # Expected: 5 ("nfpdm")
        "ggububgvfk",  # Expected: 6 ("gubvfk")
        "a",           # Single character
        "ab",          # Two different
        "aa",          # Two same
        " ",           # Space
        "!@#$%^&*()",  # Special characters
        "12321",       # Numbers
        "abcdefghijklmnopqrstuvwxyz"  # All alphabet
    ]
    
    # All approaches to test
    approaches = [
        ("Brute Force", lengthOfLongestSubstring_bruteforce),
        ("Sliding Window", lengthOfLongestSubstring_sliding_window),
        ("Optimized", lengthOfLongestSubstring_optimized),
        ("Pythonic", lengthOfLongestSubstring_pythonic),
        ("Deque", lengthOfLongestSubstring_deque),
        ("Functional", lengthOfLongestSubstring_functional),
        ("List Comprehension", lengthOfLongestSubstring_list_comprehension),
        ("Generator", lengthOfLongestSubstring_generator)
    ]
    
    print("Testing All Approaches:")
    print("======================\n")
    
    for i, test_string in enumerate(test_cases):
        print(f"Test {i + 1}: Input = \"{test_string}\"")
        
        # Get detailed analysis
        length, substring, start, end = find_longest_substring_details(test_string)
        analysis = analyze_string_patterns(test_string)
        
        print(f"  Expected result: Length = {length}, Substring = \"{substring}\" (indices {start}-{end})")
        
        # Test all approaches
        results = []
        for name, func in approaches:
            try:
                start_time = time.time()
                result = func(test_string)
                end_time = time.time()
                
                results.append(result)
                execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                print(f"  {name:18}: {result:2d} ({execution_time:.4f}ms)")
            except Exception as e:
                print(f"  {name:18}: ERROR - {e}")
                results.append(None)
        
        # Check consistency
        valid_results = [r for r in results if r is not None]
        if len(set(valid_results)) <= 1:
            print("  ✓ All approaches consistent")
        else:
            print("  ✗ Inconsistent results!")
        
        # String analysis
        if analysis.get("length", 0) > 0:
            print(f"  String analysis: {analysis['unique_chars']} unique chars, "
                  f"max frequency: {analysis['max_char_frequency']}")
        
        print()

def benchmark_performance():
    """Performance benchmarking with different string sizes."""
    print("Performance Benchmarking:")
    print("========================\n")
    
    # Create test strings of different sizes
    test_strings = {
        "Short (10 chars)": "abcdefghij",
        "Medium (100 chars)": "".join(chr(ord('a') + i % 26) for i in range(100)),
        "Long (1000 chars)": "".join(chr(ord('a') + i % 26) for i in range(1000)),
        "Worst case (1000 'a')": "a" * 1000
    }
    
    # Fast approaches for large strings
    fast_approaches = [
        ("Sliding Window", lengthOfLongestSubstring_sliding_window),
        ("Optimized", lengthOfLongestSubstring_optimized),
        ("Pythonic", lengthOfLongestSubstring_pythonic),
        ("Deque", lengthOfLongestSubstring_deque)
    ]
    
    for description, test_string in test_strings.items():
        print(f"{description}:")
        print("-" * len(description))
        
        for name, func in fast_approaches:
            start_time = time.time()
            
            # Run multiple iterations for better measurement
            iterations = 1000 if len(test_string) <= 100 else 100
            for _ in range(iterations):
                result = func(test_string)
            
            end_time = time.time()
            avg_time = (end_time - start_time) / iterations * 1000
            
            print(f"  {name:15}: Result={result:3d}, Avg Time={avg_time:.6f}ms")
        
        print()

def demonstrate_edge_cases():
    """Demonstrate handling of various edge cases."""
    print("Edge Case Analysis:")
    print("==================\n")
    
    edge_cases = [
        ("Empty string", ""),
        ("Single char", "a"),
        ("All same", "aaaaa"),
        ("All different", "abcde"),
        ("Palindrome", "racecar"),
        ("With spaces", "a b c d"),
        ("Unicode", "αβγδε"),
        ("Numbers", "123456789"),
        ("Special chars", "!@#$%^&*()"),
        ("Mixed", "Hello World! 123")
    ]
    
    for description, test_case in edge_cases:
        length, substring, _, _ = find_longest_substring_details(test_case)
        analysis = analyze_string_patterns(test_case)
        
        print(f"{description:15}: \"{test_case}\"")
        print(f"  Result: Length={length}, Substring=\"{substring}\"")
        
        if analysis.get("length", 0) > 0:
            print(f"  Analysis: {analysis['unique_chars']} unique chars, "
                  f"{'all unique' if analysis['all_unique'] else 'has repeats'}")
        
        print()

# =============================================================================
# Main Execution
# =============================================================================

if __name__ == "__main__":
    test_all_approaches()
    benchmark_performance()
    demonstrate_edge_cases()
    
    print("Algorithm Complexity Summary:")
    print("============================")
    print("1. Brute Force:         O(n³) time, O(min(m,n)) space")
    print("2. Sliding Window:      O(n) time, O(min(m,n)) space") 
    print("3. Optimized:           O(n) time, O(min(m,n)) space")
    print("4. Pythonic:            O(n) time, O(min(m,n)) space")
    print("5. Deque:               O(n²) time, O(n) space")
    print("6. Functional:          O(n²) time, O(n) space")
    print("7. List Comprehension:  O(n²) time, O(n) space")
    print("8. Generator:           O(n²) time, O(k) space")
    print("9. Recursive + Memo:    O(n²) time, O(n²) space")
    print("\nRecommended: Optimized or Pythonic for best performance")
    print("Educational: Other approaches show different programming paradigms")
