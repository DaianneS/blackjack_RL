from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DADOS_DIR = BASE_DIR / "dados"
GRAFICOS_DIR = BASE_DIR / "graficos"
RESULTADOS_DIR = BASE_DIR / "resultados"
MODELOS_DIR = BASE_DIR / "modelos"
EXPORTS_DIR = BASE_DIR / "exports"

for pasta in [DADOS_DIR, GRAFICOS_DIR, RESULTADOS_DIR, MODELOS_DIR, EXPORTS_DIR]:
    pasta.mkdir(parents=True, exist_ok=True)