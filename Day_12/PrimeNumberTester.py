def is_prime(num):
    divisible_by = [1]
    prime = True

    for number in range(2, num):
       if num % number == 0:
           divisible_by.append(number)
           prime = False
    divisible_by.append(num)
    print(f"Divisible by: {divisible_by}")
    return prime

user_num = int(input("Enter a number to test if it is prime: "))

if is_prime(user_num):
    print(f"{user_num} is prime!")
else:
    print(f"{user_num} is not prime!")