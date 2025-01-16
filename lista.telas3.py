import tkinter as tk

class Aplicacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicação com Múltiplas Telas")
        self.root.geometry("400x300")

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.telas = {}

        for Tela in (Tela1, Tela2, Tela3):
            tela = Tela(self.container, self)
            self.telas[Tela] = tela
            tela.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela(Tela1)

    def mostrar_tela(self, nome_tela):
        frame = self.telas[nome_tela]
        frame.tkraise()


class Tela1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="lightblue")

        label = tk.Label(self, text="Bem-vindo à Tela 1", font=("Arial", 16), bg="lightblue")
        label.pack(pady=20)

        button = tk.Button(self, text="Ir para Tela 2", command=lambda: controller.mostrar_tela(Tela2))
        button.pack(pady=10)


class Tela2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="lightgreen")

        label = tk.Label(self, text="Você está na Tela 2", font=("Arial", 16), bg="lightgreen")
        label.pack(pady=20)

        button1 = tk.Button(self, text="Voltar para Tela 1", command=lambda: controller.mostrar_tela(Tela1))
        button1.pack(pady=10)

        button2 = tk.Button(self, text="Ir para Tela 3", command=lambda: controller.mostrar_tela(Tela3))
        button2.pack(pady=10)


class Tela3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg="lightcoral")

        label = tk.Label(self, text="Você está na Tela 3", font=("Arial", 16), bg="lightcoral")
        label.pack(pady=20)

        button = tk.Button(self, text="Voltar para Tela 2", command=lambda: controller.mostrar_tela(Tela2))
        button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacao(root)
    root.mainloop()
