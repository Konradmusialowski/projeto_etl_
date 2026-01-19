import os
import pandas as pd
from pathlib import Path

def exportar_query_sql_arquivo(conn, caminho_sql, nome_saida, formato="csv"):
    

    with open(caminho_sql, 'r', encoding='utf-8') as f:
        sql = f.read()

    df = pd.read_sql(sql, conn)

    output_dir = Path("data") / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    if formato == "csv":
        df.to_csv(output_dir / f"{nome_saida}.csv", index=False, sep=';')
    else:
        df.to_excel(output_dir / f"{nome_saida}.xlsx", index=False)

    print(f"✅ Exportado: {nome_saida}")

def executar_e_imprimir_sql(conn, sql, titulo=None):
    if titulo:
        print("\n" + "="*60)
        print(f"🔎 {titulo}")
        print("="*60)

    df = pd.read_sql(sql, conn)
    print(df)
    return df

def salvar_dataframe(df, nome_arquivo, formato="csv"):
    os.makedirs("saida", exist_ok=True)

    caminho = f"saida/{nome_arquivo}"

    if formato == "csv":
        df.to_csv(caminho + ".csv", index=False, sep=';', encoding='utf-8')

    elif formato == "excel":
        df.to_excel(caminho + ".xlsx", index=False)

    elif formato == "json":
        df.to_json(
            caminho + ".json",
            orient="records",
            force_ascii=False,
            indent=4
        )
def executar_sql_arquivo(conn, caminho_sql):
    """
    Executa um arquivo .sql no banco de dados.

    Parâmetros:
        conn: conexão psycopg2
        caminho_sql: Path ou string para o arquivo .sql
    """
    cursor = conn.cursor()

    with open(caminho_sql, 'r', encoding='utf-8') as file:
        sql_script = file.read()

    try:
        cursor.execute(sql_script)
        conn.commit()
        print(f"✅ Script executado com sucesso: {caminho_sql.name}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao executar {caminho_sql.name}")
        print(e)
    finally:
        cursor.close()



def exportar_query(
    conn,
    sql: str,
    nome_arquivo: str,
    formato: str = "csv"
):
    """
    Executa uma query SQL e salva o resultado em CSV ou Excel.

    Parâmetros:
        conn: conexão psycopg2
        sql: string SQL
        nome_arquivo: nome do arquivo sem extensão
        formato: 'csv' ou 'xlsx'
    """
    df = pd.read_sql(sql, conn)

    output_dir = Path("data") / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    caminho = output_dir / nome_arquivo

    if formato == "csv":
        df.to_csv(caminho.with_suffix(".csv"), index=False, sep=';', encoding='utf-8')
    elif formato == "xlsx":
        df.to_excel(caminho.with_suffix(".xlsx"), index=False)
    else:
        raise ValueError("Formato inválido. Use 'csv' ou 'xlsx'.")

    print(f"✅ Query exportada com sucesso: {caminho}.{formato}")
