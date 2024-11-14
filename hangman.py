word = input("Let’s play hangman! \n Player 1: Please choose a word: ")

print ("Player 1 has chosen a word:")
for i in word:
    print("_", end= " ")
print("")

word = word.upper()                                         # use only uppercase to get caseinsensitivity


count = 0
correctGuesses = []   

hangman_stages = [
    "+ - - - +\n|\n|\n|\n|\n|\n_____________",
    "+ - - - +\n|       o\n|\n|\n|\n|\n_____________",
    "+ - - - +\n|       o\n|       |\n|       |\n|\n|\n_____________",
    "+ - - - +\n|       o\n|      \| \n|       |\n|\n|\n_____________",
    "+ - - - +\n|       o\n|      \|/\n|       |\n|\n|\n_____________",
    "+ - - - +\n|       o\n|      \|/\n|       |\n|      /  \n|\n_____________",
    "+ - - - +\n|       o\n|      \|/\n|       |\n|      / \\\n|\n_____________",
    "+ - - - +\n| /     o\n|/     \|/\n|       |\n|      / \\\n|\n_____________"
]


while count < 8 and len(correctGuesses) < len(word):        # stop when either count = 8 or all letters are guessed correctly
    newLetter = input("Player 2 please guess a letter: ")
    newLetter = newLetter.upper()                           # use only uppercase to get caseinsensitivity

    if newLetter in word:
        correctGuesses = correctGuesses + [newLetter]
        print(f"You guessed correct! '{newLetter}' is part of the word.")
        for i in word:
            if i not in correctGuesses:
                print("_", end = " ")
            else:
                print (i, end = " ")
        print("")

    else:
        print(f"You guessed wrong. '{newLetter}' is not part of the word.")
        print(hangman_stages[count]) 
        print(f"You have now used {count+1}/8 wrong guesses.")          
        count+=1

if count == 8:
    print("Oh no! You have too many wrong guesses. Player 2 lost.") 
elif len(word) == len(correctGuesses):
    print("Congratulations, you guessed the correct word. Player 2 won!")

print("Game ends.")
