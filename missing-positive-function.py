def First_missing_positive(numbers):

    maximum = max(numbers) # Find the maximum number in the array, O(length)
    missing_number = -1 # Initiating the missing number to a negative value
    MISSING_NUMBERS = []
    for i in range(maximum):
        if (maximum - i) not in numbers: # We check for every value between 0 and our maximum number
            missing_number = maximum - i
            MISSING_NUMBERS.append(missing_number)

    if missing_number == -1: # If all values between our maximum and 0 exist, then the missing number is larger by 1.
        missing_number = maximum + 1
    else:
        missing_number = max(MISSING_NUMBERS)

    return missing_number



#I've used this tedious method to enter the array
#yet it ensures that all values are valid.
numbers = []

while True:
    n = input("Please enter a number to add to list, or press 'N' to continue: ")

    if n.upper() == "N":
        break

    elif n.isnumeric():
        numbers.append(int(n))

    else:
        print("Please enter a valid value.")


print(f"Original list: {numbers}")
print(f"The missing positive is: {First_missing_positive(numbers)}")