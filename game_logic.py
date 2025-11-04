import random

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

def choose_category():
    while True: 
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
                return fruitList
            case '2':
                return vegetableList
            case '3':
                return animalList
            case '4':
                return schoolList
            case '5':
                return schoolList + animalList + vegetableList + fruitList
            case _:
                print("Invalid choice. Please type 1, 2, 3, 4, or 5.")

def play_game():
    health = 5
    wordComplete = False
    playerGuesses = []
    incorrectGuesses = []
    hiddenWord = random.choice(choose_category())

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
            if len(letterGuess)>1:
                print('You cannot guess more than 1 letter!')
                continue
            if letterGuess.lower() in playerGuesses or letterGuess.lower() in incorrectGuesses:
                print('You have already guessed that letter!')
                continue
            if letterGuess.lower() in hiddenWord:
                playerGuesses.append(letterGuess.lower())
            else:
                incorrectGuesses.append(letterGuess.lower())
                health -= 1
                print('You lost 1 life!')

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

    if health == 0:
        print('Unfortunately, you did not guess the word.')
        print('The correct word was:',hiddenWord)
    if wordComplete == True:
        print(hiddenWord)
        print('Great job! You guessed the word correctly!')

    return health*100