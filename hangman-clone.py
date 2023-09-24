import random
from words import word_list

def main () :
    game()
    while input("WANNA PLAY AGAIN? (Y/N) \n").upper() == "Y" :
        game() 


def game() :
    # definitions
    word = word_picker()
    life = 6
    word_copy = "_" * len(word)
    found = False
    guessed_letters = []
    guessed_words = []
    #
    print(f"{display_hangman(life)}")
    for i in range(len(word_copy)) :
        print(word_copy[i], end=" ")
    print("\n")
    #
    while life > 0 and found == False :
        # continue game

        # get input
        guess = input("Guess a letter or word : ")
        # LETTER
        if len(guess) == 1 and guess.isalpha() :
            if guess in guessed_letters :
                print("you already guessed ", guess)
            elif guess in word :
                # then guessed right
                #LIGHT UP THE GUESSED LETTERS
                temp_list = list(word_copy)
                for i in range(len(word)) :
                    if word[i] == guess :
                        temp_list[i] = guess
                word_copy = temp_list
                #
                guessed_letters.append(guess)
            else :
                # then guessed wrong
                print("Wrong guess")
                guessed_letters.append(guess)
                life -=1
        if "_" not in word_copy :
            found = True
        # WORD
        if len(guess) == len(word) :
            if guess in guessed_words :
                print("you already guessed", guess) 
            elif guess == word :
                # then guessed right
                word_copy = word
                found = True
            else :
                # then guessed wrong
                print("Wrong guess")
                guessed_words.append(guess)
                life -= 1

        elif len(guess) != 1 :
            print("size of word doesn't match")

        print(f"{display_hangman(life)}")
        for i in range(len(word_copy)) :
            print(word_copy[i], end=" ")
        print("\n")

    if found == True :
        print("CONGRATS YOU FOUND THE WORD ", word)
    else :
        print("Sorry word was", word)




def word_picker () :
    word = random.choice(word_list)
    return word


def display_hangman(life) :
    list = [
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

    return list[life]


main()