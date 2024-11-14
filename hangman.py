while True:
    word = input("Let’s play hangman! \nPlayer 1: Please choose a word: ")
    if word.isalpha():              # checks if the word contains only alphabetic characters
        break                       # exit the loop if the word is valid
    else:
        print("Only words with standard letters are allowed. Try again!")

print ("Player 1 has chosen a word:")
for i in word:
    print("_", end= " ")
print("")

word = word.upper()                                         # use only uppercase to get caseinsensitivity


count = 0
correctGuesses = []
allGuesses = []   

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
    
    while True:
        newLetter = input("Player 2 please guess a letter: ")
        newLetter = newLetter.upper()                       # use only uppercase to get caseinsensitivity
        if newLetter.isalpha()  and  newLetter not in allGuesses and len(newLetter) == 1:
            allGuesses = allGuesses + [newLetter]
            break
        elif newLetter in allGuesses:
            print("You already guessed this letter. Please try again.")
        else: 
            print("Only single alphabetic letters allowed. Please try again.")


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
