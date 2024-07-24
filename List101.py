# Happy list []
# Steven He list - []

FAILUREList = [ "FAILURE MANAGEMENT", " Steven He", "Finding Jesus", " The Web-Man", 6969, True]
print(FAILUREList)

# Print each item in the list using for i in range approach

for i in range(len(FAILUREList)):
    print(FAILUREList[i], end=" ")

print("\r")

for eachItem in FAILUREList:
    print(FAILUREList, end=" ")

print("\r")

for i in  range(2):
    print(" FAILURE MANAGEMENT" + " **" + " Steven He" + " **" + "Finding Jesus" + " **" + " The Web-Man" )

for eachItem in FAILUREList:
    print(eachItem, end=" ** ")

for i in range(len(FAILUREList) -1, -1, -1):
    print(FAILUREList[i], end=" ")

print("\r")
print(FAILUREList[::-1])





