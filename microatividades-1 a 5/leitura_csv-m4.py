import pandas as pd

# Leitura do CSV original
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# Configuração para exibir até 9999 linhas (mantida da atividade anterior)
pd.set_option("display.max_rows", 9999)

# Exibir as primeiras 10 linhas
print("🔼 Primeiras 10 linhas:")
print(dados.head(10))

# Exibir as últimas 10 linhas
print("\n🔽 Últimas 10 linhas:")
print(dados.tail(10))
