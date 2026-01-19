from src.database import connect_db
from src.etl.pipeline import run_pipeline
from src.utils import executar_sql_arquivo, exportar_query_sql_arquivo

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def main():
    conn = connect_db()

    # 1️⃣ Criar tabelas
    executar_sql_arquivo(conn, BASE_DIR / "sql" / "create.sql")

    # 2️⃣ Limpar tabelas
    executar_sql_arquivo(conn, BASE_DIR / "sql" / "clean.sql")
    exportar_query_sql_arquivo(conn, BASE_DIR / "sql" / "volume.sql","clean")


    # 3️⃣ Rodar ETL
    run_pipeline()
    exportar_query_sql_arquivo(conn, BASE_DIR / "sql" / "volume.sql","dados")

    # 4️⃣ (opcional) Rodar queries de validação
    executar_sql_arquivo(conn, BASE_DIR / "sql" / "validar.sql")

    #    salvar arquivo
    exportar_query_sql_arquivo(conn, BASE_DIR / "sql" / "consulta.sql","consulta" )
    exportar_query_sql_arquivo(conn, BASE_DIR / "sql" / "consulta2.sql","consulta2" )
    exportar_query_sql_arquivo(conn, BASE_DIR / "sql" / "consulta_produto.sql","consulta_produto" )


    conn.close()
    print("✅ Pipeline executado com sucesso")

if __name__ == "__main__":
    main()





