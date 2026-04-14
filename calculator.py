def run_calculator():
    while True:
        print("\n===== Calculator Menu =====")
        print("1. Basic Calculator")
        print("2. Temperature Converter")
        print("3. Back to Main Menu")

        menu = input("Enter your choice: ")

        # ---------------- Calculator ----------------
        if menu == '1':
            print("\n===== Calculator =====")

            # Input with validation
            try:
                first_no = float(input("Enter first number: "))
                operand = input("Enter operator (+, -, *, /): ")
                second_no = float(input("Enter second number: "))
            except:
                print("Invalid input. Try again.")
                continue

            if operand == '+':
                result = first_no + second_no
            elif operand == '-':
                result = first_no - second_no
            elif operand == '*':
                result = first_no * second_no
            elif operand == '/':
                if second_no == 0:
                    print("Cannot divide by zero!")
                    continue
                result = first_no / second_no
            else:
                print("Unknown operator")
                continue

            print(f"Result: {result}")

        # -------- Temperature Converter --------
        elif menu == '2':
            print("\n===== Temperature Converter =====")

            try:
                temp = float(input("Enter temperature in Celsius: "))
                temp_in_f = (temp * 9/5) + 32
                print(f"Temperature in Fahrenheit: {temp_in_f}")
            except:
                print("Invalid input.")

        # -------- Exit back to main --------
        elif menu == '3':
            print("Returning to main menu...")
            break

        else:
            print("Invalid selection")