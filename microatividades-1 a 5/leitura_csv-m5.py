import pandas as pd

# Leitura do CSV original
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# Exibir informações gerais do DataFrame
print("ℹ️ Informações gerais sobre o DataFrame:")
dados.info()
