import pandas as pd #importando pandas com o apelido "pd"
import matplotlib.pyplot as plt #importando matplotlib para visualização de gráficos  

df = pd.read_csv(r"C:\Users\migue\OneDrive\Área de Trabalho\PotenciaTech\Datasets\gapminder.csv") #lendo o arquivo csv e armazenando na variável df

print("Nome das colunas originais: ", df.columns)#mostra o nome das colunas originais

df = df.rename(columns={"country": "País", "continent": "Continente", "year": "Ano", "lifeExp": "Expectativa de Vida", "pop": "Pop Total", "gdpPercap": "PIB"}) #Renomeando nome das colunas
print(df.head())#mostra as 5 primeiras linhas do dataframe

print(df.shape) #mostra a quantidade de linhas e colunas

print(df.columns) #mostra o nome das colunas

print(df.dtypes) #mostra o tipo de dado de cada coluna

print(df.tail()) #mostra as 5 últimas linhas do dataframe

print(df.describe()) #mostra um resumo estatístico do dataframe

print(df["Continente"].unique()) #mostra os valores únicos da coluna "Continente"

oceania = df.loc[df["Continente"] == "Oceania"] #cria um novo dataframe com os valores da Oceania
print(oceania.head())


print(df.groupby("Continente")["País"].nunique()) #mostra a quantidade de países por continente

print(df.groupby("Ano")["Expectativa de Vida"].mean().plot()) #mostra a média de expectativa de vida por ano

print(df["PIB"].mean()) #mostra a média do PIB

print(df.isnull().sum()) #mostra a quantidade de valores nulos em cada coluna

print(df.sample(5)) #mostra 5 linhas aleatórias do dataframe

df.groupby("Continente")["Expectativa de Vida"].mean().plot(kind="bar") #mostra a média da expectativa de vida por continente
plt.show()


df["Continente"].value_counts().plot.bar(title="Quantos Paises tem em cada Continente")
plt.xlabel("Continente")
plt.ylabel("Países")
plt.show()

plt.hist(df["Expectativa de Vida"])
plt.show()