import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageTk



class OddEvenGame:
    def __init__(self, root, main_interface):
        self.root = root
        self.main_interface = main_interface

        self.root.title("Números Ímpares e Pares")

        # Impedir redimensionamento e maximização
        self.root.resizable(False, False)

        # Configurar tamanho inicial da janela
        self.root.geometry("350x500")  # Ajuste para o tamanho desejado

        # Carregar a imagem de fundo
        background_image = Image.open("jogo_1.png")
        self.background_photo = ImageTk.PhotoImage(background_image)

        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.score = 0
        self.rounds_played = 0
        self.max_rounds = 10

        self.label = ttk.Label(self.root, text="Selecione se o número mostrado é par ou ímpar:", style="Custom.TLabel")

        self.label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        style = ttk.Style()
        style.configure("Custom.TLabel", background="light yellow", foreground="black", font=("Arial", 10))

        style.configure("Custom.TLabelframe", background="light yellow")

        style.configure("Custom.TLabelframe.Label", background="light yellow", font=("Arial", 10))

        style.configure("Custom.TButton", background="black")

        self.choice_frame = ttk.LabelFrame(self.root, text="Escolha:", style="Custom.TLabelframe")
        self.choice_frame.label = ttk.Label(self.choice_frame, text="Escolha:", style="Custom.TLabelframe.Label")

        self.choice_frame.pack(pady=5)

        self.even_button = ttk.Button(self.choice_frame, text="Par", style="Custom.TButton", command=lambda: self.make_choice("Even"))
        self.even_button.grid(row=0, column=0, padx=5, pady=5)

        self.odd_button = ttk.Button(self.choice_frame, text="Ímpar", style="Custom.TButton", command=lambda: self.make_choice("Odd"))
        self.odd_button.grid(row=0, column=1, padx=5, pady=5)

        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        self.play_button = ttk.Button(self.root, text="Jogar Novamente", style="Custom.TButton", state=tk.DISABLED, command=self.play_again)
        self.play_button.pack(pady=5)

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
            self.result_label.config(text=f"Parabéns! Você fez {self.score} pontos.", style="Custom.TLabel")
            self.even_button.config(state=tk.DISABLED)
            self.odd_button.config(state=tk.DISABLED)
            self.play_button.config(state=tk.NORMAL)


    def make_choice(self, choice):
        if hasattr(self, 'current_number'):
            number = self.current_number
            if (number % 2 == 0 and choice == "Even") or (number % 2 != 0 and choice == "Odd"):
                self.score += 10
            self.result_label.config(text=f"Pontuação: {self.score} ", style="Custom.TLabel")
            self.play()

    def play_again(self):
        self.score = 0
        self.rounds_played = 0
        self.result_label.config(text="")
        self.even_button.config(state=tk.NORMAL)
        self.odd_button.config(state=tk.NORMAL)
        self.play_button.config(state=tk.DISABLED)
        self.play()

    def close_game(self):
        self.root.destroy()
        self.main_interface.show_menu()
        self.main_interface.game_in_progress = False


class JogoDaSoma:
    def __init__(self, root, main_interface):
        self.root = root
        self.main_interface = main_interface

        self.root.title("Soma com Imagens")

        # Impedir redimensionamento e maximização
        self.root.resizable(False, False)

        # Configurar tamanho inicial da janela
        self.root.geometry("400x400")  # Ajuste para o tamanho desejado

        # Carregar a imagem de fundo
        background_image = Image.open("jogo_2.png")
        self.background_photo = ImageTk.PhotoImage(background_image)

        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        self.pontuacao = 0
        self.rodada_atual = 1
        self.max_rodadas = 10


        self.label = tk.Label(root, text="Selecione a opção que representa a soma dos números:", background="light yellow", foreground="black", font=("Arial", 10))
        self.label.pack(pady=10)

        self.image_label1 = tk.Label(root)
        self.image_label2 = tk.Label(root)

        self.image_label1.place(x=20, y=100)
        self.image_label2.place(x=230, y=100)

        self.feedback_label = tk.Label(root)

        self.pontuacao_label = tk.Label(root, text="Pontuação: 0", background="light yellow", foreground="black", font=("Arial", 10))
        self.pontuacao_label.pack()

        self.opcao_buttons = []

        self.imagens = [self.get_image(num) for num in range(1, 11)]

        self.botao_jogar_novamente = tk.Button(root, text="Jogar Novamente", command=self.reiniciar_jogo)
        self.resultado_label = tk.Label(root, text="", background="light yellow")

        self.nova_rodada()

    def nova_rodada(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        self.resposta_correta = num1 + num2

        self.image_label1.config(image=self.imagens[num1 - 1])
        self.image_label2.config(image=self.imagens[num2 - 1])

        self.opcoes = [self.resposta_correta]

        while len(self.opcoes) < 3:
            opcao = random.randint(2, 20)
            if opcao != self.resposta_correta and opcao not in self.opcoes:
                self.opcoes.append(opcao)

        random.shuffle(self.opcoes)

        self.atualizar_opcoes()

        if self.rodada_atual > self.max_rodadas:
            self.mostrar_resultado_final()
        else:
            self.feedback_label.config()

    def get_image(self, num):
        filename = f"{num}.png"
        image = Image.open(filename)
        image = image.resize((150, 150))
        image = ImageTk.PhotoImage(image)
        return image

    def atualizar_opcoes(self):
        for button in self.opcao_buttons:
            button.destroy()

        self.opcao_buttons = []


        for opcao in self.opcoes:
            button = tk.Button(self.root, text=str(opcao), command=lambda opcao=opcao: self.selecionar_opcao(opcao))
            button.pack(pady=10)
            self.opcao_buttons.append(button)

    def selecionar_opcao(self, opcao):
        if opcao == self.resposta_correta:
            self.pontuacao += 10
            self.feedback_label.config()
        else:
            self.feedback_label.config()

        self.rodada_atual += 1
        self.atualizar_pontuacao()

        if self.rodada_atual > self.max_rodadas:
            self.mostrar_resultado_final()
        else:
            self.nova_rodada()

    def atualizar_pontuacao(self):
        self.pontuacao_label.config(text=f"Pontuação: {self.pontuacao}")

    def mostrar_resultado_final(self):
        for button in self.opcao_buttons:
            button.destroy()

        self.image_label1.place_forget()
        self.image_label2.place_forget()
        resultado_texto = f"Parabéns! Você fez {self.pontuacao} pontos."
        self.pontuacao_label.config(text=resultado_texto, background="light yellow", foreground="black", font=("Arial", 10))
        self.botao_jogar_novamente.pack(pady=10)

    def reiniciar_jogo(self):
        self.pontuacao = 0
        self.rodada_atual = 1

        self.botao_jogar_novamente.pack_forget()

        self.image_label1.place(x=20, y=100)
        self.image_label2.place(x=230, y=100)
        self.nova_rodada()
        self.atualizar_pontuacao()

    def close_game(self):
        self.root.destroy()
        self.main_interface.show_menu()
        self.main_interface.game_in_progress = False


class MainInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Mate-Magia Especial")


        # Impedir redimensionamento e maximização
        self.root.resizable(False, False)

        # Configurar tamanho inicial da janela
        self.root.geometry("1000x1000")  # Ajuste para o tamanho desejado

        # Carregar a imagem de fundo
        background_image = Image.open("Interface.png")
        self.background_photo = ImageTk.PhotoImage(background_image)

        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)

        style = ttk.Style()
        style.configure("Custom.TButton", background="black")

        self.play_button = ttk.Button(self.root, text="JOGAR", style="Custom.TButton", command=self.choose_game)
        self.play_button.pack(pady=80)

        self.game_in_progress = False

    def choose_game(self):
        self.play_button.pack_forget()

        self.game1_button = ttk.Button(self.root, text="JOGO 1-Números Ímpares e Pares", style="Custom.TButton", command=self.play_game1)
        self.game1_button.pack()

        self.game2_button = ttk.Button(self.root, text="JOGO 2-Soma com Imagens", style="Custom.TButton",  command=self.play_game2)
        self.game2_button.pack()

    def play_game1(self):
        if not self.game_in_progress:
            self.hide_buttons()
            self.game_in_progress = True
            game_root = tk.Toplevel(self.root)
            self.game_window = OddEvenGame(game_root, self)
            game_root.protocol("WM_DELETE_WINDOW", self.game_window.close_game)

    def play_game2(self):
        if not self.game_in_progress:
            self.hide_buttons()
            self.game_in_progress = True
            game_root = tk.Toplevel(self.root)
            self.game_window = JogoDaSoma(game_root, self)
            game_root.protocol("WM_DELETE_WINDOW", self.game_window.close_game)

    def hide_buttons(self):
        self.game1_button.pack_forget()
        self.game2_button.pack_forget()

    def show_menu(self):
        self.game_window = None
        self.play_button.pack()




root = tk.Tk()
main_interface = MainInterface(root)
root.geometry("300x200")
icon_path = "icone.ico"
ico = Image.open(icon_path)
icon_photo = ImageTk.PhotoImage(ico)
root.iconphoto(True, icon_photo)
root.mainloop()