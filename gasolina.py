# código de geração do gráfico 

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gasolina.csv") 

with sns.axes_style ('whitegrid') :
  grafico = sns.lineplot(data = df, x = "dia", y = "venda", color = "green", marker = "o")
  grafico.set(title='Gráfico de vendas de gasolina', xlabel='Dia', ylabel='Preço')
  plt.savefig('gasolina.png')