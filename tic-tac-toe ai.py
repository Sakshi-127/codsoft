import random

# Initialize the board
board = [" " for _ in range(9)]

# Display the board
def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print("\n")

# Check if someone has won
def check_winner(b, player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # columns
        [0,4,8], [2,4,6]           # diagonals
    ]
    for combo in win_combinations:
        if all(b[i] == player for i in combo):
            return True
    return False

# Check for draw
def is_draw():
    return " " not in board

# Get available moves
def available_moves():
    return [i for i in range(9) if board[i] == " "]

# AI move logic (simple strategy)
def ai_move():
    # 1. Win if possible
    for move in available_moves():
        board_copy = board[:]
        board_copy[move] = "O"
        if check_winner(board_copy, "O"):
            return move

    # 2. Block player win
    for move in available_moves():
        board_copy = board[:]
        board_copy[move] = "X"
        if check_winner(board_copy, "X"):
            return move

    # 3. Take center if available
    if 4 in available_moves():
        return 4

    # 4. Pick a random corner
    corners = [i for i in [0,2,6,8] if i in available_moves()]
    if corners:
        return random.choice(corners)

    # 5. Pick any random move
    return random.choice(available_moves())

# Main game loop
def play_game():
    print("🎮 Welcome to Tic Tac Toe!")
    print("You are X. AI is O.")
    print_board()

    while True:
        # Player move
        try:
            move = int(input("Enter your move (0-8): "))
            if board[move] != " ":
                print("That spot is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 0-8.")
            continue

        board[move] = "X"
        print_board()

        if check_winner(board, "X"):
            print("🎉 You win!")
            break
        elif is_draw():
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai = ai_move()
        board[ai] = "O"
        print_board()

        if check_winner(board, "O"):
            print("💻 AI wins!")
            break
        elif is_draw():
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
