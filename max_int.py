num_int = int(input("Input a number: "))    # Do not change this line

num1 = 0
max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))
    num1 = num_int
    if num1 > max_int:
        max_int = num1

print("The maximum is", max_int)    # Do not change this line
