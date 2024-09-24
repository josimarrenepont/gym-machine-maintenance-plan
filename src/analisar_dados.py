def analisar_dados_manutencao(df):
    print("Análise das Manutenções de Máquinas")
    print("Quantidade de Manutenções por Tipo de Máquina:")
    print(df['Maquina'].value_counts())
    
    print("\nProblemas mais Comuns Identificados:")
    print(df['Problema Identificado'].value_counts())

    print("\nMédia de Horas de Uso Antes de Manutenção por Tipo de Máquina:")
    print(df.groupby('Maquina')['Horas de Uso'].mean())
