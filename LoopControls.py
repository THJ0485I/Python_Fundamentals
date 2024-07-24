#For loop
# It is used when we know specifically the no. of repeatition
for i in range(0, 5, 1):
    print("Blah")

import time
#While Loop
#It is used when we are uncertain about the amount of repetitions
#But we know the condition for which the loop has to remain active
#Loop manipulation techniques:
#1. To alter the execution speed/frequency of a loop
#2. Break  - Terminate the loop immediately
# 3. continue - The continue statement exits the current iteration
# #               and starts a new iteration immediately!

WaterCount = 0
while True:
    WaterCount = WaterCount + 1
    print("Water" + "-" + str(WaterCount))
    if WaterCount > 99:
        print(" You have reached Ohio")
        break


    if WaterCount < 50:
        continue

    print(" You are reaching Ohio")
    time.sleep(0.1)

print("END OF LOOP")