# 📌 Python Variables & Naming Conventions

Welcome to the **Variables** module! This guide covers what variables are in Python, how to create them, the strict rules for naming them, and the recommended PEP 8 naming conventions.

---

## 📖 Table of Contents

- [What is a Variable?](#-what-is-a-variable)
- [Creating Variables in Python](#-creating-variables-in-python)
- [Rules for Naming Variables in Python](#-rules-for-naming-variables-in-python)
- [Variable Naming Conventions (Case Styles)](#-variable-naming-conventions-case-styles)
- [Best Practices](#-best-practices)
- [Quick Examples](#-quick-examples)

---

## ❓ What is a Variable?

A **variable** is a named container or reference used to store data in computer memory. Think of a variable as a labeled box where you can store a value (like a number, text, or list) and retrieve or update it later in your code.

In Python:
- You don't need to specify the data type explicitly (Python is **dynamically typed**).
- A variable is automatically created the moment you assign a value to it using the assignment operator (`=`).

---

## ✍️ Creating Variables in Python

To create a variable, specify the variable name followed by the `=` operator and the value:

```python
# Creating variables
name = "Ubaid Naeem"  # String (text)
age = 22             # Integer (whole number)
height = 5.9         # Float (decimal number)
is_student = True    # Boolean (True/False)

# Printing variables
print(name)
print(age)
```

### Dynamic Re-assignment
Variables in Python can change their type and value at any time:

```python
x = 10       # x is an integer
x = "Hello"  # x is now a string
```

---

## 🚫 Rules for Naming Variables in Python

Python has strict **syntax rules** for variable names. If you break these rules, Python will throw a `SyntaxError`.

| Rule | Valid Example | Invalid Example |
| :--- | :--- | :--- |
| Must start with a **letter** or an **underscore (`_`)**. | `user_name`, `_age` | `1user` |
| Cannot start with a **number**. | `item1`, `total2` | `2total` |
| Can only contain **alphanumeric characters** (`a-z`, `A-Z`, `0-9`) and **underscores (`_`)**. | `student_id`, `age_2026` | `user-name`, `total$` |
| **Case-sensitive** (`age`, `Age`, and `AGE` are 3 different variables). | `age = 20`, `Age = 25` | N/A |
| Cannot use **Python reserved keywords** (e.g., `if`, `for`, `class`, `def`, `import`). | `my_class` | `class` |

### Reserved Keywords in Python
Avoid using built-in keywords as variable names:
> `False`, `None`, `True`, `and`, `as`, `assert`, `async`, `await`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, `yield`

---

## 🔤 Variable Naming Conventions (Case Styles)

Conventions are community-agreed guidelines for writing clean, readable code. Python follows the **PEP 8** style guide.

### 1. `snake_case` (Python Standard ⭐)
- All letters are lowercase, and words are separated by underscores.
- **Used for**: Variable names, function names, module names.
```python
user_name = "Ubaid"
total_item_count = 15
is_logged_in = True
```

### 2. `camelCase`
- Starts with a lowercase letter, and every subsequent word starts with a capital letter.
- **Used for**: Common in JavaScript/Java (less common in standard Python).
```python
userName = "Ubaid"
totalItemCount = 15
```

### 3. `PascalCase` (Capitalized Words)
- Every word starts with a capital letter.
- **Used for**: Class names in Python.
```python
UserProfile = "Class structure"
StudentRecord = "Data structure"
```

### 4. `UPPER_CASE_SNAKE_CASE`
- All letters are uppercase, separated by underscores.
- **Used for**: Constants (values that should not change throughout the program).
```python
PI = 3.14159
MAX_CONNECTIONS = 100
DATABASE_URL = "localhost:5432"
```

---

## 💡 Best Practices

1. **Use Meaningful & Descriptive Names**:
   ```python
   # ❌ Poor naming (unclear)
   n = "Ubaid"
   a = 22
   
   # ✅ Good naming (descriptive)
   user_name = "Ubaid"
   user_age = 22
   ```

2. **Keep names concise but clear**:
   ```python
   # ❌ Too long
   name_of_the_person_who_is_currently_logged_in = "Ubaid"
   
   # ✅ Clear & concise
   logged_in_user = "Ubaid"
   ```

3. **Follow PEP 8**: Stick to `snake_case` for variable names in Python!

---

## 📁 Related Files

- Practice Code: [`main.py`](file:///c:/Users/Masjidal2026/Desktop/Learning-roadmaps/Python/variables/main.py)

