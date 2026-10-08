import numpy as np

# =====================================================================
# 1. Understanding Array Dimensions (ndim) and Shape (shape)
# - ndim: Returns the number of dimensions (axes) the array has.
# - shape: Returns a tuple showing the size of the array in each dimension.
# Understanding shapes is crucial in AI and Computer Vision to ensure 
# matrix multiplications and image processing functions work correctly.
# =====================================================================

# 1D Array (Vector)
# A simple list of 4 elements. 
# The shape is (4,), meaning 1 axis with 4 elements.
my_array1 = np.array([1, 2, 3, 4])
print("1D ndim:", my_array1.ndim)
print("1D shape:", my_array1.shape)

print("#" * 50)

# 2D Array (Matrix)
# A grid containing 3 rows and 4 columns.
# The shape is (3, 4).
my_array2 = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
print("2D ndim:", my_array2.ndim)
print("2D shape:", my_array2.shape)

print("#" * 50)

# 3D Array (Tensor)
# Consists of 2 main blocks, each containing 2 rows and 5 columns.
# The shape is (2, 2, 5). In Computer Vision, a color image is often 
# represented exactly like this: (Color Channels, Height, Width).
my_array3 = np.array([[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]])
print("3D ndim:", my_array3.ndim)
print("3D shape:", my_array3.shape)

print("#" * 50)

# =====================================================================
# 2. Reshaping Arrays using reshape()
# Reshaping changes the structure of the data without changing the data itself.
# IMPORTANT RULE: The total number of elements must remain exactly the same.
# (e.g., you can reshape 12 elements into 2x6, 3x4, or 4x3, but not 5x2).
# =====================================================================

# Original 1D array with 12 elements
my_array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print("Original ndim:", my_array4.ndim)
print("Original shape:", my_array4.shape)

# Reshaping from 1D to 2D
# We are transforming the 12 elements into a matrix of 2 rows and 6 columns.
reshaped_array4 = my_array4.reshape(2, 6)
print("Reshaped ndim:", reshaped_array4.ndim)
print("Reshaped shape:", reshaped_array4.shape)
print("Reshaped Array:\n", reshaped_array4)

print("#" * 50)

# Original 2D array with shape (2, 10) -> Total of 20 elements
my_array5 = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print("Original 2D ndim:", my_array5.ndim)
print("Original 2D shape:", my_array5.shape)

print("#" * 50)

# Reshaping from 2D to 3D
# - reshape(-1) is a shortcut that completely flattens the array back into 1D.
# - reshape(4, 5) would organize the 20 elements into 4 rows and 5 columns.

# Here, we transform the 20 elements into a 3D tensor: 2 blocks, 5 rows, 2 columns.
# (2 * 5 * 2 = 20 elements).
reshaped_array5 = my_array5.reshape(2, 5, 2) 
print("Reshaped 3D ndim:", reshaped_array5.ndim)
print("Reshaped 3D shape:", reshaped_array5.shape)      
print("Reshaped 3D Array:\n", reshaped_array5)