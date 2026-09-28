s = input("Enter a number: ").strip()
body = s[1:] if s.startswith("-") else s

if not body.replace(".", "", 1).isdigit():
    print("Invalid input")
else:
    n = float(s)

    if n == 0:
        print("Square root of 0 is 0")
    else:
        x = abs(n)
        guess = x
        for i in range(100):
            guess = (guess + x / guess) / 2

        root = round(guess, 4)

        if n < 0:
            print(f"Square root of {n} is {root}i ")
        else:
            print(f"Square root of {n} is {root}")
