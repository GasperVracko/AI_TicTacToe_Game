import customtkinter as ctk

class MenuScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_columnconfigure(0, weight=1, uniform="a")
        self.grid_rowconfigure((0,5), weight=1, uniform="a")

        # Title
        self.title = ctk.CTkLabel(self, text="MENU", font=("Copperplate Gothic Bold", 40, "bold"))
        self.title.grid(row=1, column=0, pady=20)

        # Game Button
        self.GameBtn = ctk.CTkButton(self, text="Tic Tac Toe",font=("Copperplate Gothic Light", 24, "bold"), width=200, height=40, command=lambda: controller.show_page("GameScreen"))
        self.GameBtn.grid(row=2, column=0, pady=10)

        # Settings Button
        self.SettingsBtn = ctk.CTkButton(self, text="Settings", font=("Copperplate Gothic Light", 24, "bold"), width=200, height=40, command=lambda: controller.show_page("SettingsScreen"))
        self.SettingsBtn.grid(row=3, column=0, pady=10)

        # Exit Button
        self.ExitBtn = ctk.CTkButton(self, text="Exit", font=("Copperplate Gothic Light", 24, "bold"), width=200, height=40, command=self.quit)
        self.ExitBtn.grid(row=4, column=0, pady=10)