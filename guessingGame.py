secret_number = 9;
guess_count = 0;
guess_limit=3
while guess_count<guess_limit:
    guess = input("Guess: ")
    guess_count+=1;
    if int(guess) == secret_number:
        print("You won!")
        break
else:
    print("Sorry you failed")