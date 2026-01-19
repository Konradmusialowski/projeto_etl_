import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA = BASE_DIR / "data" / "raw"


def extract_centros():
    """
    Extrai os dados de centros de distribuição
    """
    file_path = RAW_DATA / "centros_distrib.xlsx"
    df_centros = pd.read_excel(file_path, engine="openpyxl")

    print("Centros de distribuição carregados com sucesso")
    return df_centros


def extract_estq():
    """
    Extrai a movimentação de estoque
    """
    file_path = RAW_DATA / "mov_estq.xlsx"
    df_mov = pd.read_excel(file_path, engine="openpyxl")

    print("Movimentação de estoque carregada com sucesso")
    return df_mov


if __name__ == "__main__":
    df1 = extract_centros()
    df2 = extract_estq()

    print(df1.head())
    print(df2.head())
