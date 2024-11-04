# Function definitions

def binary():
    output_type = input("Select the type of number you want to convert to (b/d/h): ")

    if output_type == 'd':
        input_binary = input("Input the binary number: ")
        # Need to verify that the input number is in fact binary

        i = len(input_binary) - 1
        j = 0
        output_decimal = 0

        while i >= 0:
            output_decimal = output_decimal + (int(input_binary[j]) * 2 ** i)
            i = i - 1
            j = j + 1

        return(output_decimal)

    else:
        print("Invalid option")

def decimal():
    output_type = input("Select the type of number you want to convert to (b/d/h): ")

    if output_type == 'b':
        binary_digits = []
        input_decimal = int(input("Input the decimal number: "))
        
        while input_decimal > 0:
            remainder = input_decimal % 2
            binary_digits.append(str(remainder))
            input_decimal //= 2

        binary_digits.reverse()
        binary_output = ''.join(binary_digits)

        return(binary_output)

    elif output_type == "h":
        hex_digits = []
        input_decimal = int(input("Input the decimal number :"))

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

    else:
        print("PLACEHOLDER")

def hexadecimal():
    print("PLACEHOLDER")

# Start of the interface

print("Base Converter takes any combination of binary, decimal and hexadecimal.")

input_type = input("Select type of number you want to convert (b/d/h): ")

if input_type == 'b':
    binary()

elif input_type == 'd':
    decimal()

elif input_type == 'h':
    hexadecimal()

else:
    print("Input error")


