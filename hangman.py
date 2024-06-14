import random

words = ["hymn", "cyst", "griffonage", "petrichor", "coign", "fudgel", "nudistertian", "selcouth", "defenestration", "phosphene", "cledonism", "somnambulist", "bombinate", "ineffable", "syzygy", "jayus" ]

def get_random_word():
    random_word = words[random.randint(0, len(words) - 1)] #randomly selects an integer that is the length of the list
    return random_word

randomWord = get_random_word()

def how_many_guesses():
    guess = len(randomWord) + 5
    return guess

guesses = how_many_guesses()

def guess_letter():
    letter = input("Guess a letter: ")
    guessedLetters = []
    if letter in randomWord:
        print("This letter is in the word")
    else:
        print("This letter is not in the word")
    
    global guesses
    guesses = guesses - 1
    return letter, guesses

guessedLetter = guess_letter()

print("Let's play Hangman! Here is the length of your word: " + str(len(randomWord)) + " letters")
print("Guesses left: " + str(guesses))
print("Let's begin: " + str(guessedLetter))
