# Makefile for Two Sum Problem Implementations
# Usage:
#   make          - Compile and run all implementations
#   make c        - Compile and run C implementation
#   make python   - Run Python implementation
#   make clean    - Clean compiled files
#   make help     - Show help

CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -O2
TARGET = two_sum
SOURCE = two_sum.c

# Default target
all: c python

# Compile and run C implementation
c: $(TARGET)
	@echo "🚀 Running C implementation..."
	@echo "================================"
	./$(TARGET)

# Compile C program
$(TARGET): $(SOURCE)
	@echo "🔨 Compiling C program..."
	$(CC) $(CFLAGS) $(SOURCE) -o $(TARGET)

# Run Python implementation
python:
	@echo "🐍 Running Python implementation..."
	@echo "===================================="
	python3 two_sum.py

# Performance comparison
benchmark: $(TARGET)
	@echo "⚡ Performance Benchmark"
	@echo "========================"
	@echo "Running C implementation:"
	time ./$(TARGET) > /dev/null
	@echo ""
	@echo "Running Python implementation:"
	time python3 two_sum.py > /dev/null

# Clean compiled files
clean:
	@echo "🧹 Cleaning up..."
	rm -f $(TARGET)

# Help target
help:
	@echo "Two Sum Problem - Build Instructions"
	@echo "===================================="
	@echo "Available targets:"
	@echo "  make          - Compile and run all implementations"
	@echo "  make c        - Compile and run C implementation"
	@echo "  make python   - Run Python implementation"
	@echo "  make benchmark- Compare performance of both implementations"
	@echo "  make clean    - Remove compiled files"
	@echo "  make help     - Show this help message"
	@echo ""
	@echo "Requirements:"
	@echo "  - GCC compiler for C code"
	@echo "  - Python 3.6+ for Python code"

# Declare phony targets
.PHONY: all c python benchmark clean help
