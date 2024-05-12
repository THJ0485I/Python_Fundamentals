"""
 Decimal - base 10 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

 Binary - base 2 (0, 1)

 Octal - base 8 (0, 1, 2, 3, 4, 5, 6, 7)

 Hexadecimal - base 16 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)

 Converting a decimal to any other systems to decimal
 Multiply and Sum

 1 byte = 8 bits
 
 """

bin1 = 0b1100
oct1 = 0o44
hex1 = 0xFF

print(int('0b1100', 2))
print(int('0o44', 8))
print(int('0xFF', 16))


# Converting a decimal to any other system
# Division and take remainders

int1 = 100

# Denary(base 10) to binary
print(bin(int1))
print(id(int1))  # id returns memory location of a data piece

# Denary to oct
print(oct(int1))

# Denary to hex
print(hex(int1))

# Math operations of binary numbers
bin10 = 0b111
bin20 = 0b11

print(bin10, bin20)
print(bin(bin10 + bin20))
"""
 Bitwise manipulation
 Manipulating a data piece on the granular level

 Bitwise AND, &
 Logical and (and) VS Bitwise and (&)
"""
num1 = 100
num2 = 200
if num1 > 0 and num2 > 0:
    print('Both numbers are positive')

"""
 Bitwise AND, &
 Both inputs have to be 1 for output to be 1
"""
x1 = 0b100
x2 = 0b111
print(bin(x1 & x2))


# Logical or
x10 = True
x20 = False
if x10 or x20:
    print('Either x10 or x20 is True')

"""
 Bitwise OR, |
 Either one of the input has to be 1 for the output to be 1
"""

y1 = 0b100
y2 = 0b111
print(bin(y1 | y2))

hex10 = 0xff
bin100 = 0b1101

print(int('0xff', 16))
print(int('0b1101', 2))

# Convert base10 to any other systems
int10 = 255

print(bin(int10))
print(oct(int10))
print(hex(int10))

# Math operations of Binary Numbers
bin1000 = 0b1111
bin2000 = 0b1001

print(bin(bin1000 + bin2000))
print(bin1000 + bin2000)

print(0b100 - 0b11)

"""
 Bitwise XOR, ^
 Both inputs have to be different for the output to be 1
bin3 = 0b100
bin4 = 0b111
print(bin(bin3 ^ bin4))

"""
 Bit shifting
 Left shifting, <<
"""
x3 = 0b100
print(bin(x3 << 3))
print(x3 << 3)

"""
 Bit shifting
 Right shifting, >>
"""
x31 = 0b100
print(bin(x31 >> 2))
print(x31 >> 2)