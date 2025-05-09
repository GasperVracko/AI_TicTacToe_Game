import customtkinter as ctk

class SettingsScreen(ctk.CTkFrame):
    def __init__(self, parent, controller, config):
        super().__init__(parent)
        self.controller = controller
        self.config = config

        self.grid_columnconfigure((0,2), weight=1, uniform="a")
        self.grid_rowconfigure((0,8), weight=1, uniform="a")

        # Title
        self.title = ctk.CTkLabel(self, text="Settings", font=("Copperplate Gothic Bold", 40, "bold"))
        self.title.grid(row=1, column=1, pady=20)

        # AI Algorithm
        self.ai_algorithm_container = ctk.CTkFrame(self, fg_color="transparent")
        self.ai_algorithm_container.grid(row=2, column=1, pady=10)

        self.ai_algorithm_label = ctk.CTkLabel(self.ai_algorithm_container, text="AI Algorithm:", font=("Copperplate Gothic Light", 28, "bold"))
        self.ai_algorithm_label.grid(row=0, column=1, pady=0)

        self.ai_algorithm_var = ctk.StringVar(value=self.config.get('Settings', 'ai_algorithm'))
        self.ai_algorithm_menu = ctk.CTkOptionMenu(self.ai_algorithm_container, variable=self.ai_algorithm_var, values=["Minimax", "Alpha-Beta"], font=("Copperplate Gothic Light", 20, "bold"), width=200, height=30,)
        self.ai_algorithm_menu.grid(row=1, column=1, pady=5)

        # Difficulty
        self.difficulty_container = ctk.CTkFrame(self, fg_color="transparent")
        self.difficulty_container.grid(row=3, column=1, pady=10)

        self.difficulty_label = ctk.CTkLabel(self.difficulty_container, text="Difficulty:", font=("Copperplate Gothic Light", 28, "bold"))
        self.difficulty_label.grid(row=0, column=1, pady=0)

        self.difficulty_var = ctk.IntVar(value=self.config.get('Settings', 'difficulty'))
        self.difficulty_menu = ctk.CTkOptionMenu(self.difficulty_container, variable=self.difficulty_var, values=["1","2","3","4","5","6","7","8","9"], font=("Copperplate Gothic Light", 20, "bold"), width=200, height=30,)
        self.difficulty_menu.grid(row=1, column=1, pady=5)

        # Checkbox for aggressive AI
        self.ai_strategy_var = ctk.BooleanVar(value=self.config.getboolean('Settings', 'ai_strategy'))
        self.ai_strategy_checkbox = ctk.CTkCheckBox(self, text="Aggressive AI", variable=self.ai_strategy_var, font=("Copperplate Gothic Light", 24, "bold"))
        self.ai_strategy_checkbox.grid(row=4, column=1, pady=10)

        # Checkbox for AI player
        self.ai_var = ctk.BooleanVar(value=self.config.getboolean('Settings', 'ai_player'))
        self.ai_checkbox = ctk.CTkCheckBox(self, text="AI Player", variable=self.ai_var, font=("Copperplate Gothic Light", 24, "bold"))
        self.ai_checkbox.grid(row=5, column=1, pady=10)


        # Back Button
        self.BackBtn = ctk.CTkButton(self, text="Back", font=("Copperplate Gothic Light", 24, "bold"), width=150, height=40, command=self.save_settings)
        self.BackBtn.grid(row=6, column=1, pady=25)

    def save_settings(self):
        self.config.set('Settings', 'ai_algorithm', self.ai_algorithm_var.get())
        self.config.set('Settings', 'difficulty', str(self.difficulty_var.get()))
        self.config.set('Settings', 'ai_strategy', str(self.ai_strategy_var.get()))
        self.config.set('Settings', 'ai_player', str(self.ai_var.get()))

        with open("config.ini", "w") as configfile:
            self.config.write(configfile)

        self.controller.show_page("MenuScreen")