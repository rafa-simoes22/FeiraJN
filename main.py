import tkinter as tk
import subprocess

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogos")


        self.play_button = tk.Button(root, text="Jogar", command=self.show_games)
        self.play_button.pack()

    def show_games(self):
        self.play_button.pack_forget()  # Esconde o botão Jogar

        self.game1_button = tk.Button(root, text="Jogo 1", command=self.run_game1)
        self.game1_button.pack()

        self.game2_button = tk.Button(root, text="Jogo 2", command=self.run_game2)
        self.game2_button.pack()

        self.back_button = tk.Button(root, text="Voltar", command=self.show_play_button)
        self.back_button.pack()

    def run_game1(self):
        subprocess.run(["python", "game.py"])  # Executa o código do game.py

    def run_game2(self):
        subprocess.run(["python", "game2.py"])  # Executa o código do game2.py

    def show_play_button(self):
        self.game1_button.pack_forget()
        self.game2_button.pack_forget()
        self.back_button.pack_forget()
        self.play_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
