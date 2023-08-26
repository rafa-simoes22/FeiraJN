import sys
import random
from PySide6 import QtWidgets, QtGui, QtCore


class OddEvenGame(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.rounds_played = 0
        self.max_rounds = 10

        self.label = QtWidgets.QLabel("Selecione se o número mostrado é par ou ímpar:")
        self.canvas = QtWidgets.QLabel()
        self.choice_frame = QtWidgets.QGroupBox("Escolha:")
        self.even_button = QtWidgets.QPushButton("Par")
        self.odd_button = QtWidgets.QPushButton("Ímpar")
        self.result_label = QtWidgets.QLabel("")
        self.play_button = QtWidgets.QPushButton("Jogar Novamente")

        self.play_button.setEnabled(False)

        self.even_button.clicked.connect(lambda: self.make_choice("Even"))
        self.odd_button.clicked.connect(lambda: self.make_choice("Odd"))
        self.play_button.clicked.connect(self.play_again)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.canvas, alignment=QtCore.Qt.AlignCenter)

        choice_layout = QtWidgets.QHBoxLayout()
        choice_layout.addWidget(self.even_button)
        choice_layout.addWidget(self.odd_button)
        self.choice_frame.setLayout(choice_layout)
        layout.addWidget(self.choice_frame)

        layout.addWidget(self.result_label)
        layout.addWidget(self.play_button)

        self.setLayout(layout)

        self.play()

    def play(self):
        if self.rounds_played < self.max_rounds:
            self.rounds_played += 1
            number = random.randint(1, 10)
            self.current_number = number

            pixmap = QtGui.QPixmap(f"num_{number}.png")
            self.canvas.setPixmap(pixmap)

        else:
            self.result_label.setText(f"Parabéns! Você fez {self.score} pontos.")
            self.even_button.setEnabled(False)
            self.odd_button.setEnabled(False)
            self.play_button.setEnabled(True)

    def make_choice(self, choice):
        if hasattr(self, 'current_number'):
            number = self.current_number
            if (number % 2 == 0 and choice == "Even") or (number % 2 != 0 and choice == "Odd"):
                self.score += 10
            self.result_label.setText(f"Resultado: {self.score} pontos")
            self.play()

    def play_again(self):
        self.score = 0
        self.rounds_played = 0
        self.result_label.setText("")
        self.even_button.setEnabled(True)
        self.odd_button.setEnabled(True)
        self.play_button.setEnabled(False)
        self.play()


class JogoDaSoma(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.pontuacao = 0
        self.rodada_atual = 1
        self.max_rodadas = 10

        self.label = QtWidgets.QLabel("Selecione a opção que representa a soma dos números:")
        self.image_label1 = QtWidgets.QLabel()
        self.image_label2 = QtWidgets.QLabel()
        self.plus_label = QtWidgets.QLabel("+")
        self.feedback_label = QtWidgets.QLabel("")
        self.pontuacao_label = QtWidgets.QLabel("Pontuação: 0")
        self.botao_jogar_novamente = QtWidgets.QPushButton("Jogar Novamente")

        self.botao_jogar_novamente.clicked.connect(self.reiniciar_jogo)
        self.botao_jogar_novamente.hide()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)

        image_layout = QtWidgets.QHBoxLayout()
        image_layout.addWidget(self.image_label1)
        image_layout.addWidget(self.plus_label)
        image_layout.addWidget(self.image_label2)
        layout.addLayout(image_layout)

        layout.addWidget(self.feedback_label)
        layout.addWidget(self.pontuacao_label)
        layout.addWidget(self.botao_jogar_novamente)

        self.setLayout(layout)

        self.imagens = [self.get_image(num) for num in range(1, 11)]

        self.nova_rodada()

    def nova_rodada(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        self.resposta_correta = num1 + num2

        pixmap1 = QtGui.QPixmap.fromImage(self.imagens[num1 - 1])
        pixmap2 = QtGui.QPixmap.fromImage(self.imagens[num2 - 1])

        self.image_label1.setPixmap(pixmap1)
        self.image_label2.setPixmap(pixmap2)

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
            self.feedback_label.setText("")

    def get_image(self, num):
        filename = f"{num}.png"
        image = QtGui.QImage(filename)
        image = image.scaled(150, 150)
        return image

    def atualizar_opcoes(self):
        for i in reversed(range(self.layout().count())):
            item = self.layout().itemAt(i)
            if item.widget() is not None:
                item.widget().deleteLater()

        for opcao in self.opcoes:
            button = QtWidgets.QPushButton(str(opcao))
            button.clicked.connect(lambda opcao=opcao: self.selecionar_opcao(opcao))
            self.layout().addWidget(button)

    def selecionar_opcao(self, opcao):
        if opcao == self.resposta_correta:
            self.pontuacao += 10
            self.feedback_label.setText("Resposta correta! +10 pontos")
        else:
            self.feedback_label.setText("Resposta incorreta. Tente novamente.")

        self.rodada_atual += 1
        self.atualizar_pontuacao()

        if self.rodada_atual > self.max_rodadas:
            self.mostrar_resultado_final()
        else:
            self.nova_rodada()

    def atualizar_pontuacao(self):
        self.pontuacao_label.setText(f"Pontuação: {self.pontuacao}")

    def mostrar_resultado_final(self):
        self.feedback_label.setText(f"Jogo finalizado! Sua pontuação final: {self.pontuacao}")
        self.botao_jogar_novamente.show()

    def reiniciar_jogo(self):
        self.pontuacao = 0
        self.rodada_atual = 1

        self.feedback_label.setText("")
        self.botao_jogar_novamente.hide()

        self.image_label1.clear()
        self.image_label2.clear()

        self.nova_rodada()
        self.atualizar_pontuacao()


class MainInterface(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jogos")
        self.setGeometry(100, 100, 300, 200)

        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = OddEvenGame()
        self.tab2 = JogoDaSoma()

        self.tabs.addTab(self.tab1, "Jogo 1")
        self.tabs.addTab(self.tab2, "Jogo 2")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.tabs)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_interface = MainInterface()
    main_interface.show()
    sys.exit(app.exec())
