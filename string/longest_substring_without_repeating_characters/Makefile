# Makefile for LeetCode #3: Longest Substring Without Repeating Characters
# Comprehensive build system for C and Python implementations

# =============================================================================
# Configuration
# =============================================================================

CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pedantic -g
CFLAGS_RELEASE = -Wall -Wextra -std=c99 -pedantic -O3 -DNDEBUG
TARGET = longest_substring_without_repeating_characters
SOURCE = $(TARGET).c
PYTHON_SCRIPT = $(TARGET).py

# Platform-specific settings
UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
	# macOS specific flags
	CFLAGS += -Wno-deprecated-declarations
endif

# =============================================================================
# Build Targets
# =============================================================================

.PHONY: all compile debug release clean run-c run-python test benchmark help

# Default target
all: compile

# Compile with debug information
compile: $(TARGET)

$(TARGET): $(SOURCE)
	@echo "Compiling $(SOURCE) with debug flags..."
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCE)
	@echo "✓ Compilation successful!"

# Debug build with extra debugging symbols
debug: CFLAGS += -DDEBUG -fsanitize=address -fsanitize=undefined -fno-omit-frame-pointer
debug: $(TARGET)
	@echo "✓ Debug build complete with AddressSanitizer enabled"

# Optimized release build
release:
	@echo "Building optimized release version..."
	$(CC) $(CFLAGS_RELEASE) -o $(TARGET)_release $(SOURCE)
	@echo "✓ Release build complete!"

# =============================================================================
# Execution Targets
# =============================================================================

# Run C implementation
run-c: compile
	@echo "Running C implementation..."
	@echo "=========================="
	./$(TARGET)

# Run Python implementation  
run-python:
	@echo "Running Python implementation..."
	@echo "================================"
	python3 $(PYTHON_SCRIPT)

# Run both implementations
run-all: run-c run-python

# =============================================================================
# Testing Targets
# =============================================================================

# Quick test with sample cases
test: compile
	@echo "Running Quick Tests..."
	@echo "====================="
	@echo "C Implementation:"
	@./$(TARGET) | head -20
	@echo ""
	@echo "Python Implementation:"
	@python3 $(PYTHON_SCRIPT) | head -20

# Performance benchmark
benchmark: compile release
	@echo "Performance Benchmark Comparison..."
	@echo "=================================="
	@echo "Debug Build:"
	@time -p ./$(TARGET) > /dev/null
	@echo ""
	@echo "Release Build:"
	@time -p ./$(TARGET)_release > /dev/null
	@echo ""
	@echo "Python Implementation:"
	@time -p python3 $(PYTHON_SCRIPT) > /dev/null

# Memory leak detection (requires valgrind)
memcheck: compile
	@echo "Running memory leak detection..."
	@if command -v valgrind >/dev/null 2>&1; then \
		valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./$(TARGET); \
	else \
		echo "Valgrind not found. Install with: brew install valgrind (macOS) or apt-get install valgrind (Linux)"; \
	fi

# Static analysis with cppcheck (if available)
static-analysis:
	@echo "Running static analysis..."
	@if command -v cppcheck >/dev/null 2>&1; then \
		cppcheck --enable=all --std=c99 $(SOURCE); \
	else \
		echo "cppcheck not found. Install with: brew install cppcheck (macOS)"; \
	fi

# =============================================================================
# Code Quality Targets
# =============================================================================

# Format code using clang-format (if available)
format:
	@echo "Formatting C code..."
	@if command -v clang-format >/dev/null 2>&1; then \
		clang-format -i -style="{BasedOnStyle: Google, IndentWidth: 4, ColumnLimit: 100}" $(SOURCE); \
		echo "✓ C code formatted"; \
	else \
		echo "clang-format not found. Install with: brew install clang-format (macOS)"; \
	fi
	@echo "Formatting Python code..."
	@if command -v black >/dev/null 2>&1; then \
		black $(PYTHON_SCRIPT); \
		echo "✓ Python code formatted"; \
	else \
		echo "black not found. Install with: pip3 install black"; \
	fi

# Lint Python code
lint-python:
	@echo "Linting Python code..."
	@if command -v flake8 >/dev/null 2>&1; then \
		flake8 $(PYTHON_SCRIPT); \
	else \
		echo "flake8 not found. Install with: pip3 install flake8"; \
	fi
	@if command -v pylint >/dev/null 2>&1; then \
		pylint $(PYTHON_SCRIPT); \
	else \
		echo "pylint not found. Install with: pip3 install pylint"; \
	fi

# Type checking for Python
type-check:
	@echo "Type checking Python code..."
	@if command -v mypy >/dev/null 2>&1; then \
		mypy $(PYTHON_SCRIPT); \
	else \
		echo "mypy not found. Install with: pip3 install mypy"; \
	fi

# =============================================================================
# Performance Analysis
# =============================================================================

# Profile C code with gprof
profile: CFLAGS += -pg
profile: $(TARGET)
	@echo "Running profiling..."
	./$(TARGET) > /dev/null
	@if [ -f gmon.out ]; then \
		gprof $(TARGET) gmon.out > profile_report.txt; \
		echo "✓ Profile report generated: profile_report.txt"; \
	else \
		echo "No profiling data generated"; \
	fi

# Profile Python code
profile-python:
	@echo "Profiling Python code..."
	python3 -m cProfile -o python_profile.prof $(PYTHON_SCRIPT)
	@echo "✓ Python profile saved: python_profile.prof"
	@echo "View with: python3 -c 'import pstats; pstats.Stats(\"python_profile.prof\").sort_stats(\"cumulative\").print_stats(20)'"

# =============================================================================
# Assembly and Low-level Analysis
# =============================================================================

# Generate assembly code
assembly: $(SOURCE)
	@echo "Generating assembly code..."
	$(CC) $(CFLAGS_RELEASE) -S -o $(TARGET).s $(SOURCE)
	@echo "✓ Assembly code generated: $(TARGET).s"

# Disassemble compiled binary
disassemble: compile
	@echo "Disassembling binary..."
	@if command -v objdump >/dev/null 2>&1; then \
		objdump -d $(TARGET) > $(TARGET)_disassembly.txt; \
		echo "✓ Disassembly saved: $(TARGET)_disassembly.txt"; \
	else \
		echo "objdump not found"; \
	fi

# =============================================================================
# Educational Targets
# =============================================================================

# Compare algorithm complexities with timing
complexity-demo: compile release
	@echo "Algorithm Complexity Demonstration"
	@echo "=================================="
	@echo ""
	@echo "Creating test strings of increasing sizes..."
	@echo ""
	@for size in 100 500 1000 2000; do \
		echo "Testing with string size: $$size"; \
		python3 -c " \
import time; \
test_str = ''.join(chr(ord('a') + i % 26) for i in range($$size)); \
exec(open('$(PYTHON_SCRIPT)').read()); \
funcs = [lengthOfLongestSubstring_optimized, lengthOfLongestSubstring_sliding_window]; \
for func in funcs: \
	start = time.time(); \
	result = func(test_str); \
	end = time.time(); \
	print(f'  {func.__name__.replace(\"lengthOfLongestSubstring_\", \"\"):12}: {result:3d} chars, {(end-start)*1000:.3f}ms'); \
		"; \
		echo ""; \
	done

# Step-by-step algorithm walkthrough
walkthrough: compile
	@echo "Algorithm Walkthrough"
	@echo "===================="
	@echo "Testing with: 'abcabcbb'"
	@echo ""
	@echo "Expected output: Length = 3, Substring = 'abc'"
	@echo ""
	@./$(TARGET) | grep -A 10 "Test 1"

# =============================================================================
# Documentation and Help
# =============================================================================

# Generate documentation
docs:
	@echo "Generating documentation..."
	@echo "=========================="
	@echo ""
	@echo "Problem: LeetCode #3 - Longest Substring Without Repeating Characters"
	@echo "Files:"
	@echo "  - $(SOURCE): C implementation with multiple approaches"
	@echo "  - $(PYTHON_SCRIPT): Python implementation with various techniques"
	@echo "  - README.md: Comprehensive problem analysis and solutions"
	@echo ""
	@echo "Key algorithms implemented:"
	@echo "  1. Brute Force: O(n³) - Check all substrings"
	@echo "  2. Sliding Window: O(n) - Two pointers with set"
	@echo "  3. Optimized: O(n) - Hash map with index jumping"
	@echo "  4. Space Optimized: O(n) - Fixed array for known charset"
	@echo ""
	@echo "Use 'make help' for all available commands"

# Display help information
help:
	@echo "LeetCode #3: Longest Substring Without Repeating Characters"
	@echo "=========================================================="
	@echo ""
	@echo "Available targets:"
	@echo ""
	@echo "Build targets:"
	@echo "  compile        - Compile C code with debug flags (default)"
	@echo "  debug          - Compile with AddressSanitizer and debug info"
	@echo "  release        - Compile optimized release version"
	@echo ""
	@echo "Execution targets:"
	@echo "  run-c          - Run C implementation"
	@echo "  run-python     - Run Python implementation"
	@echo "  run-all        - Run both implementations"
	@echo ""
	@echo "Testing targets:"
	@echo "  test           - Quick test with sample inputs"
	@echo "  benchmark      - Performance comparison between builds"
	@echo "  memcheck       - Memory leak detection (requires valgrind)"
	@echo "  static-analysis - Static code analysis (requires cppcheck)"
	@echo ""
	@echo "Code quality targets:"
	@echo "  format         - Format code using clang-format and black"
	@echo "  lint-python    - Lint Python code with flake8 and pylint"
	@echo "  type-check     - Type check Python code with mypy"
	@echo ""
	@echo "Performance analysis:"
	@echo "  profile        - Profile C code with gprof"
	@echo "  profile-python - Profile Python code with cProfile"
	@echo "  assembly       - Generate assembly code"
	@echo "  disassemble    - Disassemble compiled binary"
	@echo ""
	@echo "Educational targets:"
	@echo "  complexity-demo - Demonstrate algorithm complexity differences"
	@echo "  walkthrough    - Step-by-step algorithm explanation"
	@echo "  docs           - Show documentation summary"
	@echo ""
	@echo "Utility targets:"
	@echo "  clean          - Remove compiled files"
	@echo "  help           - Show this help message"

# =============================================================================
# Cleanup
# =============================================================================

clean:
	@echo "Cleaning up compiled files..."
	rm -f $(TARGET) $(TARGET)_release
	rm -f $(TARGET).s $(TARGET)_disassembly.txt
	rm -f gmon.out profile_report.txt python_profile.prof
	rm -f *.o *.dSYM *.tmp
	rm -rf $(TARGET).dSYM/
	@echo "✓ Cleanup complete!"

# =============================================================================
# Advanced Features
# =============================================================================

# Create a test suite with various input patterns
create-test-suite:
	@echo "Creating comprehensive test suite..."
	@python3 -c "\
import random; \
import string; \
patterns = {'empty': '', 'single': 'a', 'two_same': 'aa', 'two_diff': 'ab', 'all_same': 'aaaaaaaaaa', 'all_diff': 'abcdefghij', 'palindrome': 'abcba', 'alternating': 'ababababab', 'random_short': ''.join(random.choices(string.ascii_lowercase, k=20)), 'random_long': ''.join(random.choices(string.ascii_lowercase, k=100)), 'worst_case': 'a' * 1000, 'best_case': string.ascii_lowercase}; \
f = open('test_cases.txt', 'w'); \
[f.write(f'{name}: {pattern}\\n') for name, pattern in patterns.items()]; \
f.close(); \
print('✓ Test suite created: test_cases.txt')"

# Install required Python packages
install-deps:
	@echo "Installing Python dependencies..."
	pip3 install black flake8 pylint mypy
	@echo "✓ Python dependencies installed"

# Display project statistics
stats:
	@echo "Project Statistics"
	@echo "=================="
	@echo "C code:"
	@wc -l $(SOURCE) | awk '{print "  Lines: " $$1}'
	@grep -c "^[[:space:]]*int\|^[[:space:]]*void\|^[[:space:]]*bool" $(SOURCE) | awk '{print "  Functions: " $$1}'
	@echo ""
	@echo "Python code:"
	@wc -l $(PYTHON_SCRIPT) | awk '{print "  Lines: " $$1}'
	@grep -c "^def " $(PYTHON_SCRIPT) | awk '{print "  Functions: " $$1}'
	@echo ""
	@echo "Documentation:"
	@if [ -f README.md ]; then wc -l README.md | awk '{print "  README lines: " $$1}'; fi
	@echo ""
	@echo "Binary size (if compiled):"
	@if [ -f $(TARGET) ]; then ls -lh $(TARGET) | awk '{print "  Debug build: " $$5}'; fi
	@if [ -f $(TARGET)_release ]; then ls -lh $(TARGET)_release | awk '{print "  Release build: " $$5}'; fi
