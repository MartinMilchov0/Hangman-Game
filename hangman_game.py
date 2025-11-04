import game_logic

def main():
    print(game_logic.rules)

    start_game = input("Would you like to begin? (Y for Yes/ Anything else for No): ").upper()
    if start_game != 'Y':
        print("Maybe next time!")
        return

    total_score = 0
    play_again = 'Y'

    while play_again == 'Y':
        score = game_logic.play_game()
        total_score += score
        print("Score:", score)
        print("Total Score:", total_score)

        play_again = input("Would you like to play again? (Y/N): ").upper()
        while play_again not in ('Y', 'N'):
            play_again = input("Please respond with Y or N: ").upper()

    print("Thank you for playing!")


if __name__ == "__main__":
    main()