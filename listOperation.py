# 1. Accessing/Traversing the list
# shoppingList = ['Milk', 'Cheese', 'Butter']

# for i in range(len(shoppingList)):
#     shoppingList[i] = shoppingList[i] + "+"
#     print(shoppingList[i])

# 2. Update/ Insert - list
# myList = [1,2,3,4,5,6,7,]
# print(myList)
# # myList.insert(4, 15) O(n)

# newList = [11,12,13,14]
# myList.extend(newList) # O(n) 
# # myList.append(55) O(1)
# print(myList)

# 3. Using the slice operator
# myList = ['a','b','c','d','e','f']
# # myList.pop() time complexity is O(1)
# # del myList[2:4] Time complexity O(n)

# myList.remove('e') # Time complexity O(n)

# print(myList)

# # 4. Searching for an element in the list 
# my_list = [10,20,30,40,50,60,70,80,90]
# # in operator
# target = 90
# # if target in my_list:
# #     print(f"{target} is in the list")
# # else:
# #     print(f"{target} is not in the list")

# # Linear search (Time complexity is O(n))
# def linear_search(p_list, p_target):
#     for i, value in enumerate(p_list): # O(n)
#         if value == p_target: #O(1)
#             return i #O(1)
#     return -1

# print(linear_search(my_list, target))

# 5. List operations / functions
# a = [1,2,3,4,5,6,7,8,9]
# print(sum(a)/len(a))

# 6. Pitfalls and ways to avoid them 
# myList = [2,4,3,1,5,7]
# myList.append(10)
# myList = myList +[10]
# print(myList)

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]

# fruit_list2[0] ='Guava'
# fruit_list3[1] = 'Kiwi'

# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20

# print (sum)


a=[1,2,3,4,5]
print(a[3:0:-1])