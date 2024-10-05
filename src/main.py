import random
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import pandas as pd

# Tipos de máquinas e problemas comuns
tipos_maquinas = ['Esteira', 'Bicicleta', 'Supino', 'Puxada', 'Leg Press']
problemas_comuns = ['Correia gasta', 'Motor aquecendo', 'Cabos soltos', 'Ruído anormal', 'Rolamentos desgastados']

# Função para gerar dados fictícios de manutenção
def gerar_dados_manutencao(n_maquinas=10):
    dados_manutencao = []
    for i in range(n_maquinas):
        maquina = random.choice(tipos_maquinas)
        horas_uso = random.randint(50, 500)
        problema = random.choice(problemas_comuns)
        acao_corretiva = f"Substituição/Reparo de {problema.split()[1]}"
        data_manutencao = datetime.now() - timedelta(days=random.randint(1, 180))

        dados_manutencao.append({
            'Maquina': maquina,
            'Horas de Uso': horas_uso,
            'Problema Identificado': problema,
            'Ação Corretiva': acao_corretiva,
            'Data da Manutenção': data_manutencao.strftime('%Y-%m-%d')
        })

    return pd.DataFrame(dados_manutencao)

# Função para plotar gráfico de barras e adicionar valores no topo das barras
def plot_manutencoes(df_manutencao):
    # Agrupa os dados por máquina e soma as horas de uso
    horas_por_maquina = df_manutencao.groupby('Maquina')['Horas de Uso'].sum()

    # Cria o gráfico de barras
    plt.figure(figsize=(10, 6))
    barras = plt.bar(horas_por_maquina.index, horas_por_maquina.values, color='skyblue')

    # Adiciona rótulos com os valores no topo das barras
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 f'{int(altura)}', ha='center', va='bottom', fontsize=12)

    # Configurações do gráfico
    plt.title('Horas de Uso por Máquina', fontsize=16, fontweight='bold')
    plt.xlabel('Máquina', fontsize=14)
    plt.ylabel('Horas de Uso', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', alpha=0.75)

    # Exibe o gráfico
    plt.tight_layout()
    plt.show()

# Gerar dados fictícios de manutenção
df_manutencao = gerar_dados_manutencao(20)

# Plotar o gráfico com valores
plot_manutencoes(df_manutencao)
