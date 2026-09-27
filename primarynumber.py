num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not a prime number")
else:
    count = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1

    if count == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
