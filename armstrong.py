n = input("Enter the number: ")

if not n.isdigit():
    print(f"{n} is an invalid entry. Don't use non-numeric, float, or negative values!")

else:
    result = 0

    for item in n:
        result += int(item) ** len(n)

    if result == int(n):
        print(f"{result} is an Armstrong number")

    else:
        print(f"{n} is not an Armstrong number")
