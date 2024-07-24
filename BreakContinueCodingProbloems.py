testString = "PooooooooooooP"
# GetWellSoonHJ

# for loop with the range() function
for i in range(0, len(testString), 1):
    print(testString[i], end=" ")

print("\r")

# for-each loop in python
# eachChar represents the character in the current iteration
# as we iterate through the string
for i in testString:
    print(i, end="")

print("\r")

# Question 1 - Print every character in the testString except for letter "O" "o"
#               USING THE FOR-EACH LOOP APPROACH AND CONTINUE STATEMENT

for eachletter in testString:
    if eachletter == "0"or eachletter == "o":
        continue # It starts a new iteration immediately
    print(eachletter, end=" ")

print("\r")

# Question 2 - To count the occurances of letter "O" "o" in the testString
# Use for-each loop, declare a new variable "count" to keep the count
# testString = "POOP"
#2
# Declare a new variable "count" to keep the count
# Create a for each loop to loop through testString
# In the loop, check if character in the current iteration (eachChar) is a letter "O" or "o"
# Mine got deleted

count = 0
for eachChar in testString:
    if eachChar == "o" or eachChar == "0":
        count += 1

print(count)

count = 0
for eachChar in testString:
    if eachChar == "o" or eachChar =="0":
        count += 1
    count = 0
    for eachChar in testString:
        if eachChar == "o" or eachChar == "0":
            count += 1









