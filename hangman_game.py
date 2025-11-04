import game_logic

def main():
    rules = '''Welcome to Hangman! Your goal is to guess a hidden word either by guessing individual 
    letters in the word or the entire word.
    You have 5 health at the start and everytime you guess a letter incorrectly you lose 1 health.
    But if you try to guess the entire word and dont get it right, you lose all your health at once.
    If you reach 0 health, you lose the game.
    You can choose the category of your word from 4 options - Fruits, Vegetables, Animals & School
    and you also get a score based on how well you perform(1 health = 100 points).
    Good luck and have fun!'''
    print(rules)

    startGame = input("Would you like to begin? (Y for Yes/ Anything else for No): ").upper()
    if startGame != 'Y':
        print("Maybe next time!")
        return

    totalScore = 0
    playAgain = 'Y'

    while playAgain == 'Y':
        score = game_logic.play_game()
        totalScore += score
        print("Score:", score)
        print("Total Score:", totalScore)

        playAgain = input("Would you like to play again? (Y/N): ").upper()
        while playAgain not in ('Y', 'N'):
            playAgain = input("Please respond with Y or N: ").upper()

    print("Thank you for playing!")


if __name__ == "__main__":
    main()