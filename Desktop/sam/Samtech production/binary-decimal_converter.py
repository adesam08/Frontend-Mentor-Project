userDecision = input("Do you want to use binary to decimal converter (Type: bd) or decimal to binary converter (Type: db)")
if userDecision == "bd":
    #The function that converts binary to decimal
    def binaryToDecimal(binaryNumber):
        decimal = 0
        for i, digit in enumerate(reversed(binaryNumber)):
            decimal += int(digit) * (2**i)
        return decimal

    #Taking user's input
    binaryInput = input("Input your binary:- ")
    #Validating the user's input
    if set(binaryInput).issubset({"0","1"}):
        #Function applied on user's input
        result = binaryToDecimal(binaryInput)
        print(f"The decimal value of {binaryInput} is {result}")
    else:
        print("Invalid Input (0s and 1s should be inputed)")
elif userDecision == "db":
    #Function that converts decimal to binary
    def decimalToBinary(decimalNumber):
        binary = ""
        while decimalNumber > 0:
            binary = str(decimalNumber % 2) + binary
            decimalNumber //= 2
        return binary
    #Takes user's input
    decimalInput = int(input("Enter your number:- "))
    if decimalInput == 0:
        print("Enter a number")
    else:
        #Function applied on user's input
        result = decimalToBinary(decimalInput)
        print(f"The binary value of {decimalInput} is {result}")

else:
    print("Invalid Option")