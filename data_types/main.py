name = "Ubaid"
age = 22
is_student = True
height = 5.9
# ===== Basic Data Types =====
name = "Ubaid"       # String (str)
age = 22             # Integer (int)
is_student = True    # Boolean (bool)
height = 5.9         # Float (float)

print(type(name))
print(type(age))
print(type(is_student))
print(type(height))
# ===== Checking Data Types using type() =====
print("--- Checking Data Types ---")
print(name, "->", type(name))
print(age, "->", type(age))
print(is_student, "->", type(is_student))
print(height, "->", type(height))

# ===== Checking Data Types using isinstance() =====
print("\n--- Using isinstance() ---")
print("Is age an integer?", isinstance(age, int))
print("Is name a string?", isinstance(name, str))

# ===== Basic Type Casting (Conversion) =====
print("\n--- Type Casting Examples ---")
age_as_str = str(age)
print("Age as string:", age_as_str, type(age_as_str))

height_as_int = int(height)
print("Height converted to integer:", height_as_int, type(height_as_int))