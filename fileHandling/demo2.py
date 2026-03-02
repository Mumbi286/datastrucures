# # 1. Saving Complex data
# def save_user_data():
#     name = input ("Enter name")
#     email = input ("Enter email")
#     contact = input("Enter contact")

#     user_data = f"Name: {name}\nEmail:{email}\nContact: {contact}\n"
#     with open("data2.txt", "a") as file:
#         file.write(user_data)
# save_user_data()

# # 2. Reading the data from data2.txt
# def read_user_data():
#     with open("data2.txt", "r") as file:
#         print(file.read())
# read_user_data()

# # 3. Seriliazation - Is the process of converting a data sructure or object state into a format that can be stored or transmitted and then reconstructed later in the original form. 
# import json

# data = {
#     "name" : "John Doe",
#     "age" : 30,
#     "city": "New York"
# }
# json_data = json.dumps(data)
# print(type(json_data))
# print(type(data))

# # 4. Deserialization 
# import json 
# json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'

# data = json.loads(json_data)
# print(type(data))
# print(data["name"])
# print(data["age"])
# print(data["city"])

#5. Writing Serialised Data to file
#  Perfoming CRUD operation
import json
import os 

#  1. Saving user data 
def save_user_data():
    user_list=[]

    while True:
        name = input("Enter name ('or quit' to exit the program): ")
        if name == 'quit':
            break
        email = input ("Enter email ")
        contact = input("Enter contact")

        # Creating a dictionary
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }

        user_list.append(user_data)

    # Checking if the file exists and preserving the old data into data2.json
    if os.path.exists("data2.json"):
        with open("data2.json", "r") as file:
            existing_data = json.load(file)
        user_list.extend(existing_data)

    with open("data2.json", "w") as file:
        json.dump(user_list, file)

    print("User data saved successfully")

# 2. To view the user data 
def read_user_data():
    if not os.path.exists("data2.json"):
        print("No user data found")
        return
    
    with open("data2.json", "r") as file:
        user_list = json.load(file)
        for user_data in user_list:
            print("Name : ", user_data["name"])
            print("Email : ", user_data["email"])
            print("Contact : ", user_data["contact"])
            print("\n")



#3. Editing user's data fron data.json file 
def edit_user_data(name):
    if not os.path.exists("data2.json"):
        print("No user data found")
        return

    with open('data2.json','r') as file:
        user_list = json.load(file)


    user_found = False
    for user_data in user_list:
        if user_data['name'].lower() == name.lower():
            email = input("Enter updated email: ")
            contact = input("Enter updated contact: ")

            user_data["email"] = email
            user_data["contact"] = contact
            user_found = True 
            break

    if not user_found:
        print("User not found ")
    
    with open("data2.json", "w") as file:
        json.dump(user_list,file)
    print("User data updated successfully!")

# 4. Deleting user function 
def delete_user_data(name):
    if not os.path.exists("data2.json"):
        print("No user data found")
        return

    with open('data2.json','r') as file:
        user_list = json.load(file)


    user_found = False
    for user_data in user_list:
        if user_data['name'].lower() == name.lower():
            user_list.remove(user_data)
            user_found = True 
            break

    if not user_found:
        print("User not found ")
    
    with open("data2.json", "w") as file:
        json.dump(user_list,file)
    print("User data deleted successfully!")
    

# edit_name = input("Enter name which you want to edit data for: ")
# edit_user_data(edit_name)
# read_user_data()

delete_name = input("Enter name which you want to delete: ")
delete_user_data(delete_name)
read_user_data()


        


    



