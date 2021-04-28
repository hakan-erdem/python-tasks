n = int(input("Enter the number: "))

is_prime = True

if n < 5:
    for i in range(2,n):
        if n % i == 0:
            is_prime = False

# for optimization we only look until the root of the number
# if we dont make an exception for the numbers below 5, the algorithm gives true for 4 which is wrong.
else:
    for i in range(2, int((n**1/2))):
        if n % i == 0:
            is_prime = False


if is_prime:
    print(f"{n} is a prime number")

else:
    print(f"{n} is not a prime number")