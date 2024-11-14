word = input("Let’s play hangman! \n Player 1: Please choose a word: ")

print ("Player 1 has chosen a word:")
for i in word:
    print("_", end= " ")
print("")

word = word.upper()                                         # use only uppercase to get caseinsensitivity


count = 0
correctLetters = []                          

while count < 8 and len(correctLetters) < len(word):        # stop when either count = 8 or all letters are guessed correctly
    newLetter = input("Player 2 please guess a letter: ")
    newLetter = newLetter.upper()                           # use only uppercase to get caseinsensitivity

    if newLetter in word:
        correctLetters = correctLetters + [newLetter]
        print(f"You guessed correct! '{newLetter}' is part of the word.")
        for i in word:
            if i not in correctLetters:
                print("_", end = " ")
            else:
                print (i, end = " ")
        print("")

    else:
        print(f"You guessed wrong. '{newLetter}' is part of the word.")
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
            print("+ - - - +\n| /     o\n|/     \|/\n|       |\n|      / \\\n|\n_____________")
            print("Oh no! You have too many wrong guesses. You lost.")           
        
        count+=1

else:
    print("Game ends.")
