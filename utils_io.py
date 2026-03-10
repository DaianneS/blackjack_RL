import pandas as pd
import matplotlib.pyplot as plt
from config_projeto import DADOS_DIR, GRAFICOS_DIR, RESULTADOS_DIR, MODELOS_DIR

def salvar_df(df, nome, pasta="dados"):
    if pasta == "dados":
        caminho = DADOS_DIR / f"{nome}.csv"
    elif pasta == "resultados":
        caminho = RESULTADOS_DIR / f"{nome}.csv"
    elif pasta == "modelos":
        caminho = MODELOS_DIR / f"{nome}.csv"
    else:
        raise ValueError("Pasta inválida. Use: dados, resultados ou modelos.")

    df.to_csv(caminho, index=False, encoding="utf-8-sig")
    print(f"Arquivo salvo em: {caminho}")

def carregar_df(nome, pasta="dados"):
    if pasta == "dados":
        caminho = DADOS_DIR / f"{nome}.csv"
    elif pasta == "resultados":
        caminho = RESULTADOS_DIR / f"{nome}.csv"
    elif pasta == "modelos":
        caminho = MODELOS_DIR / f"{nome}.csv"
    else:
        raise ValueError("Pasta inválida. Use: dados, resultados ou modelos.")

    print(f"Lendo arquivo: {caminho}")
    return pd.read_csv(caminho)

def salvar_grafico(nome_arquivo, dpi=300):
    caminho = GRAFICOS_DIR / nome_arquivo
    plt.tight_layout()
    plt.savefig(caminho, dpi=dpi, bbox_inches="tight")
    print(f"Gráfico salvo em: {caminho}")