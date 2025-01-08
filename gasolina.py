# código de geração do gráfico 

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

sns.lineplot(data=df, x='dia', y='venda')
plt.savefig('gasolina.png')