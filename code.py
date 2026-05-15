import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title='Selecione uma Pasta')

lista_arquivos = os.listdir(caminho)

locais = {
    "Imagens": [".png", ".jpg", ".jpeg"],
    "Planilhas": [".xlsx"],
    "PDFs e Documentos": [".pdf", ".docx", ".mht", ".webp"],
    "Apps": [".exe"],
    "Pastas Compactadas": [".zip", ".7z"],
    "Musicas, Sons e Vídeos": [".mp4", ".gif", ".mp3"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    if extensao not in locais.values():
        nova_extensao = str(extensao[1:].upper())
        locais[nova_extensao] = list(extensao)
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")

    