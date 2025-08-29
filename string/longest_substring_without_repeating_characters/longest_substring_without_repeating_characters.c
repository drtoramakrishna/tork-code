#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

/**
 * LeetCode #3: Longest Substring Without Repeating Characters
 * 
 * Problem: Given a string s, find the length of the longest substring 
 * without repeating characters.
 * 
 * Multiple implementations demonstrating different approaches and optimizations.
 */

// =============================================================================
// Approach 1: Brute Force - Check all substrings
// Time: O(n^3), Space: O(min(m,n)) where m is charset size
// =============================================================================

bool allUnique(char* s, int start, int end) {
    bool char_set[256] = {false};  // ASCII character set
    
    for (int i = start; i < end; i++) {
        unsigned char c = (unsigned char)s[i];
        if (char_set[c]) {
            return false;  // Duplicate found
        }
        char_set[c] = true;
    }
    return true;
}

int lengthOfLongestSubstring_BruteForce(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;
    
    int max_len = 1;
    
    // Check all possible substrings
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (allUnique(s, i, j)) {
                int current_len = j - i;
                max_len = (current_len > max_len) ? current_len : max_len;
            }
        }
    }
    
    return max_len;
}

// =============================================================================
// Approach 2: Sliding Window with Character Set
// Time: O(2n) = O(n), Space: O(min(m,n))
// =============================================================================

int lengthOfLongestSubstring_SlidingWindow(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;
    
    bool char_set[256] = {false};  // Track characters in current window
    int left = 0, right = 0;
    int max_len = 0;
    
    while (right < n) {
        unsigned char right_char = (unsigned char)s[right];
        
        // If character already in window, shrink from left
        while (char_set[right_char]) {
            char_set[(unsigned char)s[left]] = false;
            left++;
        }
        
        // Add current character to window
        char_set[right_char] = true;
        
        // Update maximum length
        int current_len = right - left + 1;
        max_len = (current_len > max_len) ? current_len : max_len;
        
        right++;
    }
    
    return max_len;
}

// =============================================================================
// Approach 3: Optimized Sliding Window with Hash Map
// Time: O(n), Space: O(min(m,n))
// 
// Key optimization: Instead of incrementing left one by one,
// jump directly to the position after the duplicate character.
// =============================================================================

int lengthOfLongestSubstring_Optimized(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;
    
    int char_index[256];  // Store last seen index of each character
    for (int i = 0; i < 256; i++) {
        char_index[i] = -1;  // Initialize to -1 (not seen)
    }
    
    int left = 0;
    int max_len = 0;
    
    for (int right = 0; right < n; right++) {
        unsigned char current_char = (unsigned char)s[right];
        int last_seen = char_index[current_char];
        
        // If character was seen and is within current window
        if (last_seen >= left) {
            left = last_seen + 1;  // Jump left pointer
        }
        
        // Update last seen index
        char_index[current_char] = right;
        
        // Update maximum length
        int current_len = right - left + 1;
        max_len = (current_len > max_len) ? current_len : max_len;
    }
    
    return max_len;
}

// =============================================================================
// Approach 4: Space-Optimized for specific character sets
// For problems with known small character sets (e.g., lowercase letters only)
// Time: O(n), Space: O(1) for fixed charset
// =============================================================================

int lengthOfLongestSubstring_Lowercase(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;
    
    int char_index[26];  // Only for lowercase letters a-z
    for (int i = 0; i < 26; i++) {
        char_index[i] = -1;
    }
    
    int left = 0, max_len = 0;
    
    for (int right = 0; right < n; right++) {
        char current_char = s[right];
        
        // Check if it's a lowercase letter
        if (current_char >= 'a' && current_char <= 'z') {
            int char_idx = current_char - 'a';
            
            if (char_index[char_idx] >= left) {
                left = char_index[char_idx] + 1;
            }
            
            char_index[char_idx] = right;
            
            int current_len = right - left + 1;
            max_len = (current_len > max_len) ? current_len : max_len;
        }
    }
    
    return max_len;
}

// =============================================================================
// Approach 5: Recursive Solution (Educational)
// Time: O(n^2), Space: O(n) for recursion stack
// =============================================================================

int lengthOfLongestSubstring_Recursive_Helper(char* s, int start, int end, 
                                            bool* seen, int max_len) {
    if (start > end) {
        return max_len;
    }
    
    // Try starting a new window from current position
    memset(seen, false, 256 * sizeof(bool));
    int local_len = 0;
    
    for (int i = start; i <= end; i++) {
        unsigned char c = (unsigned char)s[i];
        if (seen[c]) {
            break;
        }
        seen[c] = true;
        local_len++;
    }
    
    int new_max = (local_len > max_len) ? local_len : max_len;
    
    // Try starting from next position
    return lengthOfLongestSubstring_Recursive_Helper(s, start + 1, end, seen, new_max);
}

int lengthOfLongestSubstring_Recursive(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;
    
    bool seen[256];
    return lengthOfLongestSubstring_Recursive_Helper(s, 0, n - 1, seen, 0);
}

// =============================================================================
// Helper Functions for Testing and Display
// =============================================================================

typedef struct {
    int length;
    int start_index;
    int end_index;
    char substring[256];
} SubstringResult;

SubstringResult findLongestSubstringWithDetails(char* s) {
    SubstringResult result = {0, 0, 0, ""};
    int n = strlen(s);
    
    if (n == 0) return result;
    
    int char_index[256];
    for (int i = 0; i < 256; i++) {
        char_index[i] = -1;
    }
    
    int left = 0;
    int max_len = 0;
    int best_left = 0, best_right = 0;
    
    for (int right = 0; right < n; right++) {
        unsigned char current_char = (unsigned char)s[right];
        
        if (char_index[current_char] >= left) {
            left = char_index[current_char] + 1;
        }
        
        char_index[current_char] = right;
        
        int current_len = right - left + 1;
        if (current_len > max_len) {
            max_len = current_len;
            best_left = left;
            best_right = right;
        }
    }
    
    result.length = max_len;
    result.start_index = best_left;
    result.end_index = best_right;
    
    // Copy substring
    int substring_len = best_right - best_left + 1;
    strncpy(result.substring, s + best_left, substring_len);
    result.substring[substring_len] = '\0';
    
    return result;
}

void printTestResult(char* input, int test_num) {
    printf("Test %d: Input = \"%s\"\n", test_num, input);
    
    // Get detailed result
    SubstringResult detail = findLongestSubstringWithDetails(input);
    
    // Test all approaches
    int bf_result = lengthOfLongestSubstring_BruteForce(input);
    int sw_result = lengthOfLongestSubstring_SlidingWindow(input);
    int opt_result = lengthOfLongestSubstring_Optimized(input);
    int rec_result = lengthOfLongestSubstring_Recursive(input);
    
    printf("  Brute Force:     %d\n", bf_result);
    printf("  Sliding Window:  %d\n", sw_result);
    printf("  Optimized:       %d\n", opt_result);
    printf("  Recursive:       %d\n", rec_result);
    printf("  Longest substring: \"%s\" (indices %d-%d)\n", 
           detail.substring, detail.start_index, detail.end_index);
    
    // Check consistency
    if (bf_result == sw_result && sw_result == opt_result && opt_result == rec_result) {
        printf("  ✓ All approaches consistent\n");
    } else {
        printf("  ✗ Inconsistent results!\n");
    }
    printf("\n");
}

// =============================================================================
// Performance Benchmarking
// =============================================================================

typedef struct {
    char* name;
    int (*func)(char*);
} Algorithm;

void benchmarkAlgorithms(char* test_string) {
    Algorithm algorithms[] = {
        {"Brute Force", lengthOfLongestSubstring_BruteForce},
        {"Sliding Window", lengthOfLongestSubstring_SlidingWindow},
        {"Optimized", lengthOfLongestSubstring_Optimized},
        {"Recursive", lengthOfLongestSubstring_Recursive}
    };
    
    int num_algorithms = sizeof(algorithms) / sizeof(algorithms[0]);
    int string_len = strlen(test_string);
    
    printf("Performance Benchmark (String length: %d)\n", string_len);
    printf("==========================================\n");
    
    for (int i = 0; i < num_algorithms; i++) {
        clock_t start = clock();
        
        // Run multiple times for better measurement
        int iterations = (string_len < 1000) ? 10000 : 100;
        int result = 0;
        
        for (int j = 0; j < iterations; j++) {
            result = algorithms[i].func(test_string);
        }
        
        clock_t end = clock();
        double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC / iterations;
        
        printf("%-15s: Result=%d, Time=%.8f seconds\n", 
               algorithms[i].name, result, time_taken);
    }
    printf("\n");
}

// =============================================================================
// Main Testing Function
// =============================================================================

void runComprehensiveTests(void) {
    printf("=== LeetCode #3: Longest Substring Without Repeating Characters ===\n\n");
    
    // Basic test cases from problem statement
    char* test_cases[] = {
        "abcabcbb",    // Expected: 3 ("abc")
        "bbbbb",       // Expected: 1 ("b") 
        "pwwkew",      // Expected: 3 ("wke")
        "",            // Expected: 0
        "au",          // Expected: 2 ("au")
        "dvdf",        // Expected: 3 ("vdf")
        "abcdef",      // Expected: 6 ("abcdef")
        "aab",         // Expected: 2 ("ab")
        "tmmzuxt",     // Expected: 5 ("mzuxt")
        "abba",        // Expected: 2 ("ab" or "ba")
        "nfpdmpi",     // Expected: 5 ("nfpdm")
        "ggububgvfk"   // Expected: 6 ("gubvfk")
    };
    
    int num_tests = sizeof(test_cases) / sizeof(test_cases[0]);
    
    printf("Comprehensive Testing:\n");
    printf("=====================\n\n");
    
    for (int i = 0; i < num_tests; i++) {
        printTestResult(test_cases[i], i + 1);
    }
    
    // Edge case testing
    printf("Edge Case Testing:\n");
    printf("==================\n\n");
    
    char* edge_cases[] = {
        "a",           // Single character
        "ab",          // Two different characters
        "aa",          // Two same characters
        "abc",         // All different
        "aaa",         // All same
        " ",           // Space character
        "a b c",       // With spaces
        "!@#$%",       // Special characters
        "123321",      // Numbers with palindrome pattern
        "abcabcabcabc" // Long repeating pattern
    };
    
    int num_edge_cases = sizeof(edge_cases) / sizeof(edge_cases[0]);
    
    for (int i = 0; i < num_edge_cases; i++) {
        printTestResult(edge_cases[i], i + 1);
    }
    
    // Performance testing
    printf("Performance Analysis:\n");
    printf("====================\n\n");
    
    char short_string[] = "abcdef";
    char medium_string[] = "abcdefghijklmnopqrstuvwxyz";
    char long_string[1001];
    
    // Create a long string with pattern
    for (int i = 0; i < 1000; i++) {
        long_string[i] = 'a' + (i % 26);
    }
    long_string[1000] = '\0';
    
    benchmarkAlgorithms(short_string);
    benchmarkAlgorithms(medium_string);
    benchmarkAlgorithms(long_string);
    
    printf("Complexity Analysis:\n");
    printf("===================\n");
    printf("1. Brute Force:       O(n³) time, O(min(m,n)) space\n");
    printf("2. Sliding Window:    O(n) time, O(min(m,n)) space\n");
    printf("3. Optimized:         O(n) time, O(min(m,n)) space\n");
    printf("4. Recursive:         O(n²) time, O(n) space\n");
    printf("\nWhere n = string length, m = character set size\n");
    printf("For ASCII: m = 256, for lowercase letters: m = 26\n");
}

// =============================================================================
// Main Function
// =============================================================================

int main(void) {
    runComprehensiveTests();
    return 0;
}
