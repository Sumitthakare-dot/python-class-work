# # my_dict = {"name": "alice", "age": 25}
# # if "name"in my_dict:
# #     print("Key exists")
# # else:
# #     print("Key does not exist")


#Get the Value for a Key

# my_dict ={"name": "Alice","age": 25}
# print(my_dict.get("name"))


#Iterate Over Dictionary Keys
# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# for Key in my_dict:
#     print(Key)



#Iterate Over Dictionary Values
# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# for value in my_dict.values():
#     print(value)



#Iterate Over Dictionary Items (Key-Value Pairs)
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in my_dict.items():
    print(f"{key}: {value}")
