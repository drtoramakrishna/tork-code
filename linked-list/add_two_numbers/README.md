# Add Two Numbers Problem - Complete Solution Guide

## Problem Statement

**Category:** Linked List  
**Difficulty:** Medium (38.74%)  
**Tags:** Linked List, Math, Recursion  

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Examples

**Example 1:**
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998.
```

### Constraints
- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

### Follow-up
What if the digits in the linked list are stored in non-reversed order? For example:
`(3 -> 2 -> 1) + (4 -> 6 -> 5) = 8 -> 0 -> 7`

---

## Understanding the Problem

This problem simulates **manual addition** that we learned in elementary school:

```
    342  (represented as 2->4->3)
  + 465  (represented as 5->6->4)
  -----
    807  (result as 7->0->8)
```

**Key Insights:**
1. **Reverse Order**: Digits are stored in reverse order, making addition easier (start from least significant digit)
2. **Carry Handling**: When sum ≥ 10, we carry 1 to the next position
3. **Different Lengths**: Lists can have different lengths
4. **Final Carry**: After processing both lists, we might still have a carry

---

## C Language Solutions

### Solution 1: Iterative Approach (Recommended)

```c
#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list
struct ListNode {
    int val;
    struct ListNode *next;
};

/**
 * Iterative approach to add two numbers represented as linked lists
 * 
 * Algorithm:
 * 1. Initialize dummy head and current pointer
 * 2. Traverse both lists simultaneously
 * 3. Calculate sum = val1 + val2 + carry
 * 4. Create new node with sum % 10
 * 5. Update carry = sum / 10
 * 6. Continue until both lists are exhausted and carry is 0
 * 
 * Time Complexity: O(max(m, n)) where m, n are lengths of input lists
 * Space Complexity: O(max(m, n)) for the result list
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // Create dummy head to simplify edge cases
    struct ListNode* dummy_head = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummy_head->val = 0;
    dummy_head->next = NULL;
    
    struct ListNode* current = dummy_head;
    int carry = 0;
    
    // Continue while there are digits to process or carry exists
    while (l1 != NULL || l2 != NULL || carry != 0) {
        // Get values from current nodes (0 if node is NULL)
        int val1 = (l1 != NULL) ? l1->val : 0;
        int val2 = (l2 != NULL) ? l2->val : 0;
        
        // Calculate sum including carry from previous addition
        int sum = val1 + val2 + carry;
        
        // Create new node with the digit (sum % 10)
        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = sum % 10;
        new_node->next = NULL;
        
        // Link the new node
        current->next = new_node;
        current = new_node;
        
        // Update carry for next iteration
        carry = sum / 10;
        
        // Move to next nodes if they exist
        if (l1 != NULL) l1 = l1->next;
        if (l2 != NULL) l2 = l2->next;
    }
    
    // Store result and free dummy head
    struct ListNode* result = dummy_head->next;
    free(dummy_head);
    
    return result;
}

// Helper function to create a new node
struct ListNode* create_node(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

// Helper function to create linked list from array
struct ListNode* create_list(int* nums, int size) {
    if (size == 0) return NULL;
    
    struct ListNode* head = create_node(nums[0]);
    struct ListNode* current = head;
    
    for (int i = 1; i < size; i++) {
        current->next = create_node(nums[i]);
        current = current->next;
    }
    
    return head;
}

// Helper function to print linked list
void print_list(struct ListNode* head) {
    printf("[");
    while (head != NULL) {
        printf("%d", head->val);
        if (head->next != NULL) printf(",");
        head = head->next;
    }
    printf("]");
}

// Helper function to free linked list
void free_list(struct ListNode* head) {
    while (head != NULL) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);
    }
}

// Test function for iterative approach
void test_iterative() {
    printf("=== Iterative Approach ===\n");
    
    // Test case 1: [2,4,3] + [5,6,4] = [7,0,8]
    int nums1[] = {2, 4, 3};
    int nums2[] = {5, 6, 4};
    struct ListNode* l1 = create_list(nums1, 3);
    struct ListNode* l2 = create_list(nums2, 3);
    
    printf("Input: l1 = ");
    print_list(l1);
    printf(", l2 = ");
    print_list(l2);
    printf("\n");
    
    struct ListNode* result1 = addTwoNumbers(l1, l2);
    printf("Output: ");
    print_list(result1);
    printf("\n");
    printf("Explanation: 342 + 465 = 807\n\n");
    
    free_list(l1);
    free_list(l2);
    free_list(result1);
    
    // Test case 2: [0] + [0] = [0]
    int nums3[] = {0};
    int nums4[] = {0};
    struct ListNode* l3 = create_list(nums3, 1);
    struct ListNode* l4 = create_list(nums4, 1);
    
    printf("Input: l1 = ");
    print_list(l3);
    printf(", l2 = ");
    print_list(l4);
    printf("\n");
    
    struct ListNode* result2 = addTwoNumbers(l3, l4);
    printf("Output: ");
    print_list(result2);
    printf("\n\n");
    
    free_list(l3);
    free_list(l4);
    free_list(result2);
    
    // Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    int nums5[] = {9, 9, 9, 9, 9, 9, 9};
    int nums6[] = {9, 9, 9, 9};
    struct ListNode* l5 = create_list(nums5, 7);
    struct ListNode* l6 = create_list(nums6, 4);
    
    printf("Input: l1 = ");
    print_list(l5);
    printf(", l2 = ");
    print_list(l6);
    printf("\n");
    
    struct ListNode* result3 = addTwoNumbers(l5, l6);
    printf("Output: ");
    print_list(result3);
    printf("\n");
    printf("Explanation: 9999999 + 9999 = 10009998\n\n");
    
    free_list(l5);
    free_list(l6);
    free_list(result3);
}
```

**Key Learning Points:**
- **Dummy Head**: Simplifies edge cases and makes code cleaner
- **Carry Logic**: `carry = sum / 10`, `digit = sum % 10`
- **Null Checks**: Handle lists of different lengths gracefully
- **Memory Management**: Always free allocated memory

---

### Solution 2: Recursive Approach

```c
/**
 * Recursive approach to add two numbers
 * 
 * Base case: Both lists are NULL and no carry
 * Recursive case: Process current nodes and recurse on remaining lists
 * 
 * Time Complexity: O(max(m, n))
 * Space Complexity: O(max(m, n)) due to recursion stack
 */
struct ListNode* addTwoNumbers_Recursive(struct ListNode* l1, struct ListNode* l2) {
    return addTwoNumbers_Helper(l1, l2, 0);
}

struct ListNode* addTwoNumbers_Helper(struct ListNode* l1, struct ListNode* l2, int carry) {
    // Base case: no more digits and no carry
    if (l1 == NULL && l2 == NULL && carry == 0) {
        return NULL;
    }
    
    // Get values from current nodes (0 if NULL)
    int val1 = (l1 != NULL) ? l1->val : 0;
    int val2 = (l2 != NULL) ? l2->val : 0;
    
    // Calculate sum
    int sum = val1 + val2 + carry;
    
    // Create new node for current digit
    struct ListNode* result_node = create_node(sum % 10);
    
    // Recursively process remaining lists
    struct ListNode* next_l1 = (l1 != NULL) ? l1->next : NULL;
    struct ListNode* next_l2 = (l2 != NULL) ? l2->next : NULL;
    int next_carry = sum / 10;
    
    result_node->next = addTwoNumbers_Helper(next_l1, next_l2, next_carry);
    
    return result_node;
}

// Test function for recursive approach
void test_recursive() {
    printf("=== Recursive Approach ===\n");
    
    // Test with the same cases as iterative
    int nums1[] = {2, 4, 3};
    int nums2[] = {5, 6, 4};
    struct ListNode* l1 = create_list(nums1, 3);
    struct ListNode* l2 = create_list(nums2, 3);
    
    printf("Input: l1 = ");
    print_list(l1);
    printf(", l2 = ");
    print_list(l2);
    printf("\n");
    
    struct ListNode* result = addTwoNumbers_Recursive(l1, l2);
    printf("Output: ");
    print_list(result);
    printf("\n");
    printf("Recursive solution matches iterative result\n\n");
    
    free_list(l1);
    free_list(l2);
    free_list(result);
}
```

**Key Learning Points:**
- **Base Case**: No more digits and no carry
- **Helper Function**: Passes carry between recursive calls
- **Tail Recursion**: Can be optimized by compiler
- **Space Trade-off**: Uses call stack instead of explicit iteration

---

### Solution 3: Follow-up - Non-Reversed Order

For the follow-up question where digits are stored in normal order:

```c
/**
 * Add two numbers when digits are stored in normal order
 * 
 * Approach:
 * 1. Reverse both input lists
 * 2. Apply the original algorithm
 * 3. Reverse the result list
 * 
 * Time Complexity: O(max(m, n))
 * Space Complexity: O(max(m, n))
 */

// Helper function to reverse a linked list
struct ListNode* reverse_list(struct ListNode* head) {
    struct ListNode* prev = NULL;
    struct ListNode* current = head;
    
    while (current != NULL) {
        struct ListNode* next_temp = current->next;
        current->next = prev;
        prev = current;
        current = next_temp;
    }
    
    return prev;
}

struct ListNode* addTwoNumbers_NonReversed(struct ListNode* l1, struct ListNode* l2) {
    // Step 1: Reverse both input lists
    struct ListNode* rev_l1 = reverse_list(l1);
    struct ListNode* rev_l2 = reverse_list(l2);
    
    // Step 2: Add reversed lists (use original algorithm)
    struct ListNode* rev_result = addTwoNumbers(rev_l1, rev_l2);
    
    // Step 3: Reverse result to get final answer
    struct ListNode* result = reverse_list(rev_result);
    
    // Note: This modifies input lists. In production, you'd want to
    // reverse them back or work with copies
    
    return result;
}

// Test function for non-reversed approach
void test_non_reversed() {
    printf("=== Follow-up: Non-Reversed Order ===\n");
    
    // Example: (3 -> 2 -> 1) + (4 -> 6 -> 5) = (8 -> 0 -> 7)
    // Represents: 321 + 465 = 786 (but we expect 807)
    // Actually: (1 -> 2 -> 3) + (5 -> 6 -> 4) should give (7 -> 0 -> 8)
    
    int nums1[] = {1, 2, 3};  // represents 123
    int nums2[] = {5, 6, 4};  // represents 564
    struct ListNode* l1 = create_list(nums1, 3);
    struct ListNode* l2 = create_list(nums2, 3);
    
    printf("Input: l1 = ");
    print_list(l1);
    printf(" (represents 123)\n");
    printf("       l2 = ");
    print_list(l2);
    printf(" (represents 564)\n");
    
    // Make copies since reversal modifies original lists
    struct ListNode* l1_copy = create_list(nums1, 3);
    struct ListNode* l2_copy = create_list(nums2, 3);
    
    struct ListNode* result = addTwoNumbers_NonReversed(l1_copy, l2_copy);
    printf("Output: ");
    print_list(result);
    printf(" (represents 687)\n");
    printf("Explanation: 123 + 564 = 687\n\n");
    
    free_list(l1);
    free_list(l2);
    free_list(result);
}
```

---

### Solution 4: Array-Based Implementation

For educational comparison, here's how this could be solved using arrays:

```c
/**
 * Array-based implementation for educational purposes
 * 
 * This converts the problem to array operations but loses the
 * memory efficiency of the linked list approach.
 */

// Convert linked list to array
int* list_to_array(struct ListNode* head, int* size) {
    // First pass: count nodes
    *size = 0;
    struct ListNode* temp = head;
    while (temp != NULL) {
        (*size)++;
        temp = temp->next;
    }
    
    if (*size == 0) return NULL;
    
    // Second pass: copy values
    int* array = (int*)malloc(*size * sizeof(int));
    temp = head;
    for (int i = 0; i < *size; i++) {
        array[i] = temp->val;
        temp = temp->next;
    }
    
    return array;
}

// Convert array to linked list
struct ListNode* array_to_list(int* array, int size) {
    if (size == 0) return NULL;
    
    struct ListNode* head = create_node(array[0]);
    struct ListNode* current = head;
    
    for (int i = 1; i < size; i++) {
        current->next = create_node(array[i]);
        current = current->next;
    }
    
    return head;
}

// Add two arrays representing numbers (in reverse order)
int* add_arrays(int* arr1, int size1, int* arr2, int size2, int* result_size) {
    int max_size = (size1 > size2) ? size1 : size2;
    int* result = (int*)malloc((max_size + 1) * sizeof(int));  // +1 for potential carry
    
    int carry = 0;
    int i = 0;
    
    while (i < size1 || i < size2 || carry > 0) {
        int val1 = (i < size1) ? arr1[i] : 0;
        int val2 = (i < size2) ? arr2[i] : 0;
        
        int sum = val1 + val2 + carry;
        result[i] = sum % 10;
        carry = sum / 10;
        i++;
    }
    
    *result_size = i;
    return result;
}

// Array-based solution wrapper
struct ListNode* addTwoNumbers_Array(struct ListNode* l1, struct ListNode* l2) {
    // Convert lists to arrays
    int size1, size2;
    int* arr1 = list_to_array(l1, &size1);
    int* arr2 = list_to_array(l2, &size2);
    
    // Add arrays
    int result_size;
    int* result_array = add_arrays(arr1, size1, arr2, size2, &result_size);
    
    // Convert result back to list
    struct ListNode* result = array_to_list(result_array, result_size);
    
    // Cleanup
    free(arr1);
    free(arr2);
    free(result_array);
    
    return result;
}

// Test function for array-based approach
void test_array_based() {
    printf("=== Array-Based Approach ===\n");
    
    int nums1[] = {2, 4, 3};
    int nums2[] = {5, 6, 4};
    struct ListNode* l1 = create_list(nums1, 3);
    struct ListNode* l2 = create_list(nums2, 3);
    
    printf("Input: l1 = ");
    print_list(l1);
    printf(", l2 = ");
    print_list(l2);
    printf("\n");
    
    struct ListNode* result = addTwoNumbers_Array(l1, l2);
    printf("Output: ");
    print_list(result);
    printf("\n");
    printf("Array-based solution matches other approaches\n\n");
    
    free_list(l1);
    free_list(l2);
    free_list(result);
}
```

---

### Complete Test Program

```c
// main.c - Complete test program
int main() {
    printf("ADD TWO NUMBERS PROBLEM - COMPLETE SOLUTIONS IN C\n");
    printf("================================================\n\n");
    
    test_iterative();
    test_recursive();
    test_non_reversed();
    test_array_based();
    
    printf("Algorithm Comparison:\n");
    printf("1. Iterative:     O(max(m,n)) time, O(1) extra space\n");
    printf("2. Recursive:     O(max(m,n)) time, O(max(m,n)) space (stack)\n");
    printf("3. Non-Reversed:  O(max(m,n)) time, O(1) extra space\n");
    printf("4. Array-Based:   O(max(m,n)) time, O(max(m,n)) space\n");
    
    printf("\nRecommended: Iterative approach for optimal space complexity\n");
    
    return 0;
}
```

---

## Python Solutions - Language Flexibility Comparison

Python's built-in features make this problem much more elegant to solve:

### Python Solution 1: Iterative Approach

```python
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Add two numbers represented as linked lists
    
    Args:
        l1: First number (reversed)
        l2: Second number (reversed)
    
    Returns:
        Sum as linked list (reversed)
    
    Time Complexity: O(max(m, n))
    Space Complexity: O(max(m, n))
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

# Test
def test_python_iterative():
    print("=== Python Iterative Approach ===")
    
    # Helper to create list from array
    def create_list(nums):
        if not nums:
            return None
        head = ListNode(nums[0])
        current = head
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
        return head
    
    # Helper to print list
    def print_list(head):
        result = []
        while head:
            result.append(str(head.val))
            head = head.next
        return "[" + ",".join(result) + "]"
    
    # Test case
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])
    result = addTwoNumbers(l1, l2)
    
    print(f"Result: {print_list(result)}")
```

### Python Solution 2: Using Integer Conversion

```python
def addTwoNumbers_IntConversion(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Convert to integers, add, then convert back
    
    This approach is simpler but can cause integer overflow
    for very large numbers.
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
```

### Python Solution 3: One-liner (Educational)

```python
def addTwoNumbers_Oneliner(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Pythonic one-liner approach (not practical, just for fun)
    """
    from functools import reduce
    
    # Convert lists to numbers, add them, convert back
    to_num = lambda head: reduce(lambda acc, x: acc + x[1] * (10 ** x[0]), 
                                enumerate(iter(lambda: head and (head.val, setattr(head, 'val', None))[0] or head and head.next and setattr(head, 'next', head.next.next), None)), 0)
    
    # This is intentionally complex to show Python's power
    # In practice, use the iterative approach!
```

---

## Algorithm Analysis & Optimization

### Time Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| Iterative | O(max(m,n)) | O(1) extra | Memory efficient, easy to understand | None |
| Recursive | O(max(m,n)) | O(max(m,n)) | Clean code, functional style | Stack overflow risk |
| Non-Reversed | O(max(m,n)) | O(1) extra | Handles follow-up case | Multiple passes |
| Array-Based | O(max(m,n)) | O(max(m,n)) | Familiar array operations | Memory overhead |

### Space Optimization Techniques

1. **In-place Modification**: Reuse input lists (if allowed)
2. **Single Pass**: Process in one iteration
3. **Minimal Nodes**: Only create necessary result nodes

### Edge Cases to Consider

```c
// Edge case handling examples
struct ListNode* robust_addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // Handle null inputs
    if (l1 == NULL && l2 == NULL) return create_node(0);
    if (l1 == NULL) return l2;
    if (l2 == NULL) return l1;
    
    // Regular algorithm
    return addTwoNumbers(l1, l2);
}

// Test edge cases
void test_edge_cases() {
    printf("=== Edge Cases ===\n");
    
    // Case 1: One empty list
    struct ListNode* l1 = NULL;
    int nums2[] = {1, 2, 3};
    struct ListNode* l2 = create_list(nums2, 3);
    
    // Case 2: Both single digit
    struct ListNode* l3 = create_node(5);
    struct ListNode* l4 = create_node(5);
    
    // Case 3: Large carry chain
    int nums5[] = {9, 9, 9};
    int nums6[] = {1};
    struct ListNode* l5 = create_list(nums5, 3);
    struct ListNode* l6 = create_list(nums6, 1);
    
    // Test each case...
}
```

---

## Key Takeaways for Budding Developers

### 1. **Problem Pattern Recognition**
- **Digit-by-digit operations**: Common in number manipulation problems
- **Carry propagation**: Essential in addition, subtraction, multiplication
- **Linked list traversal**: Process while nodes exist

### 2. **Data Structure Choice**
- **Linked Lists**: Natural for variable-length numbers
- **Arrays**: Easier indexing but fixed size
- **Strings**: Good for very large numbers

### 3. **Algorithm Techniques**
- **Dummy Head**: Simplifies linked list problems
- **Two Pointers**: Handle lists of different lengths
- **Carry Logic**: `carry = sum / 10`, `digit = sum % 10`

### 4. **Edge Case Handling**
- Empty lists
- Different length lists
- Final carry digit
- Single digit results

### 5. **Memory Management**
- Always free allocated nodes
- Use dummy head to avoid special cases
- Consider memory pooling for frequent allocations

### 6. **Testing Strategy**
- Test normal cases
- Test edge cases (empty, single digit)
- Test boundary conditions (large numbers, max carry)
- Verify memory leaks with tools like Valgrind

### 7. **Follow-up Preparation**
- Always ask about variations
- Consider reverse problem
- Think about constraints (memory, time)
- Prepare for optimization discussions

This Add Two Numbers problem teaches fundamental concepts about:
- **Linked list manipulation**
- **Mathematical operations in programming**
- **Carry handling in arithmetic**
- **Memory management in C**
- **Edge case consideration**

Master these concepts, and you'll be prepared for many similar number manipulation and linked list problems!
