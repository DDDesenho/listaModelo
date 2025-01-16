import tkinter as tk


class Aplicacao:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Aplicação com Múltiplas Telas")
        self.janela.geometry("400x160")

        # Frames para cada tela
        self.frame1 = tk.Frame(self.janela, bg="lightblue")
        self.frame2 = tk.Frame(self.janela, bg="lightgreen")
        self.frame3 = tk.Frame(self.janela, bg="lightyellow")

        # Exibe a Tela 1 ao iniciar
        self.mostrar_tela1()

    def mostrar_tela1(self):
        self.ocultar_todos_frames()
        self.frame1.pack(fill="both", expand=True)

        label1 = tk.Label(self.frame1, text="Bem-vindo à Tela 1", font=("Arial", 14))
        label1.pack(pady=20)

        button1 = tk.Button(
            self.frame1, text="Ir para Tela 2",
            command=self.mostrar_tela2,
            bg="#007acc", fg="white", width=15
        )
        button1.pack(pady=30)

    def mostrar_tela2(self):
        self.ocultar_todos_frames()
        self.frame2.pack(fill="both", expand=True)

        label2 = tk.Label(self.frame2, text="Você está na Tela 2", font=("Arial", 14))
        label2.pack(pady=20)

        button2 = tk.Button(
            self.frame2, text="Voltar para Tela 1",
            command=self.mostrar_tela1,
            bg="#28a745", fg="white", width=15
        )
        button2.pack(pady=10)

        button3 = tk.Button(
            self.frame2, text="Ir para Tela 3",
            command=self.mostrar_tela3,
            bg="#007acc", fg="white", width=15
        )
        button3.pack(pady=10)

    def mostrar_tela3(self):
        self.ocultar_todos_frames()
        self.frame3.pack(fill="both", expand=True)

        label3 = tk.Label(self.frame3, text="Você está na Tela 3", font=("Arial", 14))
        label3.pack(pady=20)

        button4 = tk.Button(
            self.frame3, text="Voltar para Tela 2",
            command=self.mostrar_tela2,
            bg="#28a745", fg="white", width=15
        )
        button4.pack(pady=10)

    def ocultar_todos_frames(self):
        """Esconde todos os telas antes de exibir o desejado."""
        for frame in [self.frame1, self.frame2, self.frame3]:
            frame.pack_forget()


# Criação e execução do aplicativo
janela = tk.Tk()
app = Aplicacao(janela)
janela.mainloop()
