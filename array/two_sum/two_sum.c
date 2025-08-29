#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define HASH_SIZE 10007  // Prime number for better hash distribution

// Hash table entry structure
typedef struct HashEntry {
    int key;
    int value;
    int exists;
} HashEntry;

// Structure to store value and original index (for optimized sorting approach)
typedef struct {
    int value;
    int index;
} ValueIndex;

// Function prototypes
int* twoSum_BruteForce(int* nums, int numsSize, int target, int* returnSize);
int* twoSum_Optimized(int* nums, int numsSize, int target, int* returnSize);
int* twoSum_HashTable(int* nums, int numsSize, int target, int* returnSize);

// Helper functions
int compare(const void* a, const void* b);
int binarySearch(ValueIndex* arr, int left, int right, int target, int excludeIndex);
int hash(int key);
void hashInsert(HashEntry* table, int key, int value);
int hashSearch(HashEntry* table, int key);

// Test functions
void test_bruteforce();
void test_optimized();
void test_hashtable();
void print_array(int* arr, int size);

/**
 * SOLUTION 1: BRUTE FORCE APPROACH
 * Time Complexity: O(n²)
 * Space Complexity: O(1)
 * 
 * Check every possible pair of elements to find the target sum.
 */
int* twoSum_BruteForce(int* nums, int numsSize, int target, int* returnSize) {
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    for (int i = 0; i < numsSize - 1; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }
    
    return result;
}

/**
 * SOLUTION 2: SORTING + BINARY SEARCH APPROACH
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 * 
 * Sort the array while preserving original indices, then use binary search.
 */
int* twoSum_Optimized(int* nums, int numsSize, int target, int* returnSize) {
    ValueIndex* valueIndexArr = (ValueIndex*)malloc(numsSize * sizeof(ValueIndex));
    
    // Fill array with values and original indices
    for (int i = 0; i < numsSize; i++) {
        valueIndexArr[i].value = nums[i];
        valueIndexArr[i].index = i;
    }
    
    // Sort by values
    qsort(valueIndexArr, numsSize, sizeof(ValueIndex), compare);
    
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    // Search for complement using binary search
    for (int i = 0; i < numsSize; i++) {
        int complement = target - valueIndexArr[i].value;
        int complementIndex = binarySearch(valueIndexArr, 0, numsSize - 1, 
                                         complement, valueIndexArr[i].index);
        
        if (complementIndex != -1) {
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

/**
 * SOLUTION 3: HASH TABLE APPROACH (MOST OPTIMAL)
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * 
 * Use hash table to store seen elements and find complement in O(1) time.
 */
int* twoSum_HashTable(int* nums, int numsSize, int target, int* returnSize) {
    HashEntry* hashTable = (HashEntry*)calloc(HASH_SIZE, sizeof(HashEntry));
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    
    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int complementIndex = hashSearch(hashTable, complement);
        
        if (complementIndex != -1) {
            result[0] = complementIndex;
            result[1] = i;
            free(hashTable);
            return result;
        }
        
        hashInsert(hashTable, nums[i], i);
    }
    
    free(hashTable);
    return result;
}

// Helper function for sorting
int compare(const void* a, const void* b) {
    ValueIndex* va = (ValueIndex*)a;
    ValueIndex* vb = (ValueIndex*)b;
    return va->value - vb->value;
}

// Binary search for complement
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

// Simple hash function
int hash(int key) {
    return abs(key) % HASH_SIZE;
}

// Insert into hash table with linear probing
void hashInsert(HashEntry* table, int key, int value) {
    int index = hash(key);
    
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
    
    while (table[index].exists) {
        if (table[index].key == key) {
            return table[index].value;
        }
        index = (index + 1) % HASH_SIZE;
    }
    
    return -1;
}

// Utility function to print array
void print_array(int* arr, int size) {
    printf("[");
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
        if (i < size - 1) printf(",");
    }
    printf("]\n");
}

// Test functions
void test_bruteforce() {
    printf("=== BRUTE FORCE APPROACH O(n²) ===\n");
    
    int nums1[] = {2, 7, 11, 15};
    int target1 = 9;
    int returnSize1;
    int* result1 = twoSum_BruteForce(nums1, 4, target1, &returnSize1);
    printf("Input: [2,7,11,15], target: 9 → Output: ");
    print_array(result1, returnSize1);
    free(result1);
    
    int nums2[] = {3, 2, 4};
    int target2 = 6;
    int returnSize2;
    int* result2 = twoSum_BruteForce(nums2, 3, target2, &returnSize2);
    printf("Input: [3,2,4], target: 6 → Output: ");
    print_array(result2, returnSize2);
    free(result2);
    
    printf("\n");
}

void test_optimized() {
    printf("=== OPTIMIZED APPROACH O(n log n) ===\n");
    
    int nums1[] = {2, 7, 11, 15};
    int target1 = 9;
    int returnSize1;
    int* result1 = twoSum_Optimized(nums1, 4, target1, &returnSize1);
    printf("Input: [2,7,11,15], target: 9 → Output: ");
    print_array(result1, returnSize1);
    free(result1);
    
    int nums3[] = {3, 3};
    int target3 = 6;
    int returnSize3;
    int* result3 = twoSum_Optimized(nums3, 2, target3, &returnSize3);
    printf("Input: [3,3], target: 6 → Output: ");
    print_array(result3, returnSize3);
    free(result3);
    
    printf("\n");
}

void test_hashtable() {
    printf("=== HASH TABLE APPROACH O(n) - OPTIMAL ===\n");
    
    int nums1[] = {2, 7, 11, 15};
    int target1 = 9;
    int returnSize1;
    int* result1 = twoSum_HashTable(nums1, 4, target1, &returnSize1);
    printf("Input: [2,7,11,15], target: 9 → Output: ");
    print_array(result1, returnSize1);
    free(result1);
    
    int nums2[] = {3, 2, 4};
    int target2 = 6;
    int returnSize2;
    int* result2 = twoSum_HashTable(nums2, 3, target2, &returnSize2);
    printf("Input: [3,2,4], target: 6 → Output: ");
    print_array(result2, returnSize2);
    free(result2);
    
    int nums3[] = {3, 3};
    int target3 = 6;
    int returnSize3;
    int* result3 = twoSum_HashTable(nums3, 2, target3, &returnSize3);
    printf("Input: [3,3], target: 6 → Output: ");
    print_array(result3, returnSize3);
    free(result3);
    
    printf("\n");
}

int main() {
    printf("TWO SUM PROBLEM - COMPLETE C IMPLEMENTATION\n");
    printf("===========================================\n\n");
    
    test_bruteforce();
    test_optimized();
    test_hashtable();
    
    printf("COMPLEXITY ANALYSIS:\n");
    printf("┌─────────────────┬─────────────────┬─────────────────┐\n");
    printf("│ Approach        │ Time Complexity │ Space Complexity│\n");
    printf("├─────────────────┼─────────────────┼─────────────────┤\n");
    printf("│ Brute Force     │ O(n²)           │ O(1)            │\n");
    printf("│ Sort + Binary   │ O(n log n)      │ O(n)            │\n");
    printf("│ Hash Table      │ O(n)            │ O(n)            │\n");
    printf("└─────────────────┴─────────────────┴─────────────────┘\n");
    
    return 0;
}
