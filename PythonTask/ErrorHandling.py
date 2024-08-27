def get_integer_input(prompt):
    attempts = 0
    failed_attempts = []
    while attempts < 3:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
            return user_input
        except ValueError as e:
            attempts += 1
            failed_attempts.append((user_input, str(e)))
            print("Invalid input. Please enter an integer.")
    if attempts == 3:
        print("Maximum attempts reached. Failed attempts:")
        for attempt in failed_attempts:
            print(f"Input: {attempt[0]}, Error: {attempt[1]}")
        return None

number = get_integer_input("Enter a number: ")
if number is not None:
    print("You entered:", number)
else:
    print("Failed to get a valid number.")
    