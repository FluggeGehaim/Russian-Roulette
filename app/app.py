import tkinter as tk
from tkinter import messagebox
import time
from .config import COLORS, FONTS
from .utils import check_your_luck

class TryYourLuckApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        self.setup_bindings()

    def setup_window(self):
        self.root.title("Russian Roulette!")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        self.root.configure(bg=COLORS["bg"])
        self.root.eval('tk::PlaceWindow . center')

    def create_widgets(self):
        self.title = tk.Label(
            self.root,
            text="Крутите барабан",
            font=FONTS["title"],
            bg=COLORS["bg"],
            fg="#333"
        )
        self.title.pack(pady=20)

        self.button = tk.Button(
            self.root,
            text="Спустить курок!",
            command=self.on_click,
            bg=COLORS["button_bg"],
            fg=COLORS["text"],
            font=FONTS["default"],
            padx=30,
            pady=15,
            borderwidth=0,
            relief=tk.RAISED
        )
        self.button.pack(pady=50)

    def setup_bindings(self):
        self.button.bind("<Enter>", lambda e: self.button.config(bg=COLORS["button_hover"]))
        self.button.bind("<Leave>", lambda e: self.button.config(bg=COLORS["button_bg"]))

    def on_click(self):
        if check_your_luck():
            self.handle_win()
        else:
            messagebox.showinfo("Результат", "Попробуйте ещё раз!")

    def handle_win(self):      # Анимация
        self.play_win_animation()
        

    def play_win_animation(self):
        for _ in range(6):
            self.button.config(bg=COLORS["win"])
            self.root.update()
            time.sleep(0.15)
            self.button.config(bg=COLORS["button_bg"])
            self.root.update()
            time.sleep(0.15)