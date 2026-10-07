import numpy as np
import time
import sys

# 1. Setup Data: Define the number of elements for our performance test
# We create two standard Python ranges and two NumPy arrays of the exact same size.
elements = 1500

my_list1 = range(elements)                      
my_list2 = range(elements)

print("#" * 50)

my_array1 = np.arange(elements)
my_array2 = np.arange(elements)

print("#" * 50)

# 2. Performance Test: Standard Python Lists
# Measuring the execution time to add two lists element-by-element.
# Python requires a loop (list comprehension with zip) to iterate through and add each element, which is relatively slow.
list_start = time.time()
list_result = [(n1 + n2) for n1, n2 in zip(my_list1, my_list2)]
print(f"list time: {time.time() - list_start}")
# print(list_result)

print("#" * 50)

# 3. Performance Test: NumPy Arrays
# Measuring the execution time to add two NumPy arrays.
# NumPy uses "Vectorization" and underlying optimized C code to add the arrays instantly without explicit Python loops.
array_start = time.time()
array_result = my_array1 + my_array2
print(f"array time: {time.time() - array_start}")
# print(array_result)

print("#" * 50)

# 4. Memory Usage Test: NumPy Arrays
# NumPy stores elements as raw, contiguous data types (e.g., int32 or int64).
# 'itemsize' gets the bytes per element, and 'size' gets the total number of elements.
my_array = np.arange(100)

print(my_array)
print(my_array.itemsize)
print(my_array.size)
print(f"All bytes (NumPy Array): {my_array.itemsize * my_array.size}")

print("#" * 50)

# 5. Memory Usage Test: Standard Python Lists
# A Python integer is an object with extra metadata, consuming much more memory (usually 28 bytes) than a raw NumPy integer.
# We calculate the total memory by multiplying the size of one Python integer by the total number of elements.
my_list = list(range(100)) # Corrected: Created an actual Python list instead of a NumPy array

print(sys.getsizeof(1))
print(len(my_list))
print(f"All bytes (Python List): {sys.getsizeof(1) * len(my_list)}")