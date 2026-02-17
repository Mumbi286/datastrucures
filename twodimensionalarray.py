# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11,5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9 

import numpy as np 

# 1. Displaying the array
print("Step 1")
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9 ]])
print(twoDArray)

# 2. Inserting two dimensional array 
# print("Step 2")
# newTwoDArray = np.insert(twoDArray, 1,[[1,2,3,4]], axis=0)
# print(newTwoDArray)

# #  Adding an element to the end of the two dimensional array 
# print("Step 3")
# newTwoDArray = np.append(twoDArray,[[1,2,3,4]], axis=0)
# print(newTwoDArray)

#3. Accessing an element in two dimensional  is a O(1) time complexity
# print("Step 3")
# def accessElements(array, rowIndex, colIndex):
#     if rowIndex >= len(array) and colIndex >= len(array[0]): #O(1)
#         print("Incorrect index") # O(1)
#     else:
#         print(array[rowIndex][colIndex]) # O(1)
# accessElements(twoDArray, 2, 3)

#  5. Travesing two dimensional array; space complexity is O(1) but the time complexity is O(n^ 2)
# print("Step 4")
# def traverseTDArray(array):  
#     for i in range(len(array)): # O(mn)
#         for j in range(len(array[0])): # O(n)
#             print(array[i][j]) # O(1)
# traverseTDArray(twoDArray)

# 6. Searching for an element in Two Dimensional Array  
# def searchTDArray(array, value):
#     for i in range(len(array)): # O(mn)
#         for j in range(len(array[0])): # O(n)
#             if array[i][j]== value: # O(1)
#                 return 'The value is located at index ' + str(i) + " " + str(j)
#     return 'The element is not found'

# print(searchTDArray(twoDArray, 55))

# 7. Deleting 2D dimensional Array 
#  deleting a column or row the time complexity wil be O(mn) and Space complexity will be O(mn) -- m its the number of columns and n is number of rows
print("Step 7")
newTDArray = np.delete(twoDArray, 1, axis = 1)
print(newTDArray) 