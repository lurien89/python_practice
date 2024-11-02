# Function definitions

def binary():
    output_type = input("Select the type of number you want to convert to (b/d/h): ")

    if output_type == 'd':
        input_binary = input("Input the binary number: ")
        # Need to verify that the input number is in fact binary

        # Binary to decimal converter here


def decimal():
    output_type = input("Select the type of number you want to convert to (b/d/h): ")

    if output_type == 'b':
        input_decimal = int(input("Input the decimal number: "))
        # Need to verify decimal
        reversed_binary = ""
        while input_decimal > 0:
            input_decimal = input_decimal // 2
            remainder = input_decimal % 2
            reversed_binary = str(reversed_binary) + str(remainder)
            #For debugging
            print(input_decimal)
            #print(reversed_binary)

        #i = -1
        #binary_output = ""
        #while (i * -1) != (len(reversed_binary) +1):
        #    binary_output = binary_output + reversed_binary[i]
        #    i = i - 1

        print(reversed_binary)
        #print(binary_output)

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


