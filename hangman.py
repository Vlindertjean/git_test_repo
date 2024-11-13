word = input("Let’s play hangman! \n Player 1: Please choose a word: ")
print ("Player 1 chose a word:")
for i in word:
    print("_", end= " ")
print("")

word = word.upper()                                         # use only uppercase to get caseinsensitivity


count = 0

                                     # use only uppercase to get caseinsensitivity

while count <8:
    newLetter = input("Player 2 please guess a letter: ")
    newLetter = newLetter.upper()

    if newLetter in word:
        print(f"You guessed correct! '{newLetter}' is Part of the word.")

    else:
        print(f"You guessed wrong.'{newLetter}' is Part of the word.")
        if count == 0:
            print("+ - - - +\n|\n|\n|\n|\n|\n|\n_____________")
        elif count == 1:
            print("+ - - - +\n|       o\n|         \n|        \n|         \n|\n_____________")
        elif count == 2:
            print("+ - - - +\n|       o\n|       | \n|       |\n|         \n|\n_____________")
        elif count == 3:
            print("+ - - - +\n|       o\n|      \| \n|       |\n|         \n|\n_____________")
        elif count == 4:
            print("+ - - - +\n|       o\n|      \|/\n|       |\n|         \n|\n_____________")
        elif count == 5:
            print("+ - - - +\n|       o\n|      \|/\n|       |\n|      /  \n|\n_____________")
        elif count == 6:
            print("+ - - - +\n|       o\n|      \|/\n|       |\n|      / \\\n|\n_____________")
        else: 
            print("Oh no! You have too many wrong guesses. You lost.")
            print("+ - - - +\n| /     o\n|/     \|/\n|       |\n|      / \\\n|\n_____________")
                                        
                        
        count+=1
else:
    print("Game ends.")
