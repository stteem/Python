def hangman(secretWord):
    
    guessesCounter = 8
    lettersGuessed = ' '
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",  len(secretWord),  "letters long.")
    print("-------------")
    
    while not isWordGuessed(secretWord, lettersGuessed):
        
        print("You have", guessesCounter, "guesses left.")
        print("Available letters: ", getAvailableLetters(*lettersGuessed))
        lettersGuessed = input("Please guess a letter: ").lower()
                
        if isWordGuessed(secretWord, lettersGuessed):        
            print("Good guess:",getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            
            print("Congratulations! You have won")            
            return None
        
        elif lettersGuessed in lettersGuessed:
            print("Oops! You’ve already guessed that letter:",
                  getGuessWord(secretWord, lettersGuessed))
        
        elif lettersGuessed in secretWord:
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
            guessesCount -= 1

        else:
            print("Oops! That letter is not in my word",getGuessedWord(secretWord, lettersGuessed))
            print('-----------')
        
        if guessesCounter == 1:
            print("Sorry, you ran out of guesses. The word was ", secretWord)
            break
    return None
                