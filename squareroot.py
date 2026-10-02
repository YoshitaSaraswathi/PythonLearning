def square_root(number):
    if number == 0:
        return "square root of 0 is 0"

    positive_number = abs(number)
    guess = positive_number

    while True:
        divide = positive_number / guess
        average = (guess + divide) / 2
        if abs(average - guess) < 0.000001:
            break
        guess = average

    if number < 0:
        return f"{average}i"
    else:
        return average


try:
    number = float(input("Enter a Number: "))
    print(square_root(number))
except ValueError:
    print("Invalid Input")
