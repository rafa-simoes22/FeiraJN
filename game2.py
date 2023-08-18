import tkinter as tk
import random

try:
    from PIL import Image, ImageTk
except ImportError:
    import Image
    import ImageTk

class JogoDaSoma:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Soma com Imagens")

        self.pontuacao = 0
        self.rodada_atual = 1
        self.max_rodadas = 10

        self.label = tk.Label(root, text="Selecione a opção que representa a soma dos números:")
        self.label.pack(pady=10)

        self.image_frame = tk.Frame(root)
        self.image_frame.pack()

        self.image_label1 = tk.Label(self.image_frame)
        self.image_label2 = tk.Label(self.image_frame)
        self.plus_label = tk.Label(self.image_frame, text="+")

        self.image_label1.pack(side=tk.LEFT, padx=10)
        self.plus_label.pack(side=tk.LEFT)
        self.image_label2.pack(side=tk.LEFT, padx=10)

        self.feedback_label = tk.Label(root, text="")
        self.feedback_label.pack(pady=5)

        self.pontuacao_label = tk.Label(root, text="Pontuação: 0")
        self.pontuacao_label.pack()

        self.opcao_buttons = []

        self.imagens = [self.get_image(num) for num in range(1, 11)]

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
            self.feedback_label.config(text="")

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
            button.pack(pady=5)
            self.opcao_buttons.append(button)

    def selecionar_opcao(self, opcao):
        if opcao == self.resposta_correta:
            self.pontuacao += 10
            self.feedback_label.config(text="Resposta correta! +10 pontos")
        else:
            self.feedback_label.config(text="Resposta incorreta. Tente novamente.")

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

        self.image_frame.pack_forget()
        self.feedback_label.config(text=f"Jogo finalizado! Sua pontuação final: {self.pontuacao}")

        self.botao_jogar_novamente = tk.Button(self.root, text="Jogar Novamente", command=self.reiniciar_jogo)
        self.botao_jogar_novamente.pack(pady=10)

    def reiniciar_jogo(self):
        self.pontuacao = 0
        self.rodada_atual = 1

        self.feedback_label.config(text="")
        self.botao_jogar_novamente.pack_forget()

        self.image_frame.pack()
        self.nova_rodada()
        self.atualizar_pontuacao()


root = tk.Tk()
jogo = JogoDaSoma(root)
root.mainloop()