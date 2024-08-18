# Print the solution to the Fizzbuzz game
# Rules of Fizzbuzz:
# Print each number from 1 to 100 in turn and include number 100
# Number is divisible by 3, print "Fizz"
# Number is divisible by 5, print "Buzz"
# Number is divisible by 3 and 5, print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)