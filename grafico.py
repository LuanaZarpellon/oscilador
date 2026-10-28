import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Função do OHA original (voltando a oscilar estritamente em torno de zero)
def oha(t, A, b, w, phi):
    return A * np.exp(-b * t) * np.cos(w * t - phi)

# Lê os dados da tabela (que já estão corrigidos e centralizados no zero)
dados = pd.read_csv('dados.csv')
t = dados['t'].values
x = dados['x'].values


#chutes iniciais dos parâmetros
chute_A = np.max(x)       
chute_b = 0.002           
chute_w = 5.0             
chute_phi = 0.0     

chute_inicial = [chute_A, chute_b, chute_w, chute_phi]

popt, pcov = curve_fit(oha, t, x, p0=chute_inicial)
A_otim, b_otim, w_otim, phi_otim = popt

#como é um valor muito pequeno de b, utiliza-se a equação Q = (m*wo)/gamma
#considerando b = j/2m, e considerando que pra amortecimentos pequenos w=~wo
qualidade = w_otim / (2 * b_otim)

print(f"Amplitude (A): {A_otim:.4f}")
print(f"Amortecimento (b): {b_otim:.4f}")
print(f"Frequência angular (w): {w_otim:.4f}")
print(f"Fase inicial (phi): {phi_otim:.4f}")
print(f"Fator de qualidade (Q): {qualidade: .4f}")



plt.figure(figsize=(12, 5))


#grafico dos dois juntos
plt.subplot(3, 1, 1)
plt.plot(t, x, color='red', linewidth=1.5, label='Dados Experimentais', alpha=0.7)
plt.plot(t, oha(t, *popt), color='blue', linewidth=2, label='Curva Ajustada (OHA)')
plt.title('Experimental x Curva ajustada')
plt.ylabel('Posição (x)')
plt.xlabel('Tempo (t)')
plt.grid(True)
plt.legend()

#graficos dos dados experimentais
plt.subplot(3, 1, 2)
plt.plot(t, x, color='red', linewidth=1.5, label='Dados Experimentais')
plt.title('Apenas Dados Experimentais')
plt.ylabel('Posição (x)')
plt.xlabel('Tempo (t)')
plt.grid(True)
plt.legend()

#grafico da curva ajustada
plt.subplot(3, 1, 3)
plt.plot(t, oha(t, *popt), color='blue', linewidth=2, label='Curva Ajustada (OHA)')
plt.title('Apenas Curva Ajustada Teórica')
plt.ylabel('Posição (x)')
plt.xlabel('Tempo (t)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
