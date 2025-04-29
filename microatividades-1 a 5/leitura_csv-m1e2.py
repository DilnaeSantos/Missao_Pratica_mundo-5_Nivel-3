import pandas as pd

# microatividade 1
# Lê o arquivo CSV com separador ';', utilizando a engine 'python'
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# Exibe o conteúdo do DataFrame
print(dados)


# microatividade 2
# Criação do subconjunto com 3 colunas específicas
subconjunto = dados[["Date", "Pulse", "Calories"]]

# Exibe o subconjunto
print("\n🔍 Subconjunto (Date, Pulse, Calories):")
print(subconjunto)
