import random as rnd

def hangman():
    stages = ["",
              "________          ",
              "       |          ",
              "|      0          ",
              "|     /|\         ",
              "|     / \         ",
              "|"]
    
    wrong_attempt = 0
    win = False
    keywords = ["iloveyoutoo","guffadi","badarni","imissyou","monkey","lotsoflove","airplane"]
    rnum = rnd.randint(0,5)
    #rnum = 0
    word = keywords[rnum]
    letter_board = ["__"] * len(word)
    remaining_letters = list(word)
    
    print("Welcome to Hangman \n")
    
    while wrong_attempt < len(stages) -1:
        print("\n")
        guess = input("Guess a letter or type 1 to quit \n")
        if guess == '1':
            win = "quit"
            break
        else:
            if guess in remaining_letters:
                character_index = remaining_letters.index(guess)
                letter_board[character_index] = guess
                remaining_letters[character_index] = '$'
            else:
                wrong_attempt +=1   
            print((' '.join(letter_board)))
            print('\n'.join(stages[0: wrong_attempt + 1]))
            if '__' not in letter_board:
                print("You win !! The word was ::")
                print(' '.join(letter_board))
                win = True
               

    if not win:
        print('\n'.join(stages[0: wrong_attempt]))
        print('You lose! The words was {}'.format(word))
    elif win == 'quit':
        print("You have quit the game")

hangman()  




