import numpy as np

# 1. Create a standard Python list and convert it to a NumPy array
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)

print(my_list)
print(my_array)

print("#" * 50)

# 2. Compare the data types of a Python list and a NumPy array
print(type(my_list))
print(type(my_array))

print("#" * 50)

# 3. Access the first element (index 0) in both the list and the array
print(my_list[0])
print(my_array[0])

print("#" * 50)

# 4. Create arrays with different dimensions (0-D, 1-D, 2-D, and 3-D)
a = np.array(10)                                          # 0-D array (Scalar)
b = np.array([10, 20])                                    # 1-D array (Vector)
c = np.array([[1, 2], [3, 4]])                            # 2-D array (Matrix)
d = np.array([[[5, 6], [7, 9]], [[1, 3], [4, 8]]])        # 3-D array (Tensor)

# 5. Access an element in a 3-D array using two different syntaxes
print(d[1][1][1])
print(d[1, 1, 1])

print("#" * 50)

# 6. Check the number of dimensions for each array using the 'ndim' attribute
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("#" * 50)

# 7. Create an array and explicitly set a minimum number of dimensions using 'ndmin'
my_cumstom_array = np.array([1, 2, 3], ndmin=3)
print(my_cumstom_array)
print(my_cumstom_array.ndim)
print(my_cumstom_array[0, 0, 0])