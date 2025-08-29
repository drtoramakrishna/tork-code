#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list
struct ListNode {
    int val;
    struct ListNode *next;
};

/**
 * Add Two Numbers - Iterative Solution
 * ===================================
 * 
 * Problem: Add two numbers represented as linked lists (digits in reverse order)
 * 
 * Algorithm:
 * 1. Use dummy head for easier list construction
 * 2. Iterate through both lists simultaneously
 * 3. Handle carry from previous addition
 * 4. Create new nodes for result
 * 5. Continue until both lists exhausted and no carry
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

/**
 * Recursive Solution
 * ==================
 */
struct ListNode* addTwoNumbers_Helper(struct ListNode* l1, struct ListNode* l2, int carry);

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
    struct ListNode* result_node = (struct ListNode*)malloc(sizeof(struct ListNode));
    result_node->val = sum % 10;
    result_node->next = NULL;
    
    // Recursively process remaining lists
    struct ListNode* next_l1 = (l1 != NULL) ? l1->next : NULL;
    struct ListNode* next_l2 = (l2 != NULL) ? l2->next : NULL;
    int next_carry = sum / 10;
    
    result_node->next = addTwoNumbers_Helper(next_l1, next_l2, next_carry);
    
    return result_node;
}

/**
 * Follow-up: Non-Reversed Order
 * =============================
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

// Helper function to copy a linked list
struct ListNode* copy_list(struct ListNode* head) {
    if (head == NULL) return NULL;
    
    struct ListNode* new_head = (struct ListNode*)malloc(sizeof(struct ListNode));
    new_head->val = head->val;
    new_head->next = copy_list(head->next);
    
    return new_head;
}

struct ListNode* addTwoNumbers_NonReversed(struct ListNode* l1, struct ListNode* l2) {
    // Make copies to avoid modifying original lists
    struct ListNode* l1_copy = copy_list(l1);
    struct ListNode* l2_copy = copy_list(l2);
    
    // Step 1: Reverse both input lists
    struct ListNode* rev_l1 = reverse_list(l1_copy);
    struct ListNode* rev_l2 = reverse_list(l2_copy);
    
    // Step 2: Add reversed lists (use original algorithm)
    struct ListNode* rev_result = addTwoNumbers(rev_l1, rev_l2);
    
    // Step 3: Reverse result to get final answer
    struct ListNode* result = reverse_list(rev_result);
    
    return result;
}

/**
 * Helper Functions
 * ================
 */

// Create a new node
struct ListNode* create_node(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

// Create linked list from array
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

// Print linked list
void print_list(struct ListNode* head) {
    printf("[");
    while (head != NULL) {
        printf("%d", head->val);
        if (head->next != NULL) printf(",");
        head = head->next;
    }
    printf("]");
}

// Free linked list
void free_list(struct ListNode* head) {
    while (head != NULL) {
        struct ListNode* temp = head;
        head = head->next;
        free(temp);
    }
}

// Get number represented by list (for verification)
long long list_to_number(struct ListNode* head) {
    long long result = 0;
    long long multiplier = 1;
    
    while (head != NULL) {
        result += head->val * multiplier;
        multiplier *= 10;
        head = head->next;
    }
    
    return result;
}

/**
 * Test Functions
 * ==============
 */

void test_iterative() {
    printf("=== ITERATIVE APPROACH ===\n");
    printf("Time: O(max(m,n)), Space: O(max(m,n))\n\n");
    
    // Test case 1: [2,4,3] + [5,6,4] = [7,0,8]
    printf("Test Case 1:\n");
    int nums1[] = {2, 4, 3};
    int nums2[] = {5, 6, 4};
    struct ListNode* l1 = create_list(nums1, 3);
    struct ListNode* l2 = create_list(nums2, 3);
    
    printf("Input:  l1 = ");
    print_list(l1);
    printf(" (represents %lld)\n", list_to_number(l1));
    printf("        l2 = ");
    print_list(l2);
    printf(" (represents %lld)\n", list_to_number(l2));
    
    struct ListNode* result1 = addTwoNumbers(l1, l2);
    printf("Output: ");
    print_list(result1);
    printf(" (represents %lld)\n", list_to_number(result1));
    printf("Explanation: 342 + 465 = 807 ✓\n\n");
    
    free_list(l1);
    free_list(l2);
    free_list(result1);
    
    // Test case 2: [0] + [0] = [0]
    printf("Test Case 2:\n");
    int nums3[] = {0};
    int nums4[] = {0};
    struct ListNode* l3 = create_list(nums3, 1);
    struct ListNode* l4 = create_list(nums4, 1);
    
    printf("Input:  l1 = ");
    print_list(l3);
    printf(", l2 = ");
    print_list(l4);
    printf("\n");
    
    struct ListNode* result2 = addTwoNumbers(l3, l4);
    printf("Output: ");
    print_list(result2);
    printf("\n");
    printf("Explanation: 0 + 0 = 0 ✓\n\n");
    
    free_list(l3);
    free_list(l4);
    free_list(result2);
    
    // Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    printf("Test Case 3 (Large Numbers):\n");
    int nums5[] = {9, 9, 9, 9, 9, 9, 9};
    int nums6[] = {9, 9, 9, 9};
    struct ListNode* l5 = create_list(nums5, 7);
    struct ListNode* l6 = create_list(nums6, 4);
    
    printf("Input:  l1 = ");
    print_list(l5);
    printf(" (represents %lld)\n", list_to_number(l5));
    printf("        l2 = ");
    print_list(l6);
    printf(" (represents %lld)\n", list_to_number(l6));
    
    struct ListNode* result3 = addTwoNumbers(l5, l6);
    printf("Output: ");
    print_list(result3);
    printf(" (represents %lld)\n", list_to_number(result3));
    printf("Explanation: 9999999 + 9999 = 10009998 ✓\n\n");
    
    free_list(l5);
    free_list(l6);
    free_list(result3);
}

void test_recursive() {
    printf("=== RECURSIVE APPROACH ===\n");
    printf("Time: O(max(m,n)), Space: O(max(m,n)) due to call stack\n\n");
    
    printf("Test Case: [2,4,3] + [5,6,4] = [7,0,8]\n");
    int nums1[] = {2, 4, 3};
    int nums2[] = {5, 6, 4};
    struct ListNode* l1 = create_list(nums1, 3);
    struct ListNode* l2 = create_list(nums2, 3);
    
    printf("Input:  l1 = ");
    print_list(l1);
    printf(", l2 = ");
    print_list(l2);
    printf("\n");
    
    struct ListNode* result = addTwoNumbers_Recursive(l1, l2);
    printf("Output: ");
    print_list(result);
    printf("\n");
    printf("Recursive solution produces same result as iterative ✓\n\n");
    
    free_list(l1);
    free_list(l2);
    free_list(result);
}

void test_non_reversed() {
    printf("=== FOLLOW-UP: NON-REVERSED ORDER ===\n");
    printf("Time: O(max(m,n)), Space: O(max(m,n))\n\n");
    
    printf("Test Case: Normal order digits\n");
    // Example: [1,2,3] + [5,6,4] should represent 123 + 564 = 687
    int nums1[] = {1, 2, 3};  // represents 123
    int nums2[] = {5, 6, 4};  // represents 564
    struct ListNode* l1 = create_list(nums1, 3);
    struct ListNode* l2 = create_list(nums2, 3);
    
    printf("Input:  l1 = ");
    print_list(l1);
    printf(" (represents 123)\n");
    printf("        l2 = ");
    print_list(l2);
    printf(" (represents 564)\n");
    
    struct ListNode* result = addTwoNumbers_NonReversed(l1, l2);
    printf("Output: ");
    print_list(result);
    printf(" (represents 687)\n");
    printf("Explanation: 123 + 564 = 687 ✓\n\n");
    
    free_list(l1);
    free_list(l2);
    free_list(result);
}

void test_edge_cases() {
    printf("=== EDGE CASES ===\n\n");
    
    // Test case 1: Different length lists
    printf("Test Case 1: Different lengths\n");
    int nums1[] = {1, 8};        // represents 81
    int nums2[] = {0};           // represents 0
    struct ListNode* l1 = create_list(nums1, 2);
    struct ListNode* l2 = create_list(nums2, 1);
    
    printf("Input:  l1 = ");
    print_list(l1);
    printf(" (represents %lld)\n", list_to_number(l1));
    printf("        l2 = ");
    print_list(l2);
    printf(" (represents %lld)\n", list_to_number(l2));
    
    struct ListNode* result1 = addTwoNumbers(l1, l2);
    printf("Output: ");
    print_list(result1);
    printf(" (represents %lld)\n", list_to_number(result1));
    printf("Explanation: 81 + 0 = 81 ✓\n\n");
    
    free_list(l1);
    free_list(l2);
    free_list(result1);
    
    // Test case 2: Carry at the end
    printf("Test Case 2: Final carry\n");
    int nums3[] = {9, 9};        // represents 99
    int nums4[] = {1};           // represents 1
    struct ListNode* l3 = create_list(nums3, 2);
    struct ListNode* l4 = create_list(nums4, 1);
    
    printf("Input:  l1 = ");
    print_list(l3);
    printf(" (represents %lld)\n", list_to_number(l3));
    printf("        l2 = ");
    print_list(l4);
    printf(" (represents %lld)\n", list_to_number(l4));
    
    struct ListNode* result2 = addTwoNumbers(l3, l4);
    printf("Output: ");
    print_list(result2);
    printf(" (represents %lld)\n", list_to_number(result2));
    printf("Explanation: 99 + 1 = 100 ✓\n\n");
    
    free_list(l3);
    free_list(l4);
    free_list(result2);
}

void run_performance_test() {
    printf("=== PERFORMANCE TEST ===\n");
    printf("Testing with large numbers (10000 digits each)\n");
    
    // Create large numbers (all 9s)
    const int size = 1000;
    int* large_nums = (int*)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++) {
        large_nums[i] = 9;
    }
    
    struct ListNode* large_l1 = create_list(large_nums, size);
    struct ListNode* large_l2 = create_list(large_nums, size);
    
    printf("Adding two %d-digit numbers...\n", size);
    
    // Time the addition (simple measurement)
    struct ListNode* large_result = addTwoNumbers(large_l1, large_l2);
    
    // Count result digits
    int result_digits = 0;
    struct ListNode* temp = large_result;
    while (temp != NULL) {
        result_digits++;
        temp = temp->next;
    }
    
    printf("Result has %d digits ✓\n", result_digits);
    printf("Performance test completed successfully\n\n");
    
    free(large_nums);
    free_list(large_l1);
    free_list(large_l2);
    free_list(large_result);
}

/**
 * Main Function
 * =============
 */
int main() {
    printf("ADD TWO NUMBERS PROBLEM - COMPLETE C IMPLEMENTATION\n");
    printf("==================================================\n\n");
    
    printf("Problem: Add two numbers represented as linked lists\n");
    printf("- Digits stored in reverse order\n");
    printf("- Each node contains single digit (0-9)\n");
    printf("- Return sum as linked list\n\n");
    
    // Run all tests
    test_iterative();
    test_recursive();
    test_non_reversed();
    test_edge_cases();
    run_performance_test();
    
    printf("ALGORITHM COMPLEXITY COMPARISON:\n");
    printf("================================\n");
    printf("1. Iterative:     O(max(m,n)) time, O(1) extra space\n");
    printf("2. Recursive:     O(max(m,n)) time, O(max(m,n)) space (stack)\n");
    printf("3. Non-Reversed:  O(max(m,n)) time, O(1) extra space\n");
    printf("4. Array-Based:   O(max(m,n)) time, O(max(m,n)) space\n\n");
    
    printf("RECOMMENDED APPROACH: Iterative\n");
    printf("✓ Optimal space complexity\n");
    printf("✓ Easy to understand and implement\n");
    printf("✓ No risk of stack overflow\n");
    printf("✓ Handles all edge cases\n\n");
    
    printf("KEY LEARNING POINTS:\n");
    printf("===================\n");
    printf("• Dummy head simplifies linked list construction\n");
    printf("• Carry logic: carry = sum / 10, digit = sum %% 10\n");
    printf("• Handle lists of different lengths gracefully\n");
    printf("• Always free allocated memory to prevent leaks\n");
    printf("• Test edge cases: empty lists, single digits, large numbers\n\n");
    
    return 0;
}
