import matplotlib.pyplot as plt


def plot_manutencoes(df):
    df['Maquina'].value_counts().plot(kind='bar', title='Manutenções por Tipo de Máquina')
    plt.xlabel('Tipo de Máquina')
    plt.ylabel('Número de Manutenções')
    plt.show()
