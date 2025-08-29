# Two Sum Problem - Complete Solution Guide

## Problem Statement

**Category:** Algorithms  
**Difficulty:** Easy (56.20%)  
**Tags:** Array, Hash Table  

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Examples

**Example 1:**
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

### Follow-up
Can you come up with an algorithm that is less than O(n²) time complexity?

---

## C Language Solutions

### Solution 1: Brute Force Approach (O(n²))

This is the most straightforward approach that checks every pair of elements.

```c
#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 * 
 * Brute Force Approach:
 * - Check every possible pair of elements
 * - Return indices when target sum is found
 * 
 * Time Complexity: O(n²) - nested loops
 * Space Complexity: O(1) - only using constant extra space
 */
int* twoSum_BruteForce(int* nums, int numsSize, int target, int* returnSize) {
    // Allocate memory for result array (2 integers)
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;  // We always return 2 indices
    
    // Outer loop: iterate through each element
    for (int i = 0; i < numsSize - 1; i++) {
        // Inner loop: check remaining elements
        for (int j = i + 1; j < numsSize; j++) {
            // Check if current pair sums to target
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }
    
    // This should never be reached given problem constraints
    return result;
}

// Test function for brute force approach
void test_bruteforce() {
    printf("=== Brute Force Approach ===\n");
    
    // Test case 1
    int nums1[] = {2, 7, 11, 15};
    int target1 = 9;
    int returnSize1;
    int* result1 = twoSum_BruteForce(nums1, 4, target1, &returnSize1);
    printf("Input: [2,7,11,15], target: 9\n");
    printf("Output: [%d,%d]\n\n", result1[0], result1[1]);
    free(result1);
    
    // Test case 2
    int nums2[] = {3, 2, 4};
    int target2 = 6;
    int returnSize2;
    int* result2 = twoSum_BruteForce(nums2, 3, target2, &returnSize2);
    printf("Input: [3,2,4], target: 6\n");
    printf("Output: [%d,%d]\n\n", result2[0], result2[1]);
    free(result2);
}
```

**Key Learning Points:**
- Always allocate memory for return arrays using `malloc()`
- Remember to set `*returnSize` to indicate how many elements are returned
- Use nested loops carefully - inner loop starts from `i+1` to avoid using same element twice
- This approach is intuitive but inefficient for large arrays

---

### Solution 2: Optimized Hash Table Approach (O(n))

This approach uses a hash table concept implemented with sorting and binary search.

```c
#include <stdio.h>
#include <stdlib.h>

// Structure to store value and original index
typedef struct {
    int value;
    int index;
} ValueIndex;

// Comparison function for qsort
int compare(const void* a, const void* b) {
    ValueIndex* va = (ValueIndex*)a;
    ValueIndex* vb = (ValueIndex*)b;
    return va->value - vb->value;
}

// Binary search to find complement
int binarySearch(ValueIndex* arr, int left, int right, int target, int excludeIndex) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid].value == target && arr[mid].index != excludeIndex) {
            return arr[mid].index;
        }
        
        if (arr[mid].value < target || 
            (arr[mid].value == target && arr[mid].index == excludeIndex)) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

/**
 * Optimized Approach using Sorting + Binary Search:
 * - Create array of (value, original_index) pairs
 * - Sort by value
 * - For each element, binary search for its complement
 * 
 * Time Complexity: O(n log n) - sorting dominates
 * Space Complexity: O(n) - for the ValueIndex array
 */
int* twoSum_Optimized(int* nums, int numsSize, int target, int* returnSize) {
    // Create array to store value-index pairs
    ValueIndex* valueIndexArr = (ValueIndex*)malloc(numsSize * sizeof(ValueIndex));
    
    // Fill the array with values and their original indices
    for (int i = 0; i < numsSize; i++) {
        valueIndexArr[i].value = nums[i];
        valueIndexArr[i].index = i;
    }
    
    // Sort array by values
    qsort(valueIndexArr, numsSize, sizeof(ValueIndex), compare);
    
    // Allocate result array
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    // For each element, search for its complement
    for (int i = 0; i < numsSize; i++) {
        int complement = target - valueIndexArr[i].value;
        
        // Binary search for complement (excluding current element)
        int complementIndex = binarySearch(valueIndexArr, 0, numsSize - 1, 
                                         complement, valueIndexArr[i].index);
        
        if (complementIndex != -1) {
            // Found the pair, store indices in ascending order
            if (valueIndexArr[i].index < complementIndex) {
                result[0] = valueIndexArr[i].index;
                result[1] = complementIndex;
            } else {
                result[0] = complementIndex;
                result[1] = valueIndexArr[i].index;
            }
            
            free(valueIndexArr);
            return result;
        }
    }
    
    free(valueIndexArr);
    return result;
}

// Test function for optimized approach
void test_optimized() {
    printf("=== Optimized Approach (Sort + Binary Search) ===\n");
    
    // Test case 1
    int nums1[] = {2, 7, 11, 15};
    int target1 = 9;
    int returnSize1;
    int* result1 = twoSum_Optimized(nums1, 4, target1, &returnSize1);
    printf("Input: [2,7,11,15], target: 9\n");
    printf("Output: [%d,%d]\n\n", result1[0], result1[1]);
    free(result1);
    
    // Test case 3 (duplicate values)
    int nums3[] = {3, 3};
    int target3 = 6;
    int returnSize3;
    int* result3 = twoSum_Optimized(nums3, 2, target3, &returnSize3);
    printf("Input: [3,3], target: 6\n");
    printf("Output: [%d,%d]\n\n", result3[0], result3[1]);
    free(result3);
}
```

**Key Learning Points:**
- Sorting can help optimize search operations
- Binary search reduces lookup time from O(n) to O(log n)
- When dealing with indices, be careful to preserve original positions
- Always handle edge cases like duplicate values
- Memory management is crucial - always `free()` allocated memory

---

### Solution 3: Hash Table Simulation (Most Optimized - O(n))

Since C doesn't have built-in hash tables, we'll simulate one using a simple approach.

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define HASH_SIZE 10007  // Prime number for better distribution

// Hash table entry structure
typedef struct HashEntry {
    int key;
    int value;
    int exists;
} HashEntry;

// Simple hash function
int hash(int key) {
    return abs(key) % HASH_SIZE;
}

// Insert into hash table with linear probing
void hashInsert(HashEntry* table, int key, int value) {
    int index = hash(key);
    
    // Linear probing to handle collisions
    while (table[index].exists) {
        index = (index + 1) % HASH_SIZE;
    }
    
    table[index].key = key;
    table[index].value = value;
    table[index].exists = 1;
}

// Search in hash table
int hashSearch(HashEntry* table, int key) {
    int index = hash(key);
    
    // Linear probing to find the key
    while (table[index].exists) {
        if (table[index].key == key) {
            return table[index].value;
        }
        index = (index + 1) % HASH_SIZE;
    }
    
    return -1;  // Not found
}

/**
 * Hash Table Approach (Most Optimized):
 * - Use hash table to store (value -> index) mapping
 * - For each element, check if its complement exists in hash table
 * - If found, return indices; otherwise, add current element to hash table
 * 
 * Time Complexity: O(n) - single pass through array
 * Space Complexity: O(n) - hash table storage
 * 
 * This is the optimal solution for the Two Sum problem!
 */
int* twoSum_HashTable(int* nums, int numsSize, int target, int* returnSize) {
    // Initialize hash table
    HashEntry* hashTable = (HashEntry*)calloc(HASH_SIZE, sizeof(HashEntry));
    
    // Allocate result array
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        
        // Check if complement exists in hash table
        int complementIndex = hashSearch(hashTable, complement);
        
        if (complementIndex != -1) {
            // Found the pair!
            result[0] = complementIndex;
            result[1] = i;
            
            free(hashTable);
            return result;
        }
        
        // Add current number to hash table
        hashInsert(hashTable, nums[i], i);
    }
    
    free(hashTable);
    return result;
}

// Test function for hash table approach
void test_hashtable() {
    printf("=== Hash Table Approach (Most Optimized) ===\n");
    
    // Test all cases
    int nums1[] = {2, 7, 11, 15};
    int target1 = 9;
    int returnSize1;
    int* result1 = twoSum_HashTable(nums1, 4, target1, &returnSize1);
    printf("Input: [2,7,11,15], target: 9\n");
    printf("Output: [%d,%d]\n\n", result1[0], result1[1]);
    free(result1);
    
    int nums2[] = {3, 2, 4};
    int target2 = 6;
    int returnSize2;
    int* result2 = twoSum_HashTable(nums2, 3, target2, &returnSize2);
    printf("Input: [3,2,4], target: 6\n");
    printf("Output: [%d,%d]\n\n", result2[0], result2[1]);
    free(result2);
    
    int nums3[] = {3, 3};
    int target3 = 6;
    int returnSize3;
    int* result3 = twoSum_HashTable(nums3, 2, target3, &returnSize3);
    printf("Input: [3,3], target: 6\n");
    printf("Output: [%d,%d]\n\n", result3[0], result3[1]);
    free(result3);
}
```

**Key Learning Points:**
- Hash tables provide O(1) average-case lookup time
- Linear probing is a simple collision resolution technique
- Use prime numbers for hash table size to reduce clustering
- Single-pass algorithm is the most efficient approach
- This approach naturally handles the constraint of not using same element twice

---

### Complete Test Program

```c
// main.c - Complete test program
int main() {
    printf("TWO SUM PROBLEM - COMPLETE SOLUTIONS IN C\n");
    printf("==========================================\n\n");
    
    test_bruteforce();
    test_optimized();
    test_hashtable();
    
    printf("\nTime Complexity Comparison:\n");
    printf("1. Brute Force:    O(n²)\n");
    printf("2. Sort + Binary:  O(n log n)\n");
    printf("3. Hash Table:     O(n)\n");
    
    printf("\nSpace Complexity Comparison:\n");
    printf("1. Brute Force:    O(1)\n");
    printf("2. Sort + Binary:  O(n)\n");
    printf("3. Hash Table:     O(n)\n");
    
    return 0;
}
```

---

## Python Solutions - Language Flexibility Comparison

Python offers much more flexibility and built-in data structures that make implementation cleaner and more intuitive.

### Python Solution 1: Brute Force

```python
def two_sum_brute_force(nums, target):
    """
    Brute force approach in Python
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    # Python's range function makes nested loops cleaner
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []  # Empty list if no solution (shouldn't happen per constraints)

# Test
print("=== Python Brute Force ===")
print(two_sum_brute_force([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum_brute_force([3, 2, 4], 6))       # [1, 2]
```

### Python Solution 2: Hash Table (Optimal)

```python
def two_sum_hash_table(nums, target):
    """
    Hash table approach using Python's built-in dictionary
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List of two indices
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Python's dict is a built-in hash table - no manual implementation needed!
    seen = {}  # value -> index mapping
    
    for i, num in enumerate(nums):  # enumerate gives both index and value
        complement = target - num
        
        if complement in seen:  # O(1) lookup in dict
            return [seen[complement], i]
        
        seen[num] = i  # Store current number and its index
    
    return []

# Test
print("=== Python Hash Table ===")
print(two_sum_hash_table([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum_hash_table([3, 2, 4], 6))       # [1, 2]
print(two_sum_hash_table([3, 3], 6))          # [0, 1]
```

### Python Solution 3: One-liner using List Comprehension

```python
def two_sum_pythonic(nums, target):
    """
    Pythonic one-liner approach (though less efficient)
    
    This showcases Python's expressiveness but isn't optimal for performance
    """
    return next(([i, j] for i in range(len(nums)) 
                       for j in range(i + 1, len(nums)) 
                       if nums[i] + nums[j] == target), [])

# Test
print("=== Python Pythonic (One-liner) ===")
print(two_sum_pythonic([2, 7, 11, 15], 9))  # [0, 1]
```

---

## Python vs C: Flexibility Comparison

### 1. **Built-in Data Structures**

**C:**
- No built-in hash table - must implement manually
- Manual memory management with `malloc()` and `free()`
- Complex collision resolution and hash functions

**Python:**
```python
# Built-in dictionary acts as hash table
hash_map = {}
hash_map[key] = value
if key in hash_map:  # O(1) lookup
    return hash_map[key]
```

### 2. **Memory Management**

**C:**
```c
int* result = (int*)malloc(2 * sizeof(int));
// Must remember to free(result) later
```

**Python:**
```python
result = [index1, index2]  # Automatic memory management
# No need to worry about freeing memory
```

### 3. **Error Handling**

**C:**
```c
if (result == NULL) {
    // Handle allocation failure
    return NULL;
}
```

**Python:**
```python
try:
    result = two_sum(nums, target)
except Exception as e:
    print(f"Error: {e}")
```

### 4. **Code Readability**

**C Implementation (Hash Table):**
- ~80 lines of code
- Manual hash function
- Collision resolution
- Memory allocation/deallocation

**Python Implementation (Hash Table):**
- ~15 lines of code
- Built-in dictionary
- Automatic memory management
- More readable logic

### 5. **Development Speed**

**Python Advantages:**
- Faster prototyping
- Less boilerplate code
- Built-in testing with simple print statements
- Interactive development (REPL)
- Rich standard library

**C Advantages:**
- Better performance (closer to hardware)
- More control over memory usage
- No interpreter overhead
- Better for system-level programming

---

## Key Takeaways for Budding Developers

### 1. **Always Start Simple**
- Begin with brute force to understand the problem
- Optimize only after getting the basic solution working
- Don't sacrifice correctness for performance initially

### 2. **Understand Time-Space Tradeoffs**
- Brute force: O(n²) time, O(1) space
- Hash table: O(n) time, O(n) space
- Sometimes using more space can significantly reduce time

### 3. **Hash Tables are Powerful**
- Learn to recognize when hash tables can help
- Common pattern: "Have I seen this element before?"
- Trade space for time to achieve O(1) lookups

### 4. **Language Choice Matters**
- Python: Rapid prototyping, built-in data structures
- C: Performance-critical applications, memory control
- Choose based on requirements and constraints

### 5. **Problem-Solving Strategy**
1. Understand the problem completely
2. Think of brute force solution first
3. Identify bottlenecks (usually nested loops)
4. Consider data structures that can eliminate bottlenecks
5. Implement and test thoroughly

### 6. **Common Patterns**
- **Two pointers**: For sorted arrays
- **Hash tables**: For lookups and counting
- **Sliding window**: For subarray problems
- **Binary search**: For sorted search spaces

This Two Sum problem teaches fundamental concepts that appear in many other algorithm problems. Master these concepts, and you'll be well-prepared for similar challenges!
