# Carsten Kirkland
# CSCI 128 F
# Converter and Calculator

import matplotlib.pyplot as plt

# FUNCTION 1: Convert Between Bases

def convert_number(start_base, number, end_base):
    base_map = {"binary": 2, "octal": 8, "decimal": 10, "hexadecimal": 16}

    if start_base not in base_map or end_base not in base_map:
        return "Error: misspelled or invalid base."

    try:
        decimal_value = int(number, base_map[start_base])
    except ValueError:
        return "Error: number does not match the base."

    if end_base == "binary":
        converted = format(decimal_value, "b").upper().zfill(5)
    elif end_base == "octal":
        converted = format(decimal_value, "o").upper()
    elif end_base == "decimal":
        converted = str(decimal_value)
    else:
        converted = format(decimal_value, "x").upper()

    all_conversions = {
        "binary": format(decimal_value, "b").upper().zfill(5),
        "octal": format(decimal_value, "o").upper(),
        "decimal": str(decimal_value),
        "hexadecimal": format(decimal_value, "x").upper()
    }

    show_graph(all_conversions)

    with open("results.txt", "a") as f:
        f.write(f"CONVERSION: {number} ({start_base}) -> {converted} ({end_base})\n")

    return converted


# FUNCTION 2: Show Graph

def show_graph(conversions_dict):
    bases = list(conversions_dict.keys())
    lengths = []

    for base in bases:
        lengths.append(len(conversions_dict[base]))

    plt.bar(bases, lengths)
    plt.title("Length of Number in Each Base")
    plt.xlabel("Base")
    plt.ylabel("Character Length")
    plt.show()


# FUNCTION 3: Arithmetic Calculator

def calculate(base, num1, operation, num2):
    base_map = {"binary": 2, "octal": 8, "decimal": 10, "hexadecimal": 16}

    if base not in base_map:
        return "Error: misspelled or invalid base."

    try:
        dec1 = int(num1, base_map[base])
        dec2 = int(num2, base_map[base])
    except ValueError:
        return "Error: number does not match base."

    if operation not in ["+", "-", "*", "/"]:
        return "Error: invalid operation."

    if operation == "+":
        result_dec = dec1 + dec2
    elif operation == "-":
        result_dec = dec1 - dec2
    elif operation == "*":
        result_dec = dec1 * dec2
    else: 
        if dec2 == 0:
            return "Error: cannot divide by zero"
        result_dec = dec1 // dec2

    if base == "binary":
        result = format(result_dec, "b").upper().zfill(5)
    elif base == "octal":
        result = format(result_dec, "o").upper()
    elif base == "decimal":
        result = str(result_dec)
    else:
        result = format(result_dec, "x").upper()

    with open("results.txt", "a") as f:
        f.write(f"CALCULATION: {num1} {operation} {num2} in base {base} = {result}\n")

    return result


# MAIN PROGRAM

def main():
    print("Welcome to the Number Converter and Calculator!")

    while True:
        print("\nChoose an option:")
        print("1 - Convert a number")
        print("2 - Perform a calculation")
        print("3 - Quit")

        choice = input("Enter your choice (1/2/3): ").strip()

        if choice not in ["1", "2", "3"]:
            print("Error: invalid menu choice.")
            continue

        if choice == "1":
            start_base = input("Enter starting base: ").lower().strip()
            number = input("Enter number: ").strip()
            end_base = input("Enter ending base: ").lower().strip()

            result = convert_number(start_base, number, end_base)
            print(result)

        elif choice == "2":
            base = input("Enter number base: ").lower().strip()
            num1 = input("Enter first number: ").strip()
            operation = input("Enter operation (+, -, *, /): ").strip()
            num2 = input("Enter second number: ").strip()

            result = calculate(base, num1, operation, num2)
            print(result)

        else:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()