def list_numbers():
    print("Put at least 5 numbers:")
    numbers = []

    while len(numbers) < 5:
        num = int(input("Enter a number: "))
        numbers.append(num)

    print("Max:", max(numbers))
    print("Min:", min(numbers))
    print("Sum:", sum(numbers))
    print("Length:", len(numbers))


list_numbers()



