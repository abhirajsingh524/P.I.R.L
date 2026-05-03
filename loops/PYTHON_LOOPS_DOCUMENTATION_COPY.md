# Python Loops Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Integration Techniques](#integration-techniques)
3. [Dynamic Techniques](#dynamic-techniques)
4. [For Loops](#for-loops)
5. [While Loops](#while-loops)
6. [Loop Control Statements](#loop-control-statements)
7. [Nested Loops](#nested-loops)
8. [Best Practices](#best-practices)
9. [Common Patterns](#common-patterns)
10. [List Comprehension](#list-comprehension)
11. [Summary](#summary)

## Introduction

In Python, loops let you repeat code until a condition changes or until you finish iterating over a sequence. Writing loops with integration and dynamic techniques helps make Python programs more flexible, reusable, and easy to maintain.

---

## Integration Techniques

Integration techniques show how loops work together with functions, data structures, generators, and external sources.

### 1. Integrating Loops with Functions
Wrap loop logic in functions so you can reuse it across your program.

```python
def normalize_scores(scores):
    total = sum(scores)
    normalized = []
    for score in scores:
        normalized.append(score / total)
    return normalized

print(normalize_scores([50, 75, 100]))
```

### 2. Integrating Loops with Data Structures
Use loops to process dictionaries, sets, lists, and tuples.

```python
grades = {"Alice": 88, "Bob": 92, "Charlie": 79}
for student, grade in grades.items():
    print(f"{student} scored {grade}")
```

### 3. Integrating Loops with Generators
Generators let you loop over values one at a time without storing the entire sequence.

```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for number in fibonacci(6):
    print(number)
```

### 4. Integrating Loops with External Data
Read from files and process the content line by line.

```python
with open("data.txt") as file:
    for line in file:
        print(line.strip())
```

### 5. Integrating Loops with Higher-Level Tools
Use `enumerate`, `zip`, and comprehensions to make loops clearer.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for index, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{index}. {name}: {score}")
```

---

## Dynamic Techniques

Dynamic techniques make loop behavior depend on runtime values and changing conditions.

### 1. Dynamic Iteration Counts
Choose how many times to loop based on user input or computed values.

```python
n = int(input("How many items? "))
items = []
for _ in range(n):
    items.append(input("Enter item: "))
print(items)
```

### 2. Dynamic Loop Conditions
Use conditions that update inside the loop.

```python
balance = 100
while balance > 0:
    withdrawal = int(input("Withdraw amount: "))
    if withdrawal <= balance:
        balance -= withdrawal
    else:
        print("Not enough funds")
    if balance == 0:
        print("Account empty")
```

### 3. Dynamic Sequence Selection
Select the sequence to iterate based on runtime inputs or program state.

```python
data_type = input("Choose data type (numbers/letters): ")
sequence = range(5) if data_type == "numbers" else "abcde"
for item in sequence:
    print(item)
```

### 4. Dynamic Nested Loops
Build loop depth and structure from dynamic data like grids, tables, or nested lists.

```python
grid = [[1, 2], [3, 4], [5, 6]]
for row in grid:
    for value in row:
        print(value, end=" ")
    print()
```

### 5. Dynamic Output Patterns
Change output formatting or behavior during the loop.

```python
for i in range(1, 6):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
```

---

## For Loops

### Syntax
```python
for variable in sequence:
    statement(s)
```

### Examples

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

```python
for i in range(5):
    print(i)
```

### For Loop with else
```python
for i in range(5):
    print(i)
else:
    print("Finished loop")
```

---

## While Loops

### Syntax
```python
while condition:
    statement(s)
```

### Examples

```python
count = 0
while count < 3:
    print(count)
    count += 1
```

### Infinite Loop Pattern
```python
while True:
    command = input("Enter command (quit to exit): ")
    if command == "quit":
        break
```

---

## Loop Control Statements

### break
Stop the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### continue
Skip the rest of the current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

### pass
Use as a placeholder when no action is needed.

```python
for i in range(5):
    if i == 2:
        pass
    print(i)
```

---

## Nested Loops

Use nested loops when working with tables, grids, or multi-dimensional data.

```python
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in grid:
    for value in row:
        print(value, end=" ")
    print()
```

---

## Best Practices

- Use descriptive variable names
- Keep each loop focused on one task
- Prefer `enumerate` over `range(len(...))`
- Avoid modifying a list while iterating over it
- Use comprehensions when code is simple and readable

---

## Common Patterns

### Sum Elements
```python
values = [1, 2, 3, 4]
total = 0
for value in values:
    total += value
print(total)
```

### Filter Elements
```python
numbers = [1, 2, 3, 4, 5]
evens = [x for x in numbers if x % 2 == 0]
print(evens)
```

### Pair Sequences
```python
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
```

---

## List Comprehension

A concise way to create lists from loops.

```python
squares = [x**2 for x in range(6)]
print(squares)
```

With filters:

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)
```

---

## Summary

Python loops are powerful when combined with integration techniques and dynamic runtime logic. Use functions, generators, data structures, and runtime conditions to create robust and reusable loop-based programs.
