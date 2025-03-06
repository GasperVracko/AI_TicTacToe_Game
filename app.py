import customtkinter as ctk
from screens.menu import MenuScreen
from screens.settings import SettingsScreen
from screens.game import GameScreen

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

        self.show_page("MenuScreen")

    def show_page(self, page_name):
        frame = self.pages[page_name]
        frame.tkraise()