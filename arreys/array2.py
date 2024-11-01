# Insert an Element 
def Insert_at_index(arr,totleSize,real_size,index,element):
   p1 = real_size-1
   p2 = real_size

   while p1 == index:
      arr[p2] = arr[p1]
   arr[index] = element
   return arr


# Append
def arr_Append(arr,):
   
#static array --Fixed Size
arr = [10,20,40,50,6,None,None]
totleSize = 7
real_size = 5
#Calling insert Function
print(arr)
Insert_at_index(arr,totleSize,real_size,1,9999)
print(arr)
#To access array at index -O(1)
print(arr[2])

# Update an Element--o(1)
arr[0] = 0


