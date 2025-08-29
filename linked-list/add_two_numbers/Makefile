# Makefile for Add Two Numbers Problem
# ====================================

CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -g -O2
TARGET = add_two_numbers
SOURCE = add_two_numbers.c
PYTHON = python3

# Default target
all: compile

# Compile the C program
compile:
	@echo "🔨 Compiling Add Two Numbers (C)..."
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCE)
	@echo "✅ Compilation successful!"

# Run the C program
run-c: compile
	@echo "🚀 Running Add Two Numbers (C Implementation)..."
	@echo ""
	./$(TARGET)

# Run the Python program
run-python:
	@echo "🐍 Running Add Two Numbers (Python Implementation)..."
	@echo ""
	$(PYTHON) add_two_numbers.py

# Run both implementations
run: run-c
	@echo ""
	@echo "=" * 60
	@echo ""
	@$(MAKE) run-python

# Debug with GDB
debug: compile
	@echo "🐛 Starting GDB debugger..."
	gdb ./$(TARGET)

# Memory check with Valgrind (if available)
memcheck: compile
	@echo "🔍 Running memory check with Valgrind..."
	@if command -v valgrind >/dev/null 2>&1; then \
		valgrind --leak-check=full --show-leak-kinds=all --track-origins=yes ./$(TARGET); \
	else \
		echo "⚠️  Valgrind not found. Install valgrind for memory checking."; \
	fi

# Performance profiling
profile: compile
	@echo "📊 Running performance profile..."
	@if command -v time >/dev/null 2>&1; then \
		time ./$(TARGET); \
	else \
		echo "⚠️  time command not found."; \
	fi

# Static analysis with cppcheck (if available)
analyze:
	@echo "🔍 Running static analysis..."
	@if command -v cppcheck >/dev/null 2>&1; then \
		cppcheck --enable=all --std=c99 $(SOURCE); \
	else \
		echo "⚠️  cppcheck not found. Install cppcheck for static analysis."; \
	fi

# Format code (if clang-format available)
format:
	@echo "🎨 Formatting code..."
	@if command -v clang-format >/dev/null 2>&1; then \
		clang-format -i $(SOURCE); \
		echo "✅ Code formatted!"; \
	else \
		echo "⚠️  clang-format not found."; \
	fi

# Test different compiler optimizations
test-optimizations:
	@echo "⚡ Testing different optimization levels..."
	@echo "Building with -O0 (no optimization):"
	@$(CC) $(CFLAGS) -O0 -o $(TARGET)_O0 $(SOURCE)
	@time ./$(TARGET)_O0 > /dev/null
	
	@echo "Building with -O2 (moderate optimization):"
	@$(CC) $(CFLAGS) -O2 -o $(TARGET)_O2 $(SOURCE)
	@time ./$(TARGET)_O2 > /dev/null
	
	@echo "Building with -O3 (high optimization):"
	@$(CC) $(CFLAGS) -O3 -o $(TARGET)_O3 $(SOURCE)
	@time ./$(TARGET)_O3 > /dev/null
	
	@rm -f $(TARGET)_O0 $(TARGET)_O2 $(TARGET)_O3

# Generate assembly output (for learning)
assembly:
	@echo "📝 Generating assembly output..."
	$(CC) $(CFLAGS) -S -o $(TARGET).s $(SOURCE)
	@echo "✅ Assembly code written to $(TARGET).s"

# Clean build artifacts
clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -f $(TARGET) $(TARGET).s $(TARGET)_O* *.o core
	@echo "✅ Clean complete!"

# Create project archive
archive:
	@echo "📦 Creating project archive..."
	tar -czf add_two_numbers.tar.gz *.c *.py *.md Makefile
	@echo "✅ Archive created: add_two_numbers.tar.gz"

# Install dependencies (Python)
install-deps:
	@echo "📥 Installing Python dependencies..."
	$(PYTHON) -m pip install --user typing_extensions
	@echo "✅ Dependencies installed!"

# Run comprehensive tests
test: compile
	@echo "🧪 Running comprehensive tests..."
	@echo ""
	@echo "Testing C implementation:"
	./$(TARGET)
	@echo ""
	@echo "Testing Python implementation:"
	$(PYTHON) add_two_numbers.py
	@echo ""
	@echo "✅ All tests completed!"

# Show project statistics
stats:
	@echo "📊 PROJECT STATISTICS"
	@echo "====================="
	@echo "C source lines:      $$(wc -l < $(SOURCE))"
	@echo "Python source lines: $$(wc -l < add_two_numbers.py)"
	@echo "Total files:         $$(ls *.c *.py *.md Makefile 2>/dev/null | wc -l)"
	@echo "Executable size:     $$(du -h $(TARGET) 2>/dev/null | cut -f1 || echo 'Not compiled')"

# Show help
help:
	@echo "🎯 ADD TWO NUMBERS - MAKEFILE COMMANDS"
	@echo "======================================"
	@echo ""
	@echo "Build Commands:"
	@echo "  make compile          - Compile C program"
	@echo "  make all             - Same as compile (default)"
	@echo ""
	@echo "Run Commands:"
	@echo "  make run-c           - Run C implementation"
	@echo "  make run-python      - Run Python implementation"
	@echo "  make run             - Run both implementations"
	@echo ""
	@echo "Development Commands:"
	@echo "  make debug           - Debug with GDB"
	@echo "  make memcheck        - Check memory leaks with Valgrind"
	@echo "  make analyze         - Static code analysis with cppcheck"
	@echo "  make format          - Format code with clang-format"
	@echo "  make assembly        - Generate assembly output"
	@echo ""
	@echo "Testing Commands:"
	@echo "  make test            - Run comprehensive tests"
	@echo "  make test-optimizations - Test different compiler optimizations"
	@echo "  make profile         - Run performance profiling"
	@echo ""
	@echo "Utility Commands:"
	@echo "  make clean           - Clean build artifacts"
	@echo "  make archive         - Create project archive"
	@echo "  make install-deps    - Install Python dependencies"
	@echo "  make stats           - Show project statistics"
	@echo "  make help            - Show this help message"
	@echo ""
	@echo "Examples:"
	@echo "  make && make run     - Build and run both versions"
	@echo "  make test            - Run all tests"
	@echo "  make debug           - Start debugging session"

# Quick demonstration
demo: compile
	@echo "🎬 ADD TWO NUMBERS - QUICK DEMONSTRATION"
	@echo "========================================"
	@echo ""
	@echo "This program solves LeetCode #2: Add Two Numbers"
	@echo "Problem: Add two numbers represented as linked lists"
	@echo ""
	@echo "Running C version with sample data..."
	@echo ""
	./$(TARGET)

.PHONY: all compile run-c run-python run debug memcheck profile analyze format test-optimizations assembly clean archive install-deps test stats help demo
