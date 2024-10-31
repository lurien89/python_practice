def binary():
    output_type = input("Select the type of number you want to convert to (b/d/h): ")

    if output_type == 'd':
        input_binary = input("Input the binary number: ")
        # Need to verify that the input number is in fact binary
        

def decimal():
    print("PLACEHOLDER")

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


