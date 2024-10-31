def binary():
    output_type = input("Select the type of number you want to convert to (b/d/h): ")

    if output_type == 'd':
        input_binary = input("Input the binary number: ")
        # Need to verify that the input number is in fact binary

        # Binary to decimal converter here


def decimal():
    output_type = input("Select the type of number you want to convert to (b/d/h): ")

    if output_type == 'b':
        input_decimal = input("Input de decimal number: ")
        # Need to verify decimal
        while input_decimal != 0:
            input_decimal // 2
            remainder = input_decimal % 2
            rev_binary = rev_binary + str(remainder)

        while len(rev_binary):
            i = -1
            binary_output = binary_output + binary_output[i]
            i = i - 1
        print(binary_output)

def hexadecimal():
    print("PLACEHOLDER")

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


