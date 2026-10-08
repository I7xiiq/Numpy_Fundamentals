import numpy as np

# =====================================================================
# 1. Arithmetic Operations (Element-wise Operations)
# NumPy performs arithmetic operations (addition, subtraction, multiplication, division) 
# element by element. This is much faster than using standard Python loops.
# =====================================================================

# 1D Arrays Arithmetic
my_array1 = np.array([10, 20, 30])
my_array2 = np.array([5, 2, 4])

print("1D Addition:", my_array1 + my_array2)
print("1D Subtraction:", my_array1 - my_array2)
print("1D Multiplication:", my_array1 * my_array2)
print("1D Division:", my_array1 / my_array2)

print("#" * 50)

# 2D Arrays Arithmetic (Matrices)
# The exact same logic applies to 2D matrices, operating on matching positions.
my_array3 = np.array([[1, 4], [5, 9]])
my_array4 = np.array([[2, 7], [10, 5]])

print("2D Addition:\n", my_array3 + my_array4)
print("2D Subtraction:\n", my_array3 - my_array4)
print("2D Multiplication:\n", my_array3 * my_array4)
print("2D Division:\n", my_array3 / my_array4)

print("#" * 50)

# =====================================================================
# 2. Aggregation Functions (Min, Max, Sum)
# These methods scan the entire array and return a single scalar value.
# Note: For 2D arrays, if no 'axis' is specified, it treats the array as 1D.
# =====================================================================

# Aggregations on 1D Arrays
my_array5 = np.array([10, 20, 30])
print("1D Min:", my_array5.min())
print("1D Max:", my_array5.max())
print("1D Sum:", my_array5.sum())

print("#" * 50)

# Aggregations on 2D Arrays
my_array6 = np.array([[6, 4], [3, 9]])
print("2D Min (Overall):", my_array6.min())
print("2D Max (Overall):", my_array6.max())
print("2D Sum (Overall):", my_array6.sum())

print("#" * 50)

# =====================================================================
# 3. Flattening Arrays using ravel()
# ravel() converts multi-dimensional arrays (2D, 3D, etc.) into a flat 1D array.
# This is a crucial step in Computer Vision and AI before feeding image matrices 
# or tensors into machine learning models.
# =====================================================================

# Flattening a 2D Array
my_array7 = np.array([[6, 4], [3, 9]])
print("Flattened 2D array:", my_array7.ravel())

# Flattening a 3D Array (Tensor)
my_array8 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Dimensions of original array:", my_array8.ndim)
print("Flattened 3D array:", my_array8.ravel())

print("#" * 50)

# =====================================================================
# 4. Basic Statistical Functions on a 1D Array
# These functions are the core of data analysis and machine learning.
# =====================================================================
data = np.array([12, 45, 67, 89, 34, 55, 23, 90, 11])

print("Original Data:", data)
print("#" * 50)

# Mean (Average)
# np.mean() calculates the arithmetic average (sum of elements / count).
print("Mean (Average):", np.mean(data))

print("#" * 50)

# Median
# np.median() finds the exact middle value if the array was sorted. 
# It is very useful in AI because it is not affected by extreme outliers.
print("Median Value:", np.median(data))

print("#" * 50)

# Standard Deviation
# np.std() measures how spread out the numbers are from the mean.
# A low standard deviation means data is clustered around the average.
print("Standard Deviation:", np.std(data))