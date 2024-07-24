FailureList = ["BeijingCorn", "Timmy"]

FailureList.insert(5, "UncleRogers")
FailureList.insert(1, "ShangHaiCorn")
FailureList.insert(2, "GuangZhouCorn")
FailureList.insert(3, "HongKongCorn")
FailureList.insert(4, "DogeCorn")
FailureList.insert(6, "StevenHe")

print(FailureList)


"""
Question 1 - 20%
[]
[1]
[2, 1]
[3, 2, 1]
[4, 3, 2, 1, ...]
"""


"""

numList1 = []
print(numList1)

for i in range(10, 0, -1):
    numList1.append(i)
    #print(numList1)
    
"""


"""

numList2 = []

for i in range(1, 11, 1):
    numList2.insert(0, i)
    print(numList2)
    

"""




"""
numList3 = [1, 2, 3]
del numList3[len(numList3) - 1]
print(numList3)
"""

import time

while True:
    numList1 = []
    for i in range(0, 11, 1):
        numList1.insert(0, i)
        print(numList1)
        time.sleep(0.05)

    for i in range(0, 11, 1):
        del numList1[len(numList1) - 1]
        print(numList1)
        time.sleep(0.05)




