import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import re 
from statsmodels.tsa.seasonal import seasonal_decompose
import matplotlib.pyplot as plt


df = pd.read_csv(r"C:\Users\migue\OneDrive\Área de Trabalho\PotenciaTech\estudo_ciencia_dados\analise_covid\covid_19_data.csv", parse_dates=['ObservationDate', 'Last Update'])

def corrige_colunas(col_name):
    return re.sub(r"[/| ]", "", col_name).lower()

print(df)

df.columns = [corrige_colunas(col) for col in df.columns]

df.loc[df['countryregion'] == 'Brazil']

brasil = df.loc[(df.countryregion == 'Brazil') & (df.confirmed > 0)] 


print("Grafico de casos confirmados no Brasil")

fig = px.line(brasil, 'observationdate', 'confirmed', title="Casos confirmados no Brasil")
fig.show()

brasil['novoscasos'] = list(map(
    lambda x: 0 if x == 0 else brasil['confirmed'].iloc[x] - brasil['confirmed'].iloc[x - 1],
    np.arange(brasil.shape[0])
))

print(brasil)

fig = px.line(brasil, x='observationdate', y='novoscasos', title='Novos casos no Brasil')

fig.show()
#################################################
fig = go.Figure()

fig.add_trace(go.Scatter(x=brasil.observationdate, y=brasil.deaths, name="Mortes",mode="lines+markers",line={"color":"red"}))

fig.update_layout(title="Mortes por COVID no Brasil")

fig.show()

###################################################
# TAXA MÉDIA DE CRESCIMENTO

def taxa_crescimento(data, variable, data_inicio=None, data_fim=None):
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable]>0].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)

    if data_fim == None:
        data_fim = data.observationdate.iloc[-1]
    else:
        data_fim = pd.to_datetime(data_fim)

    passado = data.loc[data.observationdate == data_inicio, variable].values[0]
    presente = data.loc[data.observationdate == data_fim, variable].values[0]

    n = (data_fim - data_inicio).days

    taxa = (presente/passado)**(1/n) - 1

    return taxa * 100

print(taxa_crescimento(brasil, 'confirmed'))

def taxa_crescimento_diario(data, variable, data_inicio=None):
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable]>0].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)

    data_fim = data.observationdate.max()
    n = (data_fim - data_inicio).days

    taxas = list(map(
        lambda x: (data[variable].iloc[x] - data[variable].iloc[x-1]) / data[variable].iloc[x-1],
        range(1, n+1)
    ))
    return np.array(taxas) * 100

tx_dia = taxa_crescimento_diario(brasil, 'confirmed')

print(tx_dia)

primeiro_dia = brasil.observationdate.loc[brasil.confirmed > 0].min()

fig = px.line(x=pd.date_range(primeiro_dia, brasil.observationdate.max())[1:],
              y=tx_dia, title="Taxa de crescimento de casos por dia")
fig.show()

####################################################################
#PREDIÇÕES

confirmados = brasil.confirmed
confirmados.index = brasil.observationdate
print(confirmados)

confirmados = confirmados[~confirmados.index.duplicated(keep='first')]

confirmados = confirmados.asfreq('D')
resultado = seasonal_decompose(confirmados)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 8))

ax1.plot(resultado.observed)
ax2.plot(resultado.trend)
ax3.plot(resultado.seasonal)
ax4.plot(confirmados.index, resultado.resid)
ax4.axhline(0, linestyle="dashed", color="red")
plt.show()


####################################################################