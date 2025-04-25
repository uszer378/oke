#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")

        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = []

        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(
                    master,
                    text="",
                    font=("Arial", 40),
                    width=2,
                    height=1,
                    command=lambda row=i, col=j: self.make_move(row, col),
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(self.current_player):
                self.announce_winner(self.current_player)
                self.disable_buttons()
            elif self.check_tie():
                self.announce_tie()
                self.disable_buttons()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, player):
        # Check rows
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        # Check diagonals
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_tie(self):
        return all(cell != "" for row in self.board for cell in row)

    def announce_winner(self, winner):
        messagebox.showinfo("Game Over", f"Player {winner} wins!")

    def announce_tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")

    def disable_buttons(self):
        for row_buttons in self.buttons:
            for button in row_buttons:
                button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    gui = TicTacToeGUI(root)
    root.mainloop()
