def num_guess():
    guess_number = 9
    guess_count = 0
    while guess_count < 3:
        guess = int(input("guess a number : "))
        guess_count += 1
        if guess == guess_number:
            print("well done 👏")
            break
    else:
        print("You lost !")
        print("Try again 😉")


num_guess()
while 1:
    x = input("Do you want to continue(Y/N): ")
    if x == 'Y' or x == 'y':
        num_guess()
    else:
        break
print("thanks for choosing hope you enjoyed...")
