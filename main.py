import configparser
import customtkinter as ctk
from app import App

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

config = configparser.ConfigParser()
config.read("config.ini")

if __name__ == "__main__":
    app = App(config)
    app.mainloop()
