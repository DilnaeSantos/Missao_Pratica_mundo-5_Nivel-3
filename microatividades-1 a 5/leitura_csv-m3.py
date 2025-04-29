import pandas as pd

# Leitura do CSV original
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# Subconjunto (usado anteriormente, pode ser mantido)
subconjunto = dados[["Date", "Pulse", "Calories"]]

# Configurando o número máximo de linhas exibidas
pd.set_option("display.max_rows", 9999)

# Exibindo o DataFrame completo como string
print("📋 Exibição completa dos dados:")
print(dados.to_string())
