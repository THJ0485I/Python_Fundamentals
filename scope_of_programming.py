# Scope of programming in Python

# It has to do with how Python access/find0 a variable

"""
Common abbreviation: LEGB
Local - Variables that are defined within a function
Enclosing - Variables that are defined in the local scope of an enclosing function
Global - Variables defined at the top level of a module/script or those
          declared explicitly with the "global" keyword
Built-in - Variables that are pre-assigned in Python
"""

# Global Scope

Result = 100
print(Result)

global Age
Age = 1000000
print(Age)

# Global Scope
Bank = 'Do Bad System (DBS)'

def function1():
    # Local Scope
    Bank = 'Obama Chicken Bank Club (OCBC)'
    print(Bank)

function1()
print(Bank)

# Global Scope
PLace = 'Somewhere in this Solar System'

def function2 ():
    # Enclosing Scope
    PLace = 'Somewhere in the Universe'

    def function3():
        # Local Scope
        Place = 'Somewhere in Earth'

    function3()
function2()


# Global Scope
x = 10
def function4 ():
    # Local Scope
    x = 20
    x += 10  # Update x in the Local Scope
    print(x)

function4()

print(x)  # x in the Global Scope remains unchanged

# Global Scope
x = 10
def function4 ():
    # Local Scope
    global x  # Point to the Global x variable
    x += 10  # Update x in the Local Scope
    print(x)

function4()

print(x)  # x in the Global Scope has been updated

# Variable Shadowing
# Using the same variable name in different scopes

# Global Scope
x =10

def function5():
    # Enclosing Scope
    x = 20
    def function6():
        # Enclosing scope
        nonlocal x
        def function7():
            # Local Scope
            nonlocal x

        function7()
    function6()
function5()
