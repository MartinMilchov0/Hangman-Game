import game_logic

def main():
    print(game_logic.rules)

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