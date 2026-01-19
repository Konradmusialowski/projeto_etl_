from src.etl.extract import extract_centros, extract_estq
from src.etl.transform import transform_centros, transform_movimentacao
from src.etl.load import load_dim_centro, load_fact_movimentacao
from src.database import connect_db


def run_pipeline():
    print("🚀 Iniciando pipeline ETL Logística...")

    # 🔹 EXTRACT
    df_centros = extract_centros()
    df_mov = extract_estq()

    # 🔹 TRANSFORM
    df_centros_tratado = transform_centros(df_centros)
    df_mov_tratado = transform_movimentacao(df_mov)
    

    # 🔹 LOAD
    conn = connect_db()
    load_dim_centro(df_centros_tratado, conn)
    load_fact_movimentacao(df_mov_tratado, conn)

    conn.close()
    print("✅ Pipeline ETL finalizado com sucesso")
