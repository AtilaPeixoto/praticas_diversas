import random
import tkinter as tk


class start:
    perguntas = [['Qual é a capital do Brasil?', 'Brasília', ['Rio de Janeiro', 'São Paulo', 'Brasília']],
                ['Qual é o maior animal terrestre?', 'Elefante', ['Girafa', 'Elefante', 'Hipopótamo']]
    ]

    def __init__(self, master):
        self.master = master
        master.title("Quiz")

        self.pergunta_label = tk.Label(master, text="")
        self.pergunta_label.pack()

        self.respostas_buttons = []
        for i in range(4):
            button = tk.Button(master, text="", command=lambda index=i: self.respondendo(index))
            button.pack()
            self.respostas_buttons.append(button)

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

        self.preparando()

    def preparando(self, *args):
        pergunta_escolhida = random.choice(self.perguntas)
        self.pergunta = pergunta_escolhida[0]
        self.certa = pergunta_escolhida[1]
        self.opcoes = pergunta_escolhida[2]
        self.opcoes.append(self.certa)
        random.shuffle(self.opcoes)
        self.indice = self.opcoes.index(self.certa)

        self.pergunta_label.config(text=self.pergunta)
        for i in range(3):
            self.respostas_buttons[i].config(text=self.opcoes[i])

    def respondendo(self, index):
        self.res = index + 1
        if self.res == self.indice:
            self.status_label.config(text="Acertou!")
        else:
            self.status_label.config(text="Errou! A resposta correta era: " + self.certa)

        self.preparando()


root = tk.Tk()
jogo = start(root)
root.mainloop()
