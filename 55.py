#A dictionary is a builit-in data structure in python that allow you to store
#a collection of key-value pairs.

#dictionary is multable and it is unordered

my_dict={
    "std_id":1233,
    "std_name":"sanjana",
    "course":"BCA"
}
print(my_dict)

#Accessing Elements
x=my_dict["course"]
print(x)
x=my_dict.get("std_name")
print(x)

#Get all the keys from specified dictionary
y=my_dict.keys()
print(y)

#To update particular value
my_dict.update({"std_name":"simran"})
print (my_dict)

#adding items in the dictionary
my_dict["fees"]=45000
print(my_dict)

my_dict["std_addr"]="nevi mumbai"
print(my_dict)
#removing iteam in the dictionary using pop()

my_dict.pop()
print(my_dict)

#looping over dictionary

for i in my_dict:
    print(i)

#looping over iteam in list 
for i in my_dict:
    print(my_dict[i])   

#looping by the method values()and keys()
print("use of keys()method")
for i in my_dict.values():
    print(i)

print("Use of keys()method")    
for i in my_dict.keys():
    print(i)    