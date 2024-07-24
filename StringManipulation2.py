# String input
testString = "Timothy"

#  substring - imo
print(testString[1:4:1])

# substring -Tim
print(testString[3:6:1])

# substring - imothy
print(testString[1::1])

# substring - Tom
print(testString[4:1:-1])

# substring - omiT
print(testString[5:0:-2])

# substring - yoT
print(testString[6::-3])

# Given any string that has at least 7 characters
# Extract and join the first and last three characters of the string
# Sample
#"HONGJIANG"
# "HONANG"
# Solve this problem using thge string slicing technique

while True:
    ToContiune = input("Would you like to continue? (Y/N) ")
    if ToContiune == "Y":

        testString2 =  input("Enter a word that has at least 7 chars: ")
        if len(testString2) >= 7:
            print(testString2[0:3:1] + testString2[len(testString2) - 3::1])
        else:
            print("Please enter a world that has at least 7 chars")
    elif ToContiune == "N":
        print("Ok! See you later. Bye-Bye!")
        break

    else:
        print("Don't try to be funny, only Y or N is accepted")
