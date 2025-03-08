from cgitb import enable

import customtkinter as ctk
from ai_algorithms import minimax, alpha_beta_pruning

class GameScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, config):
        super().__init__(parent)
        self.controller = controller
        self.config = config
        self.result_message = None
        self.turn = True

        # Configure the frame to expand
        self.grid_rowconfigure((0,6), weight=1, uniform="a")
        self.grid_columnconfigure((0,4), weight=1, uniform="a")

        # Title
        self.title = ctk.CTkLabel(self, text="Tic Tac Toe", font=("Copperplate Gothic Bold", 40, "bold"))
        self.title.grid(row=1, column=0,pady=20, columnspan=5)

        # Game board
        self.board = ctk.CTkFrame(self, fg_color="transparent")
        self.board.grid(row=2, column=1, columnspan=3, rowspan=3, pady=10)

        self.board.grid_rowconfigure((0,1,2), weight=1, uniform="a")
        self.board.grid_columnconfigure((0,1,2), weight=1, uniform="a")

        # Buttons for the game board
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = ctk.CTkButton(self.board, text="", font=("Copperplate Gothic Light", 64, "bold"), width=90, height=90, command=lambda rw=i, col=j: self.on_board_btn_click(rw, col))
                button.grid(row=i, column=j, pady=1, padx=1, sticky="nsew")
                row.append(button)
            self.buttons.append(row)

        # Reset Button
        self.ResetBtn = ctk.CTkButton(self, text="Reset", font=("Copperplate Gothic Light", 24, "bold"), width=100, height=40, command=lambda: self.on_reset())
        self.ResetBtn.grid(row=5, column=1, pady=25, padx=10)

        # Back Button
        self.BackBtn = ctk.CTkButton(self, text="Back", font=("Copperplate Gothic Light", 24, "bold"), width=100, height=40, command=lambda: controller.show_page("MenuScreen"))
        self.BackBtn.grid(row=5, column=3, pady=25, padx=10)

        # Initialize game state
        self.current_player = "X"
        self.board_state = [["" for _ in range(3)] for _ in range(3)]

    # Button click event handler
    def on_board_btn_click(self, row, column):
        if self.board_state[row][column] == "":
            self.board_state[row][column] = self.current_player
            self.buttons[row][column].configure(text=self.current_player, state="disabled")
            if self.check_winner():
                self.display_result_message(self.current_player)
            elif all(self.board_state[i][j] != "" for i in range(3) for j in range(3)):
                self.display_result_message()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O" and self.config.getboolean('Settings', 'ai_player'):
                    self.ai_move()

    # Helper AI function
    def ai_move(self):
        if self.config.get('Settings', 'ai_algorithm') == "Minimax":
            _, move = minimax(self.board_state, int(self.config.get('Settings', 'difficulty')), True, bool(self.config.getboolean('Settings', 'ai_strategy')))
            if move:
                self.on_board_btn_click(move[0], move[1])
        elif self.config.get('Settings', 'ai_algorithm') == "Alpha-Beta":
            _, move = alpha_beta_pruning(self.board_state, int(self.config.get('Settings', 'difficulty')), True, bool(self.config.get('Settings', 'ai_strategy')), float("-inf"), float("inf"))
            if move:
                self.on_board_btn_click(move[0], move[1])
        else:
            raise ValueError("Invalid AI Algorithm")

    # Reset the game
    def on_reset(self):
        self.board_state = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        if self.result_message:
            self.result_message.destroy()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="", state="normal")

    # Check if there is a winner
    def check_winner(self):
        # Check rows
        for row in range(3):
            if self.board_state[row][0] == self.board_state[row][1] == self.board_state[row][2] != "":
                return True

        #Check columns
        for col in range(3):
            if self.board_state[0][col] == self.board_state[1][col] == self.board_state[2][col] != "":
                return True

        # Check diagonals
        if self.board_state[0][0] == self.board_state[1][1] == self.board_state[2][2] != "":
            return True
        if self.board_state[0][2] == self.board_state[1][1] == self.board_state[2][0] != "":
            return True

        # Else Return False
        return False

    # Display the result message
    def display_result_message(self, winner=None):
        if winner == "X":
            message = "Player X wins!"
        elif winner == "O":
            message = "Player O wins!"
        else:
            message = "It's a tie!"

        self.result_message = ctk.CTkLabel(self, text=message, font=("Copperplate Gothic Light", 32, "bold"), fg_color="transparent")
        self.result_message.grid(row=3, column=0, columnspan=5, ipadx=3)

