import numpy as np

# =====================================================================
# 1. 1D Array Slicing (One-Dimensional Arrays)
# Slicing syntax: [Start:End:Steps]
# Note: The 'End' index is exclusive (it is NOT included in the result).
# =====================================================================
a = np.array(["A", "B", "C", "D", "E", "F"])

print(a.ndim)       # Output: 1 (Checks the number of dimensions)
print(a[1])         # Single Indexing: Access the element at index 1 ("B")

# Slicing Examples:
print(a[1:4])       # Get elements from index 1 to 3 (Index 4 is excluded) -> ["B", "C", "D"]
print(a[:4])        # Get elements from the beginning up to index 3 -> ["A", "B", "C", "D"]
print(a[2:])        # Get elements from index 2 all the way to the end -> ["C", "D", "E", "F"]

print("#" * 50)

# =====================================================================
# 2. 2D Array Slicing (Two-Dimensional Arrays / Matrices)
# Slicing syntax for 2D: [Row_Slice, Column_Slice]
# =====================================================================
b = np.array([
    ["A", "B", "X"],  # Row 0
    ["C", "D", "Y"],  # Row 1
    ["E", "F", "Z"],  # Row 2
    ["M", "N", "O"]   # Row 3
])

print(b.ndim)       # Output: 2 (Checks the number of dimensions)
print(b[1])         # Access an entire row: Gets the second row (Index 1) -> ["C", "D", "Y"]

print("#" * 50)

# =====================================================================
# 3. Extracting Sub-Matrices (Slicing Rows and Columns together)
# =====================================================================

# Get Rows: 0 to 2 (Index 3 is excluded)
# Get Columns: 0 to 1 (Index 2 is excluded)
print(b[0:3, 0:2])

print("#" * 50)

# Get Rows: from index 2 to the end (Rows 2 and 3)
# Get Columns: 0 to 1 (Index 2 is excluded)
print(b[2:, 0:2])

print("#" * 50)

# =====================================================================
# 4. Advanced 2D Slicing with Steps
# =====================================================================

# Get Rows: from index 2 to the end (Rows 2 and 3)
# Get Columns: from the beginning to index 1 (Index 2 is excluded), but with a STEP of 2.
# This means it will pick column 0, step over 1, and stop.
print(b[2:, :2:2])