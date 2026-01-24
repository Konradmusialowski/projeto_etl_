import papermill as pm
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

def executar_notebook():
    input_nb = BASE_DIR / "notebooks" / "graficos.ipynb"
    output_nb = BASE_DIR / "notebooks" / "graficos_executado.ipynb"

    print("📊 Executando notebook de gráficos...")

    pm.execute_notebook(
        input_path=str(input_nb),
        output_path=str(output_nb),
        kernel_name="python3"
    )

    print("✅ Notebook executado com sucesso")