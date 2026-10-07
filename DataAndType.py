import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array([1,2,3,4,5])

print(my_list[0])
print(my_list[1])
print(my_array[0])
print(my_array[1])


print("#" * 50)

print(id(my_list[0]))
print(id(my_list[1]))
print(id(my_array[0]))
print(id(my_array[1]))

print("#" * 50)

my_list_of_data = [1 ,2 ,"A" , "B" , True , 10.50]
my_array_of_data = np.array([1 ,2 ,"A" , "B" , True , 10.50])
print(my_list_of_data)
print(my_array_of_data)

print("#" * 50)



