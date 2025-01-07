import random


def roll_dice():
    """Simulate rolling a single die."""
    return random.randint(1, 6)


def play_ludo(num_players):
    """Simulate a Ludo game for the given number of players."""
    print("Welcome to the Virtual Ludo Dice Game!")
    print(f"Number of players: {num_players}\n")

    scores = [0] * num_players  # Initialize scores for each player
    rounds = 10  # Number of rounds to play

    for round_num in range(1, rounds + 1):
        print(f"--- Round {round_num} ---")
        for player in range(num_players):
            print(f"Player {player + 1}'s turn:")
            dice_value = roll_dice()
            print(f"  Rolled: {dice_value}")

            # Scoring rules
            if dice_value == 6:
                print("  Bonus turn! Rolling again...")
                bonus_value = roll_dice()
                print(f"  Bonus roll: {bonus_value}")
                scores[player] += dice_value + bonus_value
            else:
                scores[player] += dice_value

            print(f"  Total score: {scores[player]}\n")

    # Determine the winner
    max_score = max(scores)
    winners = [i + 1 for i, score in enumerate(scores) if score == max_score]

    print("--- Final Scores ---")
    for player, score in enumerate(scores, start=1):
        print(f"Player {player}: {score}")

    if len(winners) == 1:
        print(f"\nWinner: Player {winners[0]}!")
    else:
        print(f"\nIt's a tie between players: {', '.join(map(str, winners))}!")


# Run the game
num_players = int(input("Enter the number of players (2-4): "))
if 2 <= num_players <= 4:
    play_ludo(num_players)
else:
    print("Invalid number of players. Please enter between 2 and 4.")
