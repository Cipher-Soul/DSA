# this is array in python
array = [3,4,5,5,6,84,3,2,2]
# output:[3,4,5,5,6,84,3,2,2]

# ways to access array elements
val_1 = array[0]
val_2 = array[1]
val_3 = array[2]
# output: 3,4,5

# Change value in array
array[0] = 99 #[99, 4, 5, 5, 6, 84, 3, 2, 2]

# replace value in array with method
array.insert(0,300) # insert num at index 0 :[300, 99, 4, 5, 5, 6, 84, 3, 2, 2]
#get index with method
print(array.index(5)) # return first index of value 5

#get lenght of array
lenght_of_array = len(array) # to find lenght of array take array variable as input 10

#to find occurence of value in array
occur = array.count(5) #input is value --> number of times it appear in array 2 

