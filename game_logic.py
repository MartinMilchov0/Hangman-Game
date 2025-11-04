import random

startGame = ''
playAgain = 'Y'
totalScore = 0
rules = '''Welcome to Hangman! Your goal is to guess a hidden word either by guessing individual 
letters in the word or the entire word.
You have 5 health at the start and everytime you guess a letter incorrectly you lose 1 health.
But if you try to guess the entire word and dont get it right, you lose all your health at once.
If you reach 0 health, you lose the game.
You can choose the category of your word from 4 options - Fruits, Vegetables, Animals & School
and you also get a score based on how well you perform(1 health = 100 points).
Good luck and have fun!'''
fruitList = ['apple','banana','avocado','grapes','watermelon','cherry','strawberry','kiwi','peach','pear','raspberry']
vegetableList = ['potato','carrot','lettuce','cucumber','broccoli','garlic','tomato','turnip','cabbage','eggplant','pepper']
animalList = ['wolf','tiger','bear','squirrel','cat','dog','monkey','pigeon','chicken','sheep','cow','pig']
schoolList = ['pencil','teacher','student','desk','whiteboard','marker','class','classmate','chair','homework','lesson']
wordList = []

# Rules display and start prompt
print(rules)

while startGame.upper() != 'Y' and startGame.upper() != 'N':
    startGame = input('Would you like to begin?')
    print('')
    if startGame.upper() == 'N':
        playAgain = 'N'
    
# Full game loop
while playAgain.upper() == 'Y':
    categoryChoice = ''
    health = 5
    wordComplete = False
    playerGuesses = []
    incorrectGuesses = []
    # Choosing category and word
    while categoryChoice not in ('1', '2', '3', '4', '5'): 
        categoryChoice = input(
        'Which category would you like to choose for your word?\n'
        'Fruits (Type 1)\n'
        'Vegetables (Type 2)\n'
        'Animals (Type 3)\n'
        'School (Type 4)\n'
        'Surprise Me! (Type 5)\n'
        )
        match categoryChoice:
            case '1':
                wordList = fruitList
            case '2':
                wordList = vegetableList
            case '3':
                wordList = animalList
            case '4':
                wordList = schoolList
            case '5':
                wordList = schoolList + animalList + vegetableList + fruitList
            case _:
                print("Invalid choice. Please type 1, 2, 3, 4, or 5.")
    hiddenWord = random.choice(wordList)
    # Guessing word loop
    while health > 0 and wordComplete == False:
        for letter in hiddenWord:
            if letter in playerGuesses:
                print(letter,end='')
            else: print('_',end='')
        print("\nIncorrect guesses: " + ",".join(incorrectGuesses))
        print('Current health:',health)
        wordOrLetterChoice = input("Would you like to guess a letter(L) or guess the word(W):")
        if wordOrLetterChoice.upper() == 'L':
            letterGuess = input('Type a letter to make a guess:')
            playerGuesses.append(letterGuess.lower())
            if len(letterGuess)>1:
                print('You cannot use more than 1 letter!'); playerGuesses.pop()   
            if letterGuess.lower() not in hiddenWord and len(letterGuess) == 1:
                health -= 1
                print('You lost 1 life!')
                if letterGuess.lower() not in incorrectGuesses:
                    incorrectGuesses.append(letterGuess.lower())
            wordComplete = True
            for letter in hiddenWord:
                if letter not in playerGuesses:
                    wordComplete = False
        elif wordOrLetterChoice.upper() == 'W':
            finalGuess = ''
            finalGuess = input("Type the word you think is correct:")
            if finalGuess.lower() == hiddenWord:
                wordComplete = True
            else:health = 0
    # End of game messages
    if health == 0:
        print('Unfortunately, you did not guess the word.')
        print('The correct word was:',hiddenWord)
    if wordComplete == True:
        print(hiddenWord)
        print('Great job! You guessed the word correctly!')
    # Scoring
    currentScore = health*100
    totalScore = totalScore + currentScore
    print('Score:',currentScore)
    print('Total Score:',totalScore)
    # Play again prompt
    playAgain = input('Would you like to play again?(Y/N):')
    if playAgain.upper() == 'N':
        print('Thank you for playing!')
    while playAgain.upper() != 'Y' and playAgain.upper() != 'N':
        print('Please respond with Y or N.'); playAgain = input('Would you like to play again?(Y/N):')