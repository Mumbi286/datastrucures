# # 1. Lambda functions in Python
# result = (lambda  x,y: x+y)(2,3) 
# print(result)

# # 2. map in python are preferred due to memory efficiency
# numbers = [1,2,3,4,5]

# def square(x):
#     return x*x

# new_list = list(map(square, numbers))
# print(new_list)

# # 3. Using Map in different ways 
# # coverting from list to integer
# numbers = ["1","2","3","4","5"]

# new_list = list(map(int, numbers))
# print(new_list)

# # 4.
# prices = [100,200,300,400,500]
# new_prices = list(map(lambda x: x - x*5/100, prices))
# print(new_prices)

# # 5. Capitalization 
# names = ['john', 'rob', 'mike']
# cap_names = list(map(str.upper, names))
# print(cap_names)

# numbers = [1,2,3,4,5,6,7,8,9,10]

# odd_numbers = list(filter(lambda x: x%2==1, numbers))
# print(odd_numbers)

# # 6.Extracting Intials From Names
# names = ["John Doe", "Alice Smith", "Bob Ford"]
# for name in names:
#     print(name.split()[0][0] + name.split()[1][0])


# # 7. Extracting the names using map function  
# names = ["John Doe", "Alice Smith", "Bob Ford"]
# initials = list(map(lambda name: [n[0]for n in name.split()], names))
# print(initials)


# fruit = ['a','p','p','l','e']
# print("".join(fruit))



