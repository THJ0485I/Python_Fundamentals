import random
"""
# Immutable Python Objects (Not Changeable)
# Integer, String, Float, Tuple, Boolean
"""

# Before change
Age = random.randint(10, 20)
print(Age)
print(id(Age))

# After change
Age1 = random.randint(15, 25)
print(Age1)
print(id(Age1))

Y = 50
print(id(Y))

Y += 1
print(id(Y))


"""
Mutable Python Objects (Changeable)
List, Set, Dictionary
"""

foodList = ['Ohio Fried Children', 'Obama Fried Chicken', 'Kentucky Fried Children']
print(id(foodList))

# To edit an element in the list
foodList[2] = 'Kentucky Fried Chicken'

print(foodList)
print(id(foodList))

"""
To edit multiple items in the list at once
Use list slicing
"""
foodList[1::1] = ['Obama Fried Chicks', 'Obama Fried Children']
print(foodList)
print(id(foodList))

# To add an item to the list
foodList.append('Ohio Flying Children')
print(foodList)
print(id(foodList))

numList1 = [100, 101, 102]
print(id(numList1))

# Re-assignment (Re-assign a different list changes the memory location)
numList1 =[0, 0, 0]
print(id(numList1))

# A list is mutable ONLY WHEN we change elements within the list

# numList3 will be affected when we change numList2
numList2 = [1, 2, 3, 4]
print(id(numList2))

numList3 = numList2 # Assign numList2 to numList3, both stored in the same memory loc
print(id(numList3))

numList2.append(5)  # When you update elements in the list, it effects another pointer

print(numList3)  # numList3 has been updated


# How do we prevent changing numlist3 when numList2 changes?
# Use copy() function
# To prevent changing numList3 when numList2 changes
numList2 = [1, 2, 3, 4]
print(id(numList2))

numList3 = numList2.copy()  # Copy() duplicates numList2
print(id(numList3))

numList2.append(5)  # When you update elements in the list, it effects another pointer

print(numList3)  # numList3 has been updated