import random

alphabet = [
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
        ]

def main() :
    # WORDLIST
    list = [
    "EYE",
    "BOWL",
    "MOUSE"
    ]
    # CHOOSING RANDOM WORD
    rndom = random.randint(0,len(list) - 1)
    word = list[rndom]
    # COPYWORD
    """
        copyword = []
    for i in range(len(word) - 1) :
        copyword[i] = "_" 
    """
    copyword = word # temporarily
    # LIFE
    life = 6
    # GUESSED LETTERS
    guess = ["A","B","C"]
    
    gui(copyword, life, guess)
    inp(life, word, guess, copyword)

def inp(life, word, guess, copyword) :
    while True :
            letter = input("> ").upper()
            if letter in alphabet :
                if letter not in guess :
                    # success
                    guess.append(letter)
                    checkletter(life, word, letter, copyword, guess)
                    break
                else :
                    print("you already guessed that letter")
            else :
                print("ERROR")
    
def checkletter(life, word, letter, copyword, guess) :
                    # add letter to guess (upper())
                    # if there is no {letter} in word -> life -= 1
                    # else open letters
    search = word.find(letter)

    
    if search != -1 :
        #success
        print("horrayy")
    else :
        life -= 1

        checkgame(life, copyword, word, guess)
        
def checkgame(life, copyword, word, guess) :
    if life == 0 : # or copyword == word
        print("GAME OVER")
    else :
        gui(copyword, life, guess)
        inp(life, word, guess, copyword)

def gui(copyword, life, guess) :
    size = len(copyword)
    # WORD
    print("WORD : ")
    for i in range(size) :
        print(f"_{copyword[i]}_ ", end="")
    print("\n")

    # LIFES
    print("LIFES : ", end="")
    for i in range(life) :
        print(f"O ", end="")
    print("\n")

    # GUESSES
    print("GUESSED LETTERS : ", end="")
    for i in range(len(guess)) :
        print(f"{guess[i]} ", end="")
    print("\n")

main()