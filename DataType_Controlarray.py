import numpy as np

# =====================================================================
# 1. Checking Default Data Types
# NumPy automatically detects the data type of the array elements.
# Integers default to int32/int64, floats to float64, and strings to Unicode.
# For strings, 'U' is followed by the length of the longest string in the array.
# =====================================================================
my_array1 = np.array([1, 2, 3])
my_array2 = np.array([1.5, 20.15, 3.601])
my_array3 = np.array(["ah", "m", "ahmed"]) # 'U5' because 'ahmed' has 5 characters

print(my_array1.dtype)
print(my_array2.dtype)
print(my_array3.dtype)

print("#" * 50)

# =====================================================================
# 2. Creating Arrays with Specific Data Types
# You can force a specific data type using the 'dtype' argument during creation.
# You can use shorthand codes like 'f' for float32 or 'i' for int32.
# =====================================================================
my_array4 = np.array([1, 2, 3], dtype="f")           # Forces integers to become floats
my_array5 = np.array([1.5, 20.15, 3.601], dtype="i") # Forces floats to integers (truncates decimals)

# Note: Attempting to convert alphabetical strings to integers will raise a ValueError.
# my_array6 = np.array(["ah", "m", "ahmed"], dtype="i") # This will crash the program

print(my_array4.dtype)
print(my_array5.dtype)

print("#" * 50)

# =====================================================================
# 3. Changing the Data Type of an Existing Array (Casting)
# Use the 'astype()' method to create a copy of the array cast to a new type.
# =====================================================================
my_array7 = np.array([0, 1, 2, 3, 0, 4])
print(my_array7.dtype)
print(my_array7)

# Convert integer array to float array
my_array7 = my_array7.astype('float')
print(my_array7.dtype)
print(my_array7)

print("#" * 50)

# Convert float array to boolean array
# Boolean Rule: 0 or 0.0 becomes False, while any other non-zero number becomes True.
my_array7 = my_array7.astype('bool')
print(my_array7.dtype)
print(my_array7)

print("#" * 50)

# =====================================================================
# 4. Testing Memory Capacity (Item Size)
# Different data types consume different amounts of memory.
# 'itemsize' returns the number of bytes that one single array element consumes.
# =====================================================================

# Using the shorthand 'f' usually defaults to float32 (which takes 4 bytes per element)
my_array8 = np.array([100, 200, 300, 400], dtype="f")
print(my_array8.dtype)
print(my_array8[0].itemsize) # Output: 4 bytes

# Using 'float' (or np.float64) explicitly allocates more memory (8 bytes per element)
my_array8 = np.array([100, 200, 300, 400], dtype='float')
print(my_array8.dtype)
print(my_array8[0].itemsize) # Output: 8 bytes