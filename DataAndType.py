import numpy as np

# 1. Create a Python list and a NumPy array, then access their elements
my_list = [1, 2, 3, 4, 5]
my_array = np.array([1, 2, 3, 4, 5])

print(my_list[0])
print(my_list[1])
print(my_array[0])
print(my_array[1])

print("#" * 50)

# 2. Check the memory addresses (IDs) of the elements
# Lists store references to scattered objects in memory, while NumPy arrays store elements in a contiguous block.
print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_array[0]))
print(id(my_array[1]))

print("#" * 50)

# 3. Create a list and an array with mixed data types
# A Python list keeps the original data types. A NumPy array forces all elements into a single data type (upcasting to strings here).
my_list_of_data = [1 ,2 ,"A" , "B" , True , 10.50]
my_array_of_data = np.array([1 ,2 ,"A" , "B" , True , 10.50])
print(my_list_of_data)
print(my_array_of_data)

print("#" * 50)

# 4. Check the data type of the first element in the mixed data structures
# The list element remains an 'int', while the array element is converted to a string type (e.g., numpy.str_).
print(type(my_list_of_data[0]))
print(type(my_array_of_data[0]))

print("#" * 50)

# 5. Create a list and an array containing only integers
my_list_of_data_2 = [1, 2]
my_array_of_data_2 = np.array([1, 2])
print(my_list_of_data_2)
print(my_array_of_data_2)

print("#" * 50)

# 6. Check the data type of the first element in the integer structures
# Python uses the standard 'int' class, while NumPy uses specific size-based types (e.g., numpy.int32 or numpy.int64).
print(type(my_list_of_data_2[0]))
print(type(my_array_of_data_2[0]))
