# creating a calculator
# we need function for operation

# Addition
def add(a,b):
    return  a + b

# Subtraction
def sub(a,b):
    return a - b

# Multiplication
def mul(a,b):
    return a * b

print("choose \n1.Addition \n2.Subtraction \n3.Multiplication")
choose = int(input("Enter your choice:"))

# get the input from the user
a = int(input("Enter first number to calculate:"))
b = int(input("Enter seconde number to calculate:"))

if choose == 1:
        print("Sum:", add(a,b))
elif choose == 2:
    print("Subtraction:", sub(a,b))
else:
    print("Multiplication:",mul(a,b))
