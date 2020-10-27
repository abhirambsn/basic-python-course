"""
Syntax of if in python

in C,

if (expression / condition) {
    statements
}

in python

if expression/condition:
    <4 space tab indentation>
    statements
elif expression/condition:
    <4 space tab indentation>
    statements
else:
    <4 space tab indentation>
    statements
program continues
"""

# WAP to input 2 numbers and print the larger number, or Equal if the numbers are equal

a = int(input("Enter a:"))
b = int(input("Enter b:"))

if a == b:
    print("Equal")
elif a > b:
    print(a)
else:
    print(b)
