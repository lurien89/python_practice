def binary_to_decimal(input_binary):

    i = len(input_binary) - 1
    j = 0
    output_decimal = 0

    # Loop through each bit in the binary input, from left to right
    while i >= 0:
        output_decimal = output_decimal + (int(input_binary[j]) * 2 ** i)
        i = i - 1
        j = j + 1

    return(output_decimal)

def binary_to_hex(input_binary):
    return(decimal_to_hex(binary_to_decimal(input_binary)))

def decimal_to_binary(input_decimal):
    binary_digits = []
        
    while input_decimal > 0:
        remainder = input_decimal % 2
        binary_digits.append(str(remainder)) # Append the remainder as a string to the binary_digits list
        input_decimal //= 2

    binary_digits.reverse()
    binary_output = ''.join(binary_digits)

    return(binary_output)

def decimal_to_hex(input_decimal):
    hex_digits = []
        
    while input_decimal > 0:
        remainder = input_decimal % 16
        if remainder < 10: # Append numeric digits (0-9) or convert to hexadecimal letters (A-F)
            hex_digits.append(str(remainder))
            
        else:
            hex_digits.append(chr(remainder - 10 + ord('A')))

        input_decimal //= 16

    # Reverse to arrange digits in correct order
    hex_digits.reverse()
    # Combine list of hex digits into a single string
    hex_output = ''.join(hex_digits)

    return(hex_output)

def hex_to_binary(input_hex):
    return(decimal_to_binary(hex_to_decimal(input_hex)))

def hex_to_decimal(input_hex):
    
    decimal_output = 0
    power = 0
    
    # Process each character from right to left (reverse order)
    for digit in reversed(input_hex):
        if '0' <= digit <= '9':  # Convert '0'-'9' to 0-9
            decimal_value = ord(digit) - ord('0')

        elif 'A' <= digit <= 'F':  # Convert 'A'-'F' to 10-15
            decimal_value = ord(digit) - ord('A') + 10

        else:
            print("Invalid hexadecimal number.")
            return

        # Add to the total decimal output
        decimal_output += decimal_value * (16 ** power)
        power += 1

    return(decimal_output)

def user_interface():
    input_data = []
    
    print("Base Converter takes any combination of binary, decimal and hexadecimal.")

    input_data.append(input("Select the type of number you want to convert from (b/d/h): "))
    input_data.append(input("Select the type of number you want to convert to (b/d/h): "))

    if input_data[0] == 'b' and input_data[1] == 'd':
        binary_input = (input("Enter the binary number: "))
        print(binary_input, "equals", binary_to_decimal(binary_input), "in decimal.")

    elif input_data[0] == 'b' and input_data[1] == 'h':
        binary_input = (input("Enter the binary number: "))
        print(binary_input,"equals",binary_to_hex(binary_input))

    elif input_data[0] == 'd' and input_data[1] == 'b':
        decimal_input = (input("Enter the decimal number: "))
        print(decimal_input, "equals", decimal_to_binary(decimal_input), "in binary.")

    elif input_data[0] == 'd' and input_data[1] == 'h':
        decimal_input = input("Enter the decimal number: ")
        print(decimal_input, "equals", decimal_to_hex(decimal_input), "in hexadecimal.")

    elif input_data[0] == 'h' and input_data[1] == 'b':
        hex_input = (input("Enter the hex number: "))
        print(hex_input, "equals", hex_to_binary(hex_input), "in binary.")

    elif input_data[0] == 'h' and input_data[1] == 'd':
        hex_input = input("Enter the hexadecimal number: ").upper()
        print(hex_input, "equals", hex_to_decimal(hex_input), "in decimal")

    elif input_data[0] == 'x' or input_data[1] == 'x':
        exit

    else:
        print("Input error")
        user_interface()

user_interface()
