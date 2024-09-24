import random
from datetime import datetime, timedelta

import pandas as pd

tipos_maquinas = ['Esteira', 'Bicicleta', 'Supino', 'Puxada', 'Leg Press']
problemas_comuns = ['Correia gasta', 'Motor aquecendo', 'Cabos soltos', 'Ruído anormal', 'Rolamentos desgastados']

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
            'Data da Manutenção': data_manutencao
        })
    
    return pd.DataFrame(dados_manutencao)
