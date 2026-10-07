import numpy as np

my_list = [1,2,3,4,5]
my_array = np.array(my_list)

print(my_list)
print(my_array)

print("#" * 50)

print(type(my_list))
print(type(my_array))

print("#" * 50)

print(my_list[0])
print(my_array[0])


a = np.array(10)
b = np.array([10,20])
c = np.array( [[1,2] , [3,4]])
d = np.array( [ [ [5,6 ],[7,9 ] ] , [ [1,3 ],[4,8 ] ] ])

print(d[1][1][1])
print(d[1,1,1])


print("#" * 50)


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

print("#" * 50)

my_cumstom_array = np.array([1,2,3] , ndmin=3)
print(my_cumstom_array)
print(my_cumstom_array.ndim)
print(my_cumstom_array[0,0,0])