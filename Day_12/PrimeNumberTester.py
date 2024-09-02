def is_prime(num):
    for number in range(2, num):
       if num % number == 0:
           return False
    return True

print(is_prime(int(input("Enter a number to test whether it is prime: "))))