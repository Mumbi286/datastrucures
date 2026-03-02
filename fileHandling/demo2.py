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
import json
import os 

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
save_user_data()


        


    



