secret_word = "word"


guess = ""
count = 0
guess_limit = 3

out_of_guesses = False

while guess != secret_word and out_of_guesses == False:
    if count < guess_limit:
        guess = input("Enter guess: ")
        count = count + 1
    else:
        out_of_guesses = True
    

if out_of_guesses:
    print("Out of guesses")
else:
    print("You win!")

