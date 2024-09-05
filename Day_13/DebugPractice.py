def my_function():
    for i in range(1, 20):
        if i == 20: # i never reaches function because the range() function stops the loop at i=19
            print("You get it")

my_function()

# Describe the problem
# 1. What is the loop doing? - looping i from 1 to 19
# 2. When is the function meant to print "You got it!" - Once i reaches 20
# 3. What are your assumptions about the value of i? - that i will never actually reach the number 20.
# Solution - the range needs to be extended like so, range(1, 21)