import tkinter as tk
from tkinter import ttk
import random


class OddEvenGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo dos Números Ímpares e Pares")

        self.score = 0
        self.rounds_played = 0
        self.max_rounds = 10

        self.label = ttk.Label(self.root, text="Selecione se o número mostrado é par ou ímpar:")
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        self.choice_frame = ttk.LabelFrame(self.root, text="Escolha:")
        self.choice_frame.pack(pady=5)

        self.even_button = ttk.Button(self.choice_frame, text="Par", command=lambda: self.make_choice("Even"))
        self.even_button.grid(row=0, column=0, padx=5, pady=5)

        self.odd_button = ttk.Button(self.choice_frame, text="Ímpar", command=lambda: self.make_choice("Odd"))
        self.odd_button.grid(row=0, column=1, padx=5, pady=5)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.play_button = ttk.Button(self.root, text="Jogar Novamente", state=tk.DISABLED, command=self.play_again)
        self.play_button.pack(pady=5)

        self.quit_button = ttk.Button(self.root, text="Sair", command=self.root.quit)
        self.quit_button.pack(pady=5)

        self.play()

    def play(self):
        if self.rounds_played < self.max_rounds:
            self.rounds_played += 1
            number = random.randint(1, 10)

            self.canvas.delete("all")
            img = tk.PhotoImage(file=f"num_{number}.png")
            self.canvas.create_image(150, 150, image=img, anchor="center")
            self.canvas.image = img
            self.current_number = number
        else:
            self.result_label.config(text=f"Parabéns! Você fez {self.score} pontos.")
            self.even_button.config(state=tk.DISABLED)
            self.odd_button.config(state=tk.DISABLED)
            self.play_button.config(state=tk.NORMAL)

    def make_choice(self, choice):
        if hasattr(self, 'current_number'):
            number = self.current_number
            if (number % 2 == 0 and choice == "Even") or (number % 2 != 0 and choice == "Odd"):
                self.score += 10
            self.result_label.config(text=f"Resultado: {self.score} pontos")
            self.play()

    def play_again(self):
        self.score = 0
        self.rounds_played = 0
        self.result_label.config(text="")
        self.even_button.config(state=tk.NORMAL)
        self.odd_button.config(state=tk.NORMAL)
        self.play_button.config(state=tk.DISABLED)
        self.play()


root = tk.Tk()
game = OddEvenGame(root)
root.mainloop()