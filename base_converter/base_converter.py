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

        print(output_decimal)

    else:
        print("Invalid option")

def decimal():
    output_type = input("Select the type of number you want to convert to (b/d/h): ")
    binary_digits = []

    if output_type == 'b':
        input_decimal = int(input("Input the decimal number: "))
        # reversed_binary = ""
        while input_decimal > 0:
            remainder = input_decimal % 2
            #input_decimal = input_decimal // 2
            binary_digits.append(str(remainder))
            #reversed_binary = str(reversed_binary) + str(remainder)
            input_decimal //= 2

        binary_digits.reverse()

        #i = -1
        #binary_output = ""
        #while (i * -1) != (len(reversed_binary) +1):
        #    binary_output = binary_output + reversed_binary[i]
        #    i = i - 1

        binary_output = ''.join(binary_digits)

        print(binary_output)

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


