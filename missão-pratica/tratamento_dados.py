import pandas as pd
import numpy as np

# 1. Leitura do arquivo CSV
dados = pd.read_csv('dados.csv', sep=';', engine='python', encoding='utf-8')

# 2. Verificar se os dados foram importados corretamente
print("\n📌 Informações gerais:")
dados.info()

print("\n📌 Primeiras linhas:")
print(dados.head())

print("\n📌 Últimas linhas:")
print(dados.tail())

# 3. Criar uma cópia dos dados
dados_tratados = dados.copy()

# 4. Substituir valores nulos da coluna 'Calories' por 0
dados_tratados['Calories'].fillna(0, inplace=True)
print("\n✅ Após preencher 'Calories' com 0:")
print(dados_tratados)

# 5. Substituir valores nulos da coluna 'Date' por '1900/01/01'
dados_tratados['Date'].fillna('1900/01/01', inplace=True)
print("\n✅ Após preencher 'Date' com '1900/01/01':")
print(dados_tratados)

# 6. Tentar transformar a coluna 'Date' em datetime (irá gerar erro)
try:
    dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], format='%Y/%m/%d')
except Exception as e:
    print("\n⚠️ Erro ao converter 'Date' para datetime:", e)

# 7. Corrigir '1900/01/01' para np.nan
dados_tratados['Date'].replace('1900/01/01', np.nan, inplace=True)

# 8. Corrigir o valor '20201226' para datetime
dados_tratados['Date'] = dados_tratados['Date'].replace('20201226', '2020/12/26')

# 9. Tentar novamente a conversão para datetime
dados_tratados['Date'] = pd.to_datetime(dados_tratados['Date'], errors='coerce', format='%Y/%m/%d')
print("\n✅ Após conversão final de 'Date':")
print(dados_tratados)

# 10. Remover registros com valores nulos
dados_tratados.dropna(inplace=True)

# 11. Exibir DataFrame final
print("\n🧹 DataFrame final limpo:")
print(dados_tratados)
