# 📌 Python Data Types

Welcome to the **Data Types** module! Data types define the type of data a variable can store. Python automatically detects the type of variable based on the assigned value.

---

## 📖 Table of Contents

- [What is a Data Type?](#-what-is-a-data-type)
- [Overview of Built-in Data Types](#-overview-of-built-in-data-types)
- [Detailed Breakdown of Data Types](#-detailed-breakdown-of-data-types)
  - [1. Numeric Types (`int`, `float`, `complex`)](#1-numeric-types-int-float-complex)
  - [2. Text Type (`str`)](#2-text-type-str)
  - [3. Boolean Type (`bool`)](#3-boolean-type-bool)
  - [4. Sequence Types (`list`, `tuple`, `range`)](#4-sequence-types-list-tuple-range)
  - [5. Mapping Type (`dict`)](#5-mapping-type-dict)
  - [6. Set Types (`set`, `frozenset`)](#6-set-types-set-frozenset)
  - [7. None Type (`NoneType`)](#7-none-type-nonetype)
- [Checking Data Types](#-checking-data-types)
- [Mutable vs Immutable Data Types](#-mutable-vs-immutable-data-types)
- [Type Casting (Conversion)](#-type-casting-conversion)
- [Quick Code Examples](#-quick-code-examples)

---

## ❓ What is a Data Type?

In computer programming, a **data type** specifies the kind of value a variable holds and determines what operations can be performed on that value.

In Python:
- **Dynamically Typed**: You do not need to declare variable types manually. Python infers the type automatically at runtime.
- **Everything is an Object**: In Python, all data types are implemented as classes, and variables are instances of these classes.

---

## 📊 Overview of Built-in Data Types

| Category | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| **Numeric** | `int` | Whole numbers (positive or negative) | `22`, `-100` |
| **Numeric** | `float` | Numbers with decimal points | `5.9`, `3.14159` |
| **Numeric** | `complex` | Complex numbers with real and imaginary parts | `3 + 4j` |
| **Text** | `str` | Textual data enclosed in single or double quotes | `"Ubaid"`, `'Python'` |
| **Boolean** | `bool` | Logical truth values | `True`, `False` |
| **Sequence** | `list` | Ordered, mutable collection of items | `[1, 2, 3]` |
| **Sequence** | `tuple` | Ordered, immutable collection of items | `(1, 2, 3)` |
| **Sequence** | `range` | Sequence of numbers, often used in loops | `range(0, 5)` |
| **Mapping** | `dict` | Key-value pairs enclosed in curly braces | `{"name": "Ubaid", "age": 22}` |
| **Set** | `set` | Unordered collection of unique items | `{1, 2, 3}` |
| **Set** | `frozenset` | Immutable version of a `set` | `frozenset({1, 2})` |
| **None** | `NoneType` | Represents the absence of a value | `None` |

---

## 🔍 Detailed Breakdown of Data Types

### 1. Numeric Types (`int`, `float`, `complex`)

```python
# Integer (int)
age = 22
count = -50

# Float (float)
height = 5.9
pi = 3.14159

# Complex (complex)
z = 3 + 4j
```

### 2. Text Type (`str`)

Strings are immutable sequences of Unicode characters.

```python
name = "Ubaid"
greeting = 'Hello, World!'
multi_line = """This is a 
multi-line string."""
```

### 3. Boolean Type (`bool`)

Booleans represent one of two values: `True` or `False`.

```python
is_student = True
is_admin = False

# Booleans evaluated in conditionals
print(10 > 5)  # Output: True
```

### 4. Sequence Types (`list`, `tuple`, `range`)

```python
# List (Mutable - can be modified)
fruits = ["apple", "banana", "cherry"]

# Tuple (Immutable - cannot be modified after creation)
coordinates = (10.0, 20.0)

# Range (Generates a sequence of numbers)
numbers = range(1, 6)  # 1, 2, 3, 4, 5
```

### 5. Mapping Type (`dict`)

Dictionaries store data in `key: value` pairs.

```python
user = {
    "name": "Ubaid",
    "age": 22,
    "is_student": True
}

print(user["name"])  # Output: Ubaid
```

### 6. Set Types (`set`, `frozenset`)

Sets store unique, unordered elements (automatically removes duplicates).

```python
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # Output: {1, 2, 3, 4}
```

### 7. None Type (`NoneType`)

Used to define a null value or no value at all.

```python
result = None
```

---

## 🔬 Checking Data Types

You can check the data type of any object using Python's built-in `type()` function or `isinstance()` function.

```python
name = "Ubaid"
age = 22

# Using type()
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>

# Using isinstance() - recommended for conditional checks
print(isinstance(age, int))   # True
print(isinstance(name, str))  # True
```

---

## 🔒 Mutable vs Immutable Data Types

Understanding mutability is crucial in Python:

- **Mutable** (Can be modified after creation):
  - `list`, `dict`, `set`
- **Immutable** (Cannot be modified after creation):
  - `int`, `float`, `str`, `tuple`, `bool`, `frozenset`

```python
# Example: Lists are mutable
my_list = [1, 2, 3]
my_list[0] = 99  # Valid! my_list is now [99, 2, 3]

# Example: Strings are immutable
my_str = "Hello"
# my_str[0] = "J"  # ❌ TypeError: 'str' object does not support item assignment
```

---

## 🔄 Type Casting (Conversion)

You can convert from one data type to another using built-in functions:

```python
# Explicit Type Casting
x = 10         # int
y = float(x)   # 10.0 (float)
z = str(x)     # "10" (str)

num_str = "25"
num_int = int(num_str)  # 25 (int)
```

---

## 📁 Related Files

- Practice Code: [`main.py`](file:///c:/Users/Masjidal2026/Desktop/Learning-roadmaps/Python/data_types/main.py)

