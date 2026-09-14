from tkinter import * # type: ignore
from tkinter import messagebox

# Main window
root = Tk()
root.title("Tic Tac Toe")
root.geometry("320x380")

# Variables
current_player = "X"
board = [""] * 9

# Check winner
def check_winner():
    winning_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]

    for combo in winning_combinations:
        a, b, c = combo

        if board[a] == board[b] == board[c] != "":
            messagebox.showinfo("Winner!", f"Player {board[a]} wins!")
            reset_game()
            return

    if "" not in board:
        messagebox.showinfo("Draw!", "It's a Draw!")
        reset_game()

# Button click
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        check_winner()

        current_player = "O" if current_player == "X" else "X"
        player_label.config(text=f"Player: {current_player}")

# Reset game
def reset_game():
    global current_player, board

    current_player = "X"
    board = [""] * 9

    for button in buttons:
        button.config(text="")

    player_label.config(text="Player: X")

# Title
Label(root, text="Tic Tac Toe",
      font=("Arial", 20, "bold")).pack(pady=10)

# Player Label
player_label = Label(root, text="Player: X",
                     font=("Arial", 14))
player_label.pack()

# Frame for board
frame = Frame(root)
frame.pack(pady=10)

buttons = []

for row in range(3):
    for col in range(3):
        index = row * 3 + col

        btn = Button(
            frame,
            text="",
            font=("Arial", 20, "bold"),
            width=5,
            height=2,
            command=lambda i=index: button_click(i)
        )

        btn.grid(row=row, column=col)
        buttons.append(btn)

# Reset Button
Button(root,
       text="Restart Game",
       font=("Arial", 12),
       command=reset_game).pack(pady=10)

root.mainloop()