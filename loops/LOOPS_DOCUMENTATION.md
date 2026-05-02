# Loops Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Types of Loops](#types-of-loops)
3. [For Loops](#for-loops)
4. [While Loops](#while-loops)
5. [Loop Control Statements](#loop-control-statements)
6. [Nested Loops](#nested-loops)
7. [Best Practices](#best-practices)
8. [Common Patterns](#common-patterns)

## Introduction

A **loop** is a programming construct that allows you to repeat a block of code multiple times. Loops are fundamental to programming and help reduce code duplication, making programs more efficient and maintainable.

### Why Use Loops?
- Execute the same code block multiple times
- Process collections of data
- Automate repetitive tasks
- Iterate through sequences (lists, strings, etc.)

---

## Types of Loops

Python provides two main types of loops:

1. **For Loop** - Iterates a fixed number of times
2. **While Loop** - Repeats while a condition is true

---

## For Loops

### Syntax
```python
for variable in sequence:
    # Code to execute in each iteration
    statement(s)
```

### Basic Examples

#### Example 1: Loop Through a List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
**Output:**
```
apple
banana
cherry
```

#### Example 2: Loop Through a String
```python
for char in "Python":
    print(char)
```
**Output:**
```
P
y
t
h
o
n
```

#### Example 3: Using range()
```python
for i in range(5):
    print(i)
```
**Output:**
```
0
1
2
3
4
```

#### Example 4: range() with Start, Stop, Step
```python
for i in range(2, 10, 2):
    print(i)
```
**Output:**
```
2
4
6
8
```

### For Loop with else
```python
for i in range(5):
    print(i)
else:
    print("Loop completed successfully!")
```
The `else` block executes when the loop completes normally (without a `break` statement).

---

## While Loops

### Syntax
```python
while condition:
    # Code to execute while condition is true
    statement(s)
```

### Basic Examples

#### Example 1: Simple Counter
```python
count = 0
while count < 5:
    print(count)
    count += 1
```
**Output:**    
```
0
1
2
3
4
```

#### Example 2: User Input Loop
```python
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted!")
```

#### Example 3: While Loop with else
```python
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed!")
```

### Infinite Loops
**Warning:** Be careful not to create infinite loops!
```python
while True:
    # This will run forever unless you use break
    user_input = input("Type 'exit' to quit: ")
    if user_input == "exit":
        break
```

---

## Loop Control Statements

### 1. break
Terminates the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```
**Output:**
```
0
1
2
3
4
```

### 2. continue
Skips the current iteration and moves to the next one.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```
**Output:**
```
0
1
3
4
```

### 3. pass
Does nothing; used as a placeholder.

```python
for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    print(i)
```
**Output:**
```
0
1
2
3
4
```

---

## Nested Loops

A loop inside another loop. The inner loop completes all iterations for each iteration of the outer loop.

### Example 1: Multiplication Table
```python
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} × {j} = {i * j}")
```
**Output:**
```
1 × 1 = 1
1 × 2 = 2
1 × 3 = 3
2 × 1 = 2
2 × 2 = 4
2 × 3 = 6
3 × 1 = 3
3 × 2 = 6
3 × 3 = 9
```

### Example 2: Pattern Generation
```python
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()
```
**Output:**
```
* * *
* * *
* * *
```

---

## Best Practices

### 1. Use Descriptive Variable Names
```python
# Good
for student_name in students:
    print(student_name)

# Avoid
for s in students:
    print(s)
```

### 2. Keep Loops Simple
```python
# Good - clear logic
for number in numbers:
    if number > 0:
        positive_sum += number

# Avoid - complex logic inside loop
for n in numbers:
    if n > 0 and n < 100 and n % 2 == 0:
        # Complex processing
        pass
```

### 3. Use enumerate() for Index and Value
```python
# Instead of:
for i in range(len(items)):
    print(i, items[i])

# Use:
for index, item in enumerate(items):
    print(index, item)
```

### 4. Use zip() for Multiple Sequences
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### 5. Avoid Modifying Collections During Iteration
```python
# Avoid
for item in my_list:
    if condition:
        my_list.remove(item)

# Better - create new list
new_list = [item for item in my_list if not condition]
```

---

## Common Patterns

### Pattern 1: Sum All Elements
```python
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)  # Output: 15
```

### Pattern 2: Find Maximum Value
```python
numbers = [3, 7, 2, 9, 1]
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(max_val)  # Output: 9
```

### Pattern 3: Count Occurrences
```python
items = ["a", "b", "a", "c", "a"]
count = 0
for item in items:
    if item == "a":
        count += 1
print(count)  # Output: 3
```

### Pattern 4: Filter Elements
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)  # Output: [2, 4, 6]
```

### Pattern 5: Transform Elements
```python
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)  # Output: [1, 4, 9, 16, 25]
```

---

## List Comprehension (Alternative to Loops)

Python provides a concise way to create lists using loops:

```python
# Traditional loop
squared = []
for num in range(5):
    squared.append(num ** 2)

# List comprehension (more concise)
squared = [num ** 2 for num in range(5)]
```

**Output:** `[0, 1, 4, 9, 16]`

### With Conditions
```python
# Filter even numbers
even_nums = [num for num in range(10) if num % 2 == 0]
print(even_nums)  # Output: [0, 2, 4, 6, 8]
```

---

## Summary

| Concept | Use Case |
|---------|----------|
| **For Loop** | When you know the number of iterations |
| **While Loop** | When you need to repeat until a condition changes |
| **break** | Exit loop prematurely |
| **continue** | Skip to next iteration |
| **Nested Loops** | Process multi-dimensional data |
| **List Comprehension** | Create filtered/transformed lists concisely |

---

## Tips for Debugging Loops

1. **Check loop conditions** - Ensure the condition will eventually be false
2. **Print intermediate values** - Use print statements to track loop progress
3. **Verify loop bounds** - Ensure you're iterating the correct range
4. **Count iterations** - Use a counter to track how many times the loop runs
5. **Test edge cases** - Check behavior with empty lists, single items, etc.

---

**Happy Looping! 🔄**
