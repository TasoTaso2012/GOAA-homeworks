number = int(input("Enter a number: "))
num=1
factorial = 1


while num <= number:
    factorial *= num
    num += 1

print(f"The factorial of {number} is: {factorial}")
