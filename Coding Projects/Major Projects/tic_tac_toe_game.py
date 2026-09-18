from tkinter import * # type: ignore
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.geometry("400x450")

current_player = "X"
board = [""] * 9
buttons = []


def check_winner():
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in winning_combos:
        a, b, c = combo

        if board[a] == board[b] == board[c] != "":
            messagebox.showinfo("Winner!", f"Player {board[a]} wins!")
            reset_game()
            return

    if "" not in board:
        messagebox.showinfo("Draw!", "It's a draw!")
        reset_game()


def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        check_winner()

        if "" in board:
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

            player_label.config(text=f"Player: {current_player}")


def reset_game():
    global current_player, board

    current_player = "X"
    board = [""] * 9

    for button in buttons:
        button.config(text="")

    player_label.config(text="Player: X")


Label(
    root,
    text="Tic Tac Toe",
    font=("Arial", 20, "bold")
).pack(pady=10)

player_label = Label(
    root,
    text="Player: X",
    font=("Arial", 14)
)

player_label.pack()


# Create a frame for the game board
game_frame = Frame(root)
game_frame.pack(pady=10)

for row in range(3):
    for col in range(3):

        index = row * 3 + col

        btn = Button(
            game_frame,
            text="",
            font=("Arial", 20, "bold"),
            width=5,
            height=2,
            command=lambda i=index: button_click(i)
        )

        btn.grid(row=row, column=col)
        buttons.append(btn)


Button(
    root,
    text="Restart Game",
    font=("Arial", 12),
    command=reset_game
).pack(pady=10)

root.mainloop()