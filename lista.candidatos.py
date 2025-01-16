# Importação de bibliotecas necessárias
import tkinter as tk  # Biblioteca para criar interfaces gráficas
from tkinter import messagebox, filedialog  # Exibição de mensagens e abertura de arquivos
from threading import Thread  # Para rodar tarefas em paralelo (evitar travamentos)
import os  # Para interagir com o sistema de arquivos
# import cv2  # Biblioteca para manipulação de vídeos
# from PIL import Image, ImageTk  # Para exibir imagens e vídeos no tkinter

# Lista global para armazenar candidatos
candidatos = []

# Função para ajustar o tamanho da janela
def alterar_tamanho(modo):
    if modo == "full":
        janela.attributes("-fullscreen", True)  # Ativa modo tela cheia
    elif modo == "meia_direita":
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()
        janela.geometry(f"{largura_tela//2}x{altura_tela}+{largura_tela//2}+0")  # Metade direita
    elif modo == "800x600":
        janela.geometry("800x600")  # Tamanho fixo
    elif modo == "tela_cheia_com_barra":
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight() - 40
        janela.geometry(f"{largura_tela}x{altura_tela}+0+0")  # Tela cheia com barra visível

# Função para carregar vídeos na memória
def carregar_videos():
    video_paths = ["video1.mp4", "video2.mp4"]  # Caminhos dos vídeos
    for video_path in video_paths:
        if os.path.exists(video_path):
            videos.append(cv2.VideoCapture(video_path))

# Função para reproduzir um vídeo
def reproduzir_video(video_index):
    if video_index < len(videos):
        cap = videos[video_index]

        def video_loop():
            while cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Converte frame para RGB
                    frame = ImageTk.PhotoImage(Image.fromarray(frame))
                    video_label.config(image=frame)
                    video_label.image = frame
                else:
                    break

        Thread(target=video_loop, daemon=True).start()

# Função para gerar número único para cada candidato
def gerar_numero_candidato():
    return len(candidatos) + 1

# Função para salvar os dados do formulário
def salvar_dados():
    try:
        nome = entry_nome.get()
        sexo = sexo_var.get()
        idade = int(entry_idade.get())
        faculdade = entry_faculdade.get()
        anos_experiencia = int(entry_anos_experiencia.get())
        valor_gasto = entry_valor_gasto.get()
        distancia = float(entry_distancia.get())
        unidade_distancia = unidade_distancia_var.get()
        ultimo_salario = entry_ultimo_salario.get()

        # Converte distância para metros
        if unidade_distancia == "km":
            distancia_em_metros = distancia * 1000
            distancia_display = f"{distancia} km"
        else:
            distancia_em_metros = distancia
            distancia_display = f"{distancia} metros"

        # Gera número do candidato
        numero_candidato = gerar_numero_candidato()

        # Armazena dados do candidato
        candidato = {
            "Número": numero_candidato,
            "Nome": nome,
            "Sexo": sexo,
            "Idade": idade,
            "Faculdade": faculdade,
            "Anos de experiência": anos_experiencia,
            "Valor gasto": valor_gasto,
            "Distância": distancia_em_metros,
            "Distância Display": distancia_display,
            "Último salário": ultimo_salario
        }
        candidatos.append(candidato)

        # Avaliação do candidato
        if idade < 18:
            resultado = "Status: Recusado (Menor de idade)."
        elif anos_experiencia <= 3:
            resultado = "Status: Encaminhado para curso de capacitação."
        else:
            resultado = "Status: Aprovado para a próxima fase."

        # Exibe resultados
        label_resultado.config(text=f"Resultado da Avaliação: {resultado}")
        label_detalhes.config(text=f"Detalhes do Candidato #{numero_candidato}:\n"
                                   f"Nome: {nome}\nSexo: {sexo}\nIdade: {idade}\n"
                                   f"Faculdade: {faculdade}\nAnos de experiência: {anos_experiencia}\n"
                                   f"Valor gasto para o trabalho: {valor_gasto}\nDistância: {distancia_display}\n"
                                   f"Último salário: {ultimo_salario}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar dados: {e}")

# Função para salvar backup dos dados
def salvar_backup():
    try:
        with open("backup.txt", "a") as f:
            for candidato in candidatos:
                f.write(str(candidato) + "\n")
        messagebox.showinfo("Sucesso", "Dados salvos no backup com sucesso.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar backup: {str(e)}")

# Configuração inicial da janela principal
janela = tk.Tk()
janela.title("Sistema de Análise de Candidatos")
janela.geometry("800x600")

# Campos do formulário
label_nome = tk.Label(janela, text="Nome:")
entry_nome = tk.Entry(janela)
label_nome.pack()
entry_nome.pack()

label_sexo = tk.Label(janela, text="Sexo (M/F):")
sexo_var = tk.StringVar(value="M")
opcoes_sexo = tk.OptionMenu(janela, sexo_var, "M", "F")
label_sexo.pack()
opcoes_sexo.pack()

label_idade = tk.Label(janela, text="Idade:")
entry_idade = tk.Entry(janela)
label_idade.pack()
entry_idade.pack()

label_faculdade = tk.Label(janela, text="Faculdade:")
entry_faculdade = tk.Entry(janela)
label_faculdade.pack()
entry_faculdade.pack()

label_anos_experiencia = tk.Label(janela, text="Anos de Experiência:")
entry_anos_experiencia = tk.Entry(janela)
label_anos_experiencia.pack()
entry_anos_experiencia.pack()

label_valor_gasto = tk.Label(janela, text="Valor gasto para o trabalho:")
entry_valor_gasto = tk.Entry(janela)
label_valor_gasto.pack()
entry_valor_gasto.pack()

label_distancia = tk.Label(janela, text="Distância até o trabalho:")
entry_distancia = tk.Entry(janela)
label_distancia.pack()
entry_distancia.pack()

unidade_distancia_var = tk.StringVar(value="metros")
opcoes_unidade = tk.OptionMenu(janela, unidade_distancia_var, "km", "metros")
opcoes_unidade.pack()

label_ultimo_salario = tk.Label(janela, text="Último Salário:")
entry_ultimo_salario = tk.Entry(janela)
label_ultimo_salario.pack()
entry_ultimo_salario.pack()

# Botões de ação
botao_salvar = tk.Button(janela, text="Salvar Candidato", command=salvar_dados)
botao_salvar.pack()

botao_backup = tk.Button(janela, text="Salvar Backup", command=salvar_backup)
botao_backup.pack()

# Áreas de exibição
label_resultado = tk.Label(janela, text="", font=("Arial", 12))
label_resultado.pack()

label_detalhes = tk.Label(janela, text="", font=("Arial", 12))
label_detalhes.pack()

# Inicia o loop principal da janela
janela.mainloop()
