# LeetCode #3: Longest Substring Without Repeating Characters

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

### Examples

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

**Example 4:**
```
Input: s = ""
Output: 0
Explanation: Empty string has no substrings.
```

### Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

---

## Algorithm Analysis

### Problem Classification
- **Primary Tags:** String, Hash Table, Sliding Window
- **Secondary Tags:** Two Pointers
- **Difficulty:** Medium
- **Pattern:** Sliding Window with Hash Table

### Key Insights
1. **Sliding Window:** Maintain a window `[left, right]` with no repeating characters
2. **Hash Table:** Track the last seen index of each character
3. **Two Pointers:** Expand right, contract left when duplicates found
4. **Optimization:** Jump left pointer directly to avoid redundant checks

---

## Solution Approaches

### Approach 1: Brute Force
**Time:** O(n³), **Space:** O(min(m,n))

Check every possible substring and verify if it has unique characters.

### Approach 2: Sliding Window with Set
**Time:** O(2n) = O(n), **Space:** O(min(m,n))

Use a set to track characters in current window, slide window when duplicate found.

### Approach 3: Sliding Window with Hash Map (Optimized)
**Time:** O(n), **Space:** O(min(m,n))

Use hash map to store character indices, jump left pointer directly when duplicate found.

---

## C Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Approach 1: Brute Force - Check all substrings
 * Time: O(n^3), Space: O(min(m,n)) where m is charset size
 */
bool allUnique(char* s, int start, int end) {
    bool char_set[256] = {false};  // ASCII character set
    
    for (int i = start; i < end; i++) {
        char c = s[i];
        if (char_set[(unsigned char)c]) {
            return false;  // Duplicate found
        }
        char_set[(unsigned char)c] = true;
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
                max_len = (j - i > max_len) ? j - i : max_len;
            }
        }
    }
    
    return max_len;
}

/**
 * Approach 2: Sliding Window with Character Set
 * Time: O(2n) = O(n), Space: O(min(m,n))
 */
int lengthOfLongestSubstring_SlidingWindow(char* s) {
    int n = strlen(s);
    if (n == 0) return 0;
    
    bool char_set[256] = {false};  // Track characters in current window
    int left = 0, right = 0;
    int max_len = 0;
    
    while (right < n) {
        char right_char = s[right];
        
        // If character already in window, shrink from left
        while (char_set[(unsigned char)right_char]) {
            char_set[(unsigned char)s[left]] = false;
            left++;
        }
        
        // Add current character to window
        char_set[(unsigned char)right_char] = true;
        
        // Update maximum length
        max_len = (right - left + 1 > max_len) ? right - left + 1 : max_len;
        
        right++;
    }
    
    return max_len;
}

/**
 * Approach 3: Optimized Sliding Window with Hash Map
 * Time: O(n), Space: O(min(m,n))
 * 
 * Key optimization: Instead of incrementing left one by one,
 * jump directly to the position after the duplicate character.
 */
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
        char current_char = s[right];
        int last_seen = char_index[(unsigned char)current_char];
        
        // If character was seen and is within current window
        if (last_seen >= left) {
            left = last_seen + 1;  // Jump left pointer
        }
        
        // Update last seen index
        char_index[(unsigned char)current_char] = right;
        
        // Update maximum length
        int current_len = right - left + 1;
        max_len = (current_len > max_len) ? current_len : max_len;
    }
    
    return max_len;
}

/**
 * Approach 4: Space-Optimized for specific character sets
 * For problems with known small character sets (e.g., lowercase letters only)
 */
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
        }
        
        int current_len = right - left + 1;
        max_len = (current_len > max_len) ? current_len : max_len;
    }
    
    return max_len;
}

// Helper function for testing
void print_longest_substring(char* s, int length) {
    int n = strlen(s);
    if (n == 0) {
        printf("String: \"%s\" -> Length: %d, Substring: \"\"\n", s, length);
        return;
    }
    
    // Find the actual substring for display (using optimized approach logic)
    int char_index[256];
    for (int i = 0; i < 256; i++) {
        char_index[i] = -1;
    }
    
    int left = 0, max_len = 0, best_left = 0, best_right = 0;
    
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
    
    // Extract and print the substring
    printf("String: \"%s\" -> Length: %d, Substring: \"", s, length);
    for (int i = best_left; i <= best_right; i++) {
        printf("%c", s[i]);
    }
    printf("\"\n");
}

// Test function
void run_tests() {
    printf("=== Longest Substring Without Repeating Characters ===\n\n");
    
    char test_cases[][50] = {
        "abcabcbb",
        "bbbbb", 
        "pwwkew",
        "",
        "au",
        "dvdf",
        "abcdef",
        "aab",
        "tmmzuxt",
        "abba"
    };
    
    int num_tests = sizeof(test_cases) / sizeof(test_cases[0]);
    
    printf("Testing all approaches:\n");
    printf("======================\n\n");
    
    for (int i = 0; i < num_tests; i++) {
        char* s = test_cases[i];
        
        int result1 = lengthOfLongestSubstring_BruteForce(s);
        int result2 = lengthOfLongestSubstring_SlidingWindow(s);
        int result3 = lengthOfLongestSubstring_Optimized(s);
        
        printf("Test %d: ", i + 1);
        print_longest_substring(s, result3);
        
        // Verify all approaches give same result
        if (result1 == result2 && result2 == result3) {
            printf("✓ All approaches consistent: %d\n", result3);
        } else {
            printf("✗ Inconsistent results: BF=%d, SW=%d, OPT=%d\n", 
                   result1, result2, result3);
        }
        printf("\n");
    }
}

// Main function for demonstration
int main() {
    run_tests();
    
    printf("\nComplexity Analysis:\n");
    printf("===================\n");
    printf("1. Brute Force:       O(n³) time, O(min(m,n)) space\n");
    printf("2. Sliding Window:    O(n) time, O(min(m,n)) space\n");
    printf("3. Optimized:         O(n) time, O(min(m,n)) space\n");
    printf("4. Space Optimized:   O(n) time, O(1) space (for known charset)\n");
    printf("\nWhere n = string length, m = character set size\n");
    
    return 0;
}
```

---

## Python Implementation

The Python version demonstrates multiple approaches and leverages Python's built-in data structures:

```python
def lengthOfLongestSubstring_bruteforce(s: str) -> int:
    """
    Brute Force: Check all substrings
    Time: O(n^3), Space: O(min(m,n))
    """
    def all_unique(substring):
        return len(set(substring)) == len(substring)
    
    n = len(s)
    max_len = 0
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all_unique(s[i:j]):
                max_len = max(max_len, j - i)
    
    return max_len

def lengthOfLongestSubstring_sliding_window(s: str) -> int:
    """
    Sliding Window with Set
    Time: O(2n) = O(n), Space: O(min(m,n))
    """
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

def lengthOfLongestSubstring_optimized(s: str) -> int:
    """
    Optimized Sliding Window with Dictionary
    Time: O(n), Space: O(min(m,n))
    """
    char_index = {}  # Character -> last seen index
    left = 0
    max_len = 0
    
    for right, char in enumerate(s):
        # If character seen and within current window
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Additional Python-specific approaches
def lengthOfLongestSubstring_pythonic(s: str) -> int:
    """
    Pythonic approach using enumerate and dict.get()
    Time: O(n), Space: O(min(m,n))
    """
    seen = {}
    left = max_len = 0
    
    for right, char in enumerate(s):
        left = max(left, seen.get(char, -1) + 1)
        seen[char] = right
        max_len = max(max_len, right - left + 1)
    
    return max_len

def lengthOfLongestSubstring_functional(s: str) -> int:
    """
    Functional programming approach
    Time: O(n^2), Space: O(n)
    """
    if not s:
        return 0
    
    def expand_around_center(start):
        seen = set()
        for i in range(start, len(s)):
            if s[i] in seen:
                break
            seen.add(s[i])
        return len(seen)
    
    return max(expand_around_center(i) for i in range(len(s)))

def find_longest_substring_details(s: str):
    """
    Return both length and the actual substring
    """
    char_index = {}
    left = 0
    max_len = 0
    best_left = 0
    best_right = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        
        char_index[char] = right
        
        if right - left + 1 > max_len:
            max_len = right - left + 1
            best_left = left
            best_right = right
    
    return max_len, s[best_left:best_right + 1] if s else ""

# Testing framework
def test_all_approaches():
    print("=== Python Implementation Tests ===\n")
    
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew", 
        "",
        "au",
        "dvdf",
        "abcdef",
        "aab",
        "tmmzuxt",
        "abba"
    ]
    
    approaches = [
        ("Brute Force", lengthOfLongestSubstring_bruteforce),
        ("Sliding Window", lengthOfLongestSubstring_sliding_window),
        ("Optimized", lengthOfLongestSubstring_optimized),
        ("Pythonic", lengthOfLongestSubstring_pythonic),
        ("Functional", lengthOfLongestSubstring_functional)
    ]
    
    for i, s in enumerate(test_cases):
        print(f"Test {i + 1}: Input = \"{s}\"")
        
        results = []
        for name, func in approaches:
            try:
                result = func(s)
                results.append(result)
                print(f"  {name:15}: {result}")
            except Exception as e:
                print(f"  {name:15}: ERROR - {e}")
                results.append(None)
        
        # Show actual substring
        length, substring = find_longest_substring_details(s)
        print(f"  Actual substring: \"{substring}\" (length: {length})")
        
        # Check consistency
        valid_results = [r for r in results if r is not None]
        if len(set(valid_results)) == 1:
            print("  ✓ All approaches consistent\n")
        else:
            print("  ✗ Inconsistent results!\n")

if __name__ == "__main__":
    test_all_approaches()
    
    print("\nComplexity Comparison:")
    print("=====================")
    print("Brute Force:    O(n³) time, O(min(m,n)) space")
    print("Sliding Window: O(n) time, O(min(m,n)) space") 
    print("Optimized:      O(n) time, O(min(m,n)) space")
    print("Pythonic:       O(n) time, O(min(m,n)) space")
    print("Functional:     O(n²) time, O(n) space")
```

---

## Key Learning Points

### 1. Sliding Window Pattern
The sliding window technique is fundamental for many string/array problems:
- **Expand**: Move right pointer to include new elements
- **Contract**: Move left pointer to maintain valid window
- **Optimize**: Track window state efficiently

### 2. Hash Table Usage
- **Set**: Track presence of characters in current window
- **Map**: Store character indices for optimized jumping
- **Array**: Direct indexing for known character sets (ASCII)

### 3. String Processing Techniques
- **Substring vs Subsequence**: Contiguous vs non-contiguous
- **Index Management**: Converting between 0-based and problem logic
- **Character Set Handling**: ASCII, Unicode, case sensitivity

### 4. Optimization Strategies
- **Space-Time Tradeoffs**: Hash table vs array for character tracking
- **Early Termination**: Stop when maximum possible length reached
- **Jump Optimization**: Skip redundant left pointer increments

---

## Edge Cases to Consider

1. **Empty String**: `s = ""` → return `0`
2. **Single Character**: `s = "a"` → return `1` 
3. **All Same**: `s = "aaaa"` → return `1`
4. **All Different**: `s = "abcdef"` → return `6`
5. **Two Characters**: `s = "au"` → return `2`
6. **Palindromes**: `s = "abba"` → return `2` (either "ab" or "ba")

---

## Follow-up Questions

1. **What if the string contains Unicode characters?**
   - Use dictionary instead of fixed array
   - Handle multi-byte character encoding

2. **What if we need the actual substring, not just length?**
   - Track best window boundaries
   - Return `s[best_left:best_right+1]`

3. **What if we have memory constraints?**
   - Use array for known character sets
   - Process string in chunks if too large

4. **Can this be done in constant space?**
   - Yes, if character set is bounded (e.g., only lowercase letters)
   - Use fixed-size array instead of hash table

---

## Related Problems

1. **LeetCode #159**: Longest Substring with At Most Two Distinct Characters
2. **LeetCode #340**: Longest Substring with At Most K Distinct Characters  
3. **LeetCode #76**: Minimum Window Substring
4. **LeetCode #438**: Find All Anagrams in a String
5. **LeetCode #567**: Permutation in String

All these problems use similar sliding window + hash table techniques!
