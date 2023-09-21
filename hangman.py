# CHALLENGES 
    # ADD SCORES
    # MAKE DATABASE OF SCORES

import random
from words import word_list

def main() :
    word = pick_word()
    game(word)
    
    while input("WANNA PLAY AGAIN ? (Y/N) : ").upper() == "Y" :
        word = pick_word()
        game(word)
        # how can it looping idk actually??


def pick_word () : 
    word = random.choice(word_list)
    return word.upper() ### what return does


def game (word) : 
    # 
    word_copy = "_" * len(word)
    found = False
    guessed_letters = []
    guessed_words = []
    life = 6
    # display sec
    print(display_hangman(life))
    # displaying word_copy
    for i in range(len(word_copy)) :
        print(word_copy[i], end=" ")
    print("\n")

    while not found and life > 0 :
        guess = input("GUESS A LETTER OR WORD : ").upper()
        # PLAYER GUESSED LETTER
        if len(guess) == 1 and guess.isalpha() : # (isalpha checks is it from alphabet)
            if guess in guessed_letters : # already guessed
                print(f"ALREADY GUESSED {guess}")
            elif guess not in word : # wrong guess
                print("WRONG GUESS")
                life -= 1
                guessed_letters.append(guess)
            else : # CORRECT guess (letter)
                print("CORRECT GUESS")
                guessed_letters.append(guess)
                # turning on the guessed letters
                temp_list = list(word_copy) # making a temp list cuz word_copy is a str and str is immutable but list is mutable
                for i in range(len(word)) :
                    if word[i] == guess :
                        temp_list[i] = guess 
                        word_copy = temp_list
                    #
            if "_" not in word_copy : # if there is no empty spaces then finish game
                found = True
        # PLAYER GUESSED WORD
        elif len(guess) == len(word) and guess.isalpha() :
            if guess in guessed_words : # already guessed
                print("ALREADY GUESSED", guess)
            elif guess != word : # wrong guess
                print("WRONG GUESS")
                life -= 1
                guessed_words.append(guess)
            else : # CORRECT guess (word)
                found = True
                word_copy = word
        else :
            print("Not a valid guess")
        
        # looping again
        print(display_hangman(life))
        # displaying word_copy
        for i in range(len(word_copy)) :
            print(word_copy[i], end=" ")
        print("\n")

    if found :
        print(f"CONGRATULATIONS YOU FOUND THE {word}")
    else :
        print(f"DAMN WORD WAS -> {word}\n")


def display_hangman (life) :
    stages = [
        """
            ---------
            |       |
            |       O
            |      -|-
            |      / \\
            |
           / \\  LITTLE MAN DEAD   
          /   \\      
        """,
        """
            ---------
            |       |
            |       O
            |      -|-
            |      /
            |
           / \\
          /   \\
        """,
        """
            ---------
            |       |
            |       O
            |      -|-
            |
            |
           / \\
          /   \\
        """,
        """
            ---------
            |       |
            |       O
            |      -|
            |       
            |
           / \\
          /   \\
        """,
        """
            ---------
            |       |
            |       O
            |       |
            |
            |
           / \\
          /   \\
        """,
        """
            ---------
            |       |
            |       O
            |
            |
            |
           / \\
          /   \\
        """,
        """
            ---------
            |       |
            |
            |
            |
            |
           / \\
          /   \\
        """
    ]
    return stages[life]


main()
