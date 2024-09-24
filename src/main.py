from analisar_dados import analisar_dados_manutencao
from gerar_relatorio import gerar_relatorio_preventivo
from plotar_dados import plot_manutencoes
from simular_dados import gerar_dados_manutencao

# Geração dos dados simulados
df_manutencao = gerar_dados_manutencao(20)

# Análise dos dados
analisar_dados_manutencao(df_manutencao)

# Gerar e mostrar gráficos
plot_manutencoes(df_manutencao)

# Geração de relatório preventivo
relatorio_preventivo = gerar_relatorio_preventivo(df_manutencao)
for item in relatorio_preventivo:
    print(item)
