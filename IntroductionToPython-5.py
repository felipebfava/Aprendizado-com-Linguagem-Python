#----------------------##----------------------------#
# Projeto: Unindo arquivos excel (.xlsx) em um único arquivo

# importando bibliotecas
import os
import pandas as pd

# mudar de acordo onde está o arquivo
data_arquivo_folder = 'data'

df = []

for file in os.listdir(data_arquivo_folder):
    if file.endswith('.xlsx'):
        print('Loading file {0}...', format(file))
        df.append(pd.read_excel(os.path.join(data_arquivo_folder, file)))

print(len(df))

df_principal = pd.concat(df, axis=0)
df_principal.to_excel('data/master_store.xlsx', index=False)

#----------------------##----------------------------#

#----------------------##----------------------------#
# Projeto: Unindo arquivos excel (.csv) em um único arquivo / arquivo em .xlsx para .csv
# usará o pandas -> import pandas as pd

listas=['nome_arquivo1.csv', 'nome_arquivo2.csv', 'nome_arquivo3.csv']
w = pd.ExcelWriter('nome_arquivo.xlsx')
for lista in listas:
    df = pd.read_csv(lista)
    nome = lista.replace('.csv', '')
    df.to_excel(w, sheet_name=nome, index=False)
w.save()

#----------------------##----------------------------#