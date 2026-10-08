import numpy as np

#slicing => [start:End:steps] Not including End

a = np.array(["A" , "B" , "C" , "D" , "E" , "F"])

print (a.ndim)
print(a[1])
print(a[1:4]) #Slicing
print(a[:4]) #Slicing
print(a[2:]) #Slicing

print("#" * 50)

b = np.array([["A", "B" , "X"],["C", "D" , "Y"],["E", "F" , "Z"],["M", "N" , "O"]])

print (b.ndim)
print(b[1])

print("#" * 50)

print(b[0:3 , 0:2])

print("#" * 50)

print(b[2: , 0:2])

print("#" * 50)

print(b[2: , :2:2])

