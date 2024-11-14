import string

class Hangman:
    stages = [
        "+ - - - +\n|\n|\n|\n|\n|\n_____________",
        "+ - - - +\n|       o\n|\n|\n|\n|\n_____________",
        "+ - - - +\n|       o\n|       |\n|       |\n|\n|\n_____________",
        "+ - - - +\n|       o\n|      \| \n|       |\n|\n|\n_____________",
        "+ - - - +\n|       o\n|      \|/\n|       |\n|\n|\n_____________",
        "+ - - - +\n|       o\n|      \|/\n|       |\n|      /  \n|\n_____________",
        "+ - - - +\n|       o\n|      \|/\n|       |\n|      / \\\n|\n_____________",
        "+ - - - +\n| /     o\n|/     \|/\n|       |\n|      / \\\n_____________"
    ]
    
    def __init__(self):
        self.wrong_guesses = 0
    
    def display(self):
        print(self.stages[self.wrong_guesses])
    
    def add_wrong_guess(self):
        self.wrong_guesses += 1
        self.display()

class Player:
    def __init__(self):
        self.guesses = set()
    
    def guess_letter(self):
        while True:
            guess = input("Guess a letter: ").upper()
            if len(guess) == 1 and guess in string.ascii_uppercase and guess not in self.guesses:
                self.guesses.add(guess)
                return guess
            elif guess in self.guesses:
                print("You already guessed that letter. Try again.")
            else:
                print("Please enter a single alphabetic character.")

class Game:
    def __init__(self):
        self.word = self.get_word().upper()
        self.correct_guesses = set()
        self.hangman = Hangman()
        self.player = Player()
    
    def get_word(self):
        while True:
            word = input("Player 1, please enter a word: ")
            if word.isalpha():
                return word
            else:
                print("Only words with letters are allowed. Try again.")
    
    def display_word_progress(self):
        display = [letter if letter in self.correct_guesses else "_" for letter in self.word]
        print(" ".join(display))
    
    def play(self):
        print("Let's play Hangman!")
        while self.hangman.wrong_guesses < 8 and set(self.word) != self.correct_guesses:
            self.display_word_progress()
            guess = self.player.guess_letter()
            if guess in self.word:
                self.correct_guesses.add(guess)
                print(f"Correct! '{guess}' is in the word.")
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                self.hangman.add_wrong_guess()
        
        self.end_game()
    
    def end_game(self):
        if set(self.word) == self.correct_guesses:
            print("Congratulations! You guessed the word:", self.word)
        else:
            print("Game over. The word was:", self.word)
        print("Thanks for playing Hangman!")

# Run the game
if __name__ == "__main__":
    game = Game()
    game.play()