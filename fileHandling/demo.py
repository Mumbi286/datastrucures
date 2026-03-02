# #1. Opening this file in python 
# file = open('data.txt','r') #object
# # Reading data in a file 
# content = file.readline()
# print(content)
# # Closing the file 
# file.close()

# 2.Writing & Appending Data to a file
# Writing to data.txt
# file = open('data.txt', 'w')
# file.write('New content to be added to file')
# file.close()

# #3. Appending data 
# file = open('data.txt', 'a')
# content = '\nThis is a third line'
# file.write(content)
# file.close()

# 4. Opening Files using with
# with open('data.txt','r') as file:
#     contents = file.read()
#     print(contents)

# 5. readline and  readlines 
# with open('data.txt','r') as file:
#     line1 = file.readline()
#     line2 = file.readline()

# print(line2)

#6. Readine all lines in the data.txt
# with open('data.txt','r') as file:
#     lines = file.readlines()
# print(lines)
# for line in lines:
#     print(line.strip())

# 7. Saving User data in A File 
while True:

    with open('data.txt', "a") as file:
        name = input("Enter name to be added: ")
        file.write(name+'\n')
        choice = input("Do you want to add more names? (y/n)")
        if choice == 'n':
            break

# 8. Reading Saved names
with open("data.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip().capitalize()) # Removing white spacas and capitaizing






