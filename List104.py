def Odd_Number_Filter(UncleRoger):
    numList2 = []
    for eachNum in UncleRoger:
        if eachNum % 2 == 1:
            numList2.append(eachNum)
    print(numList2)

Odd_Number_Filter([*range(1, 101, 1)])


# Given any list, find the largest number in the list
def ourMaxFunction(BeijingCorn):
    curr_max = BeijingCorn[0]
    for eachNum in BeijingCorn:
        if  eachNum > curr_max:
            curr_max = eachNum
    return  curr_max


print(ourMaxFunction([1000000000000,10000000029, 89102]))


# Given in any list, find the smallest number in the list
def ourMinFunction(BeijingCorn):
    curr_max = BeijingCorn[0]
    for eachNum in BeijingCorn:
        if  eachNum < curr_max:
            curr_max = eachNum
    return  curr_max

print(ourMinFunction([1000000000000,10000000029, 89102]))


# Create a function that returns the sum of all numbers in a anyList - 20%
# anyList = [1, 2, 3]
# output: 6

def Sumy(ShangHaiCorn):
    pocket = 0
    for eachNum  in ShangHaiCorn:
        pocket = pocket + eachNum # Change the pocket by +eachNum
    return pocket
print(Sumy([*range(1, 101, 1)]))

def SumyAvg(ShangHaiCorn):
    pocket = 0
    for eachNum  in ShangHaiCorn:
        pocket = pocket + eachNum # Change the pocket by +eachNum
    return pocket/2
print(SumyAvg([*range(1, 101, 1)]))