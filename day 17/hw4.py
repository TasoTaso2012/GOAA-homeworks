secret_number=9
guess=int(input("guess the secret number between 1 and 15: "))
while guess != secret_number:
    guess=int(input("try again:"))
print("you guessed right!")