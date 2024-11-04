# Function definitions

def binary_to_decimal(input_binary):

    i = len(input_binary) - 1
    j = 0
    output_decimal = 0

    while i >= 0:
        output_decimal = output_decimal + (int(input_binary[j]) * 2 ** i)
        i = i - 1
        j = j + 1

    return(output_decimal)

def binary_to_hex(input_binary):
    print("PLACEHOLDER")

def decimal_to_binary(input_decimal):
    binary_digits = []
        
    while input_decimal > 0:
        remainder = input_decimal % 2
        binary_digits.append(str(remainder))
        input_decimal //= 2

    binary_digits.reverse()
    binary_output = ''.join(binary_digits)

    return(binary_output)

def decimal_to_hex(input_decimal):
    hex_digits = []
        
    while input_decimal > 0:
        remainder = input_decimal % 16
        if remainder < 10:
            hex_digits.append(str(remainder))
            
        else:
            hex_digits.append(chr(remainder - 10 + ord('A')))

        input_decimal //= 16

    hex_digits.reverse()
    hex_output = ''.join(hex_digits)

    return(hex_output)

def hexadecimal():
    print("PLACEHOLDER")

# Start of the interface

def user_interface():
    input_data = []
    
    print("Base Converter takes any combination of binary, decimal and hexadecimal.")

    input_data.append(input("Select the type of number you want to convert from (b/d/h): "))
    input_data.append(input("Select the type of number you want to convert to (b/d/h): "))

    if input_data[0] == 'b' and input_data[1] == 'd':
        binary_input = (input("Enter the binary number: "))
        print(binary_input, "equals", binary_to_decimal(binary_input), "in decimal.")

    elif input_data[0] == 'b' and input_data[1] == "h":
        print("PLACEHOLDER")

    elif input_data[0] == 'd' and input_data[1] == "b":
        print("PLACEHOLDER")

    elif input_data[0] == 'd' and input_data[1] == 'h':
        print("PLACEHOLDER")

    elif input_data[0] == 'h' and input_data[1] == 'b':
        print("PLACEHOLDER")

    elif input_data[0] == 'h' and input_data[1] == 'd':
        print("PLACEHOLDER")

    elif input_data[0] == 'x' or input_data[1] == 'x':
        exit

    else:
        print("Input error")
        user_interface()

user_interface()
