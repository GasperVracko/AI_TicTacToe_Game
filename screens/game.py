import customtkinter as ctk

class GameScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

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

    def on_board_btn_click(self, row, column):
        if self.board_state[row][column] == "":
            self.board_state[row][column] = self.current_player
            self.buttons[row][column].configure(text=self.current_player)
            self.current_player = "O" if self.current_player == "X" else "X"

    def on_reset(self):
        self.board_state = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="")