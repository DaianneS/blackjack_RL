# ♠️ Blackjack RL: Q-Learning Agent with Hi-Lo Card Counting 🃏

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-150458.svg)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Data_Visualization-4C72B0.svg)](https://seaborn.pydata.org/)
[![Reinforcement Learning](https://img.shields.io/badge/AI-Reinforcement_Learning-FF6F00.svg)]()

##  Sobre o Projeto

Este projeto de Ciência de Dados aplica algoritmos de **Reinforcement Learning (Aprendizado por Reforço)** para resolver o jogo de Blackjack. O diferencial desta abordagem é o afastamento da premissa teórica de um "baralho infinito". 

O ambiente foi modelado para simular as condições reais de um cassino: um *Shoe* finito de 6 baralhos onde as cartas são compradas sem reposição imediata. Isso permitiu integrar o sistema **Hi-Lo de Contagem de Cartas**, capacitando o agente de Inteligência Artificial (treinado via **Q-Learning**) a adaptar sua estratégia de acordo com a "temperatura" da mesa (True Count).

##  Objetivos e Resultados

- **Implementar do zero** o ambiente lógico do Blackjack (regras, dealer, compra contínua de cartas).
- **Estabelecer baselines** rodando milhões de simulações com políticas estáticas (Aleatória e Política Básica de Casino).
- **Treinar um Agente de Q-Learning** lidando com a Maldição da Dimensionalidade através de *State Binning* para o True Count.
- **Provar a eficácia da Contagem de Cartas**: O agente demonstrou matematicamente a capacidade de reverter dogmas da Política Básica. Por exemplo: na clássica "pior mão" (Jogador 16 vs Dealer 10), o agente aprendeu autonomamente a trocar a ação de *Hit* (pedir carta) para *Stick* (parar) quando o baralho se torna favorável/quente (`True Count >= 2`).

##  Estrutura do Repositório

O projeto adota fortes práticas de Engenharia de Software, separando a lógica de negócio dos notebooks de experimentação:

```text
├── graficos/                # Visualizações analíticas geradas
├── modelos/                 # Q-Tables consolidadas (.csv)
├── resultados/              # Métricas agregadas e taxas de conversão
├── notebooks/               # Cadernos de experimentação e documentação
│   ├── ambiente_blackjack.ipynb
│   ├── politica_basica.ipynb
│   ├── qlearning_blackjack.ipynb
│   └── avaliacao_blackjack.ipynb
├── analise_exploratoria_blackjack.ipynb # Análise dos resultados e criação dos gráficos
├── blackjack_env.py         # Core: Física do jogo e classe ShoeBlackjack
├── config_projeto.py        # Configuração global e mapeamento de diretórios
├── utils_io.py              # Funções utilitárias para I/O padronizado
└── README.md                # Documentação do projeto

```

##  Como Executar

1. **Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/blackjack-rl.git](https://github.com/seu-usuario/blackjack-rl.git)
cd blackjack-rl

```


2. **Instale as dependências (Pandas, Matplotlib, Seaborn):**
```bash
pip install pandas matplotlib seaborn jinja2

```


3. **Execute os Notebooks:**
Recomenda-se rodar os notebooks da pasta `notebooks/` na ordem estabelecida:
* `ambiente_blackjack.ipynb`: Valida a física e mecânica contínua do baralho.
* `politica_basica.ipynb`: Gera o baseline de dados da banca.
* `qlearning_blackjack.ipynb`: Realiza o treinamento do agente.
* `avaliacao_blackjack.ipynb`: Consolida os resultados frente a frente.
* `analise_exploratoria_blackjack.ipynb`: Traz os insights visuais e financeiros.

---

## Conclusões e Resultados

A modelagem deste ecossistema de Blackjack demonstrou que o uso de **Aprendizado por Reforço (Q-Learning)**, quando integrado a variáveis dinâmicas de ambiente como o **True Count (Hi-Lo)**, é capaz de superar as limitações de estratégias estáticas.

Através de 1.000.000 de episódios de treinamento, o agente não apenas decorou as regras do jogo, mas desenvolveu uma compreensão estatística da "temperatura" do baralho. O sucesso do projeto é evidenciado pela capacidade do agente em identificar momentos de alta probabilidade de vitória, ajustando decisões críticas que a Política Básica ignora por ser determinística.

### Principais Insights Analíticos:

* **Eficácia do State Binning**: O agrupamento do True Count (entre -2 e +2) foi essencial para mitigar a Maldição da Dimensionalidade, permitindo uma convergência estável da Q-Table.
* **Adaptação Estratégica**: O agente aprendeu autonomamente a ser mais conservador em mesas "quentes" (parando com somas menores), reconhecendo que o risco de o Dealer estourar é superior ao risco de o jogador não pedir carta.

---

Com esta conclusão e a exposição destes gráficos, o seu projeto de **Blackjack RL** demonstra um ciclo completo de Ciência de Dados: desde a modelagem do ambiente até a extração de valor e inteligência de negócio.

**Gostaria que eu ajudasse a detalhar algum desses pontos ou a formatar a seção de tecnologias utilizadas?**

##  Arquitetura e Próximos Passos (Escalabilidade)

O escopo atual foca na prova de conceito e na matemática do modelo em Python local. O próximo passo de arquitetura deste projeto envolve a migração destes *pipelines* de simulação para um ambiente de Big Data escalável.

A visão de futuro inclui orquestrar a geração massiva de episódios utilizando o ecossistema de nuvem para compor uma arquitetura **Medallion**:

* **Ingestão Distribuída**: Utilização de processamento paralelo com **PySpark** para simular bilhões de mãos simultaneamente.
* **Armazenamento e Limpeza**: Organização dos logs JSON gerados (Camada Bronze) e tratamento de anomalias estatísticas no histórico (Camada Silver) utilizando **Microsoft Fabric** ou **Azure Databricks**.
* **Modelagem Semântica**: Disponibilização das Q-Tables otimizadas e métricas de desempenho na Camada Gold, prontas para consumo e criação de relatórios interativos e simulações de Bankroll em **Power BI**.

---

*Desenvolvido por [Daianne](https://www.google.com/search?q=https://github.com/DaianneS).*

```

