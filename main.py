import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("AI-Powered Tic Tac Toe")
        self.geometry("400x600")

        # Create a container frame to hold all pages
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Initialize pages
        self.pages = {}
        for Page in (MenuScreen, SettingsScreen, GameScreen):
            page_name = Page.__name__
            frame = Page(parent=self.container, controller=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Stack all pages on top of each other

        # Show the initial page
        self.show_page("MenuScreen")

    def show_page(self, page_name):
        """Show the specified page and hide others."""
        frame = self.pages[page_name]
        frame.tkraise()  # Bring the selected page to the top


class MenuScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure the frame to expand
        self.grid_columnconfigure(0, weight=1, uniform="a")
        self.grid_rowconfigure((0,5), weight=1, uniform="a")

        self.title = ctk.CTkLabel(self, text="MENU", font=("Copperplate Gothic Bold", 40, "bold"))
        self.title.grid(row=1, column=0, pady=20)

        self.GameBtn = ctk.CTkButton(self, text="Tic Tac Toe",font=("Copperplate Gothic Light", 24, "bold"), width=200, height=40, command=lambda: controller.show_page("GameScreen"))
        self.GameBtn.grid(row=2, column=0, pady=10)

        self.SettingsBtn = ctk.CTkButton(self, text="Settings", font=("Copperplate Gothic Light", 24, "bold"), width=200, height=40, command=lambda: controller.show_page("SettingsScreen"))
        self.SettingsBtn.grid(row=3, column=0, pady=10)

        self.ExitBtn = ctk.CTkButton(self, text="Exit", font=("Copperplate Gothic Light", 24, "bold"), width=200, height=40, command=self.quit)
        self.ExitBtn.grid(row=4, column=0, pady=10)


class SettingsScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure the frame to expand
        self.grid_columnconfigure((0,2), weight=1, uniform="a")
        self.grid_rowconfigure((0,8), weight=1, uniform="a")

        self.title = ctk.CTkLabel(self, text="Settings", font=("Copperplate Gothic Bold", 40, "bold"))
        self.title.grid(row=1, column=1, pady=20)

        # AI Algorithm
        self.ai_algorithm_container = ctk.CTkFrame(self, fg_color="transparent")
        self.ai_algorithm_container.grid(row=2, column=1, pady=10)

        self.ai_algorithm_label = ctk.CTkLabel(self.ai_algorithm_container, text="AI Algorithm:", font=("Copperplate Gothic Light", 28, "bold"))
        self.ai_algorithm_label.grid(row=0, column=1, pady=0)

        self.ai_algorithm_var = ctk.StringVar(value="Minimax")
        self.ai_algorithm_menu = ctk.CTkOptionMenu(self.ai_algorithm_container, variable=self.ai_algorithm_var, values=["Minimax", "Alpha-Beta"], font=("Copperplate Gothic Light", 20, "bold"), width=200, height=30,)
        self.ai_algorithm_menu.grid(row=1, column=1, pady=5)

        # Difficulty
        self.difficulty_container = ctk.CTkFrame(self, fg_color="transparent")
        self.difficulty_container.grid(row=3, column=1, pady=10)

        self.difficulty_label = ctk.CTkLabel(self.difficulty_container, text="Difficulty:", font=("Copperplate Gothic Light", 28, "bold"))
        self.difficulty_label.grid(row=0, column=1, pady=0)

        self.difficulty_var = ctk.StringVar(value="Medium")
        self.difficulty_menu = ctk.CTkOptionMenu(self.difficulty_container, variable=self.difficulty_var, values=["Easy", "Medium", "Hard"], font=("Copperplate Gothic Light", 20, "bold"), width=200, height=30,)
        self.difficulty_menu.grid(row=1, column=1, pady=5)

        # Checkbox for AI player
        self.ai_var = ctk.BooleanVar(value=False)
        self.ai_checkbox = ctk.CTkCheckBox(self, text="AI Player", variable=self.ai_var, font=("Copperplate Gothic Light", 24, "bold"))
        self.ai_checkbox.grid(row=4, column=1, pady=10)

        self.BackBtn = ctk.CTkButton(self, text="Back", font=("Copperplate Gothic Light", 24, "bold"), width=150, height=40, command=lambda: controller.show_page("MenuScreen"))
        self.BackBtn.grid(row=5, column=1, pady=25)


class GameScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure the frame to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(self, text="About Page", font=("Arial", 24))
        label.grid(row=0, column=0, pady=20, sticky="nsew")

        button = ctk.CTkButton(self, text="Go to Home", command=lambda: controller.show_page("MenuScreen"))
        button.grid(row=1, column=0, pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
