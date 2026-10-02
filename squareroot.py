def get_number():
    while True:
        try:
            return float(input("Enter a Number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")


def square_root(number):

    if number == 0:
        return "0"

    negative = number < 0
    number = abs(number)

    guess = number

    while True:
        divide = number / guess
        average = (guess + divide) / 2

        if abs(average - guess) < 0.000001:
            break

        guess = average

    if negative:
        return f"{average}i"
    else:
        return average


number = get_number()
answer = square_root(number)

print("Square root:", answer)

