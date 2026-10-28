import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dados = pd.read_csv('dados.csv')
t = dados['t'].values
x = dados['x'].values
y = dados['y'].values


plt.figure(figsize=(10, 6))

# Gráfico do Movimento Horizontal 
plt.subplot(2, 1, 1)
plt.plot(t, x, color='blue', linewidth=2, label='Gráfico OHA')
plt.title('Gráfico de oscilação posição horizontal x tempo')
plt.ylabel('x')
plt.xlabel('tempo')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()