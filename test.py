result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input(">>> ")

    if user_input == "=":
        print(result)
        break

    if wait_for_number == True:
        try:
            operand = float(user_input)
            wait_for_number = False
        except ValueError:
            print(f"{user_input} not a number, try again")
            continue

        if result is None:
           result = operand

        else:
            if operator == "+":
                result = result + operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == "/":
                try:
                     result /= operand 
                except ZeroDivisionError:
                    print(f"You can`t divide by {operand}")
                    wait_for_number = True
                    continue
    else:
        if user_input in ["+", "-", "*", "/"]:
           operator = user_input
           wait_for_number = True
        else:
            print(f"{user_input} incorrect math operator")
            continue
    