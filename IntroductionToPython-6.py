# Projeto: Organizador de Arquivos de acordo com o diretório que escolher

# importando bibliotecas
import os
import shutil
from datetime import datetime
from tkinter import Tk, filedialog

# mapear as extensões dos arquivos
def create_default_extensions_map():
    return {
        "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg"],
        "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
        "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".csv"],
        "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg", ".rar", ".xar", ".zip"],
        "Others": []
    }

# encontrar o nome da pasta apropriada para a extensão do arquivo
def get_folder_for_extensions(extension, extensions_map):
    for folder, extensions in extensions_map.items():
        if extension in extensions:
            return folder
    return "Others"

# mover o arquivo para a pasta apropriada
def move_file(file_path, folder_name, directory):
    folder_path = os.path.join(directory, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    new_path = shutil.move(file_path, folder_path)

    print(f"Moved {os.path.basename(file_path)} to {folder_path}")
    return new_path

# organizar os arquivos do diretório por tipo de extensão
def organize_by_extension(directory):
    extensions_map = create_default_extensions_map()

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        if os.path.isfile(file_path):
            created_at = datetime.fromtimestamp(os.path.getctime())
            folder_name = created_at.strftime("%Y-%m-%d")
            move_file(file_path, folder_name, directory)

def main():
    root = Tk()
    root.withdraw()
    directory = filedialog.askdirectory(title="Selecionar diretório")
    if not directory:
        print("O diretório selecionado não existe")
        return
    
    while True:
        print("\nORGANIZADOR DE ARQUIVOS - Escolha uma opção:")
        print("1. Organizar por Tipo de Arquivo")
        print("2. Organizar por Data de Criação")
        print("3. Sair")

        choice = input("Digite sua escolha (1-3): ")

        if choice == "1":
            organize_by_extension(directory)
        elif choice == "2":
            organize_by_date(directory)
        elif choice == "3":
            break
        else:
            print("Escolha inválida. Tente novamente.")

# quando executar o script, irá carregar as demais funções e iniciar pela main
if __name__ == "__main__":
    main()