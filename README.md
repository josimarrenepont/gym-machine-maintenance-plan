# Plano de Trabalho com Cronograma de Atividades
Objetivo Geral: Analisar dados de manutenção de máquinas para prevenir quebras e otimizar a manutenção preventiva.
## Ações:
1.	**Coleta de Dados:**
    - Registrar manutenções preventivas e corretivas realizadas.
    - Toda vez que uma manutenção for realizada.
    - Através de um formulário onde o técnico preenche as informações de manutenção.
    - Proprietários da academia.
    - Academia Studio 55.
2.	**Análise de Dados:**
    - Analisar padrões nos dados de manutenção para prever quebras e otimizar a manutenção preventiva.
    - Após um período de coleta de dados (mensal).
    - Utilizando métodos de análise de dados com Python e gerando relatórios.
    - Gestores e responsáveis pela academia.
    - Escritório da academia.
3.	**Geração de Relatórios:**
    - Criar relatórios preventivos e sugestões de manutenção.
    - Mensalmente ou conforme necessidade.
    - A partir da análise dos dados gerados.
    - Gestores da academia.
    - Escritório da academia.
# Explicação da Estrutura:
  - simular_dados.py: Cuida da geração de dados aleatórios de manutenção.
  - analisar_dados.py: Fornece as funções de análise básica sobre os dados gerados.
  - plotar_dados.py: Funções para criar visualizações gráficas.
  - gerar_relatorio.py: Responsável pela geração de relatórios de manutenção preventiva.
  - main.py: O ponto de entrada que junta todas as partes e executa o projeto.
________________________________________
Metodologia
1.	Coleta de Dados: A coleta será feita manualmente pelo técnico de manutenção, que vai inserir dados em um sistema (neste caso, simulados no código).
2.	Análise: Usaremos Python para identificar padrões de uso das máquinas, possíveis falhas recorrentes e gerar recomendações preventivas.
3.	Geração de Relatórios: Ao final de cada mês, o sistema vai gerar um relatório com recomendações sobre quais máquinas precisam de manutenção preventiva.
________________________________________
## Como Executar
1. **Executar o src**
   -- Navegue para o diretório `src` e execute:
     ```bash
     python main.py
     ```
________________________________________
## Dependências
Certifique-se de ter as seguintes dependências instaladas:
- `pandas`
- `matplotlib`
