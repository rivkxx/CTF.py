import random

# Initialize game variables
team_1_flag = random.randint(1, 10)  # Flag position for team 1
team_2_flag = random.randint(11, 20)  # Flag position for team 2

team_1_score = 0  # Team 1's score
team_2_score = 0  # Team 2's score

# Function to display the game board
def display_board():
    print("\nCapture the Flag Game")
    print("-" * 20)
    print("Team 1 Flag: [{}]  Team 1 Score: {}".format("*" if team_1_flag == 0 else " ", team_1_score))
    print("Team 2 Flag: [{}]  Team 2 Score: {}".format("*" if team_2_flag == 10 else " ", team_2_score))
    print("-" * 20)

# Main game loop
while True:
    display_board()

    # Get player moves
    try:
        team_1_move = int(input("Team 1, enter your move (1-10): "))
        team_2_move = int(input("Team 2, enter your move (11-20): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    # Check if Team 1 captured Team 2's flag
    if team_1_move == team_2_flag:
        team_1_score += 1
        team_2_flag = 0
        print("Team 1 captured Team 2's flag!")

    # Check if Team 2 captured Team 1's flag
    if team_2_move == team_1_flag:
        team_2_score += 1
        team_1_flag = 10
        print("Team 2 captured Team 1's flag!")

    # Check for a winner
    if team_1_score == 3:
        display_board()
        print("Team 1 wins!")
        break
    elif team_2_score == 3:
        display_board()
        print("Team 2 wins!")
        break

print("Game Over")
