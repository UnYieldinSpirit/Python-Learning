# these whole numbers are viewed as strings, meaning they don't get added together but the get concatenated instead
print("123" + "456")

# this allows you to change the datatype of whatever data type you initially had, if applicable.
# like letters can not be converted to integers since they are not numbers at all
print(int("123"))

#v fix and improve the code below: v
# print("Number of letters in your name: " + len(input("Enter your name")))

user_name = input("What is your name?\n") #str
user_name_length = len(user_name) #int
print("Number of letters in your name: " + str(user_name_length)) #convert back to string in order to concatenate