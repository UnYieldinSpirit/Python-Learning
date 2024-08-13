# Variable - just like the other languages, but the variable in Python are interpreted...
# meaning that you don't have to define the variable type since it is interpreted at runtime.
name = input("What is your name?")
print(name)

#len() function returns the length of a string, includes spaces:
print(len(name))

#Better to store information as variables then to continuously call functions over and over again.
username = input("What is your name?")
length = len(username)
print(length)
 # ^That^ is much cleaner than this:
print(len(input("What is your name?")))