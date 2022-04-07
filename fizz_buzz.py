def fizz_buzz(input_number):
    if input_number % 3 == 0 and input_number % 5 == 0:
        return "fizz buzz"
    elif input_number % 3 == 0:
        return "fizz"
    elif input_number % 5 == 0:
        return "buzz"