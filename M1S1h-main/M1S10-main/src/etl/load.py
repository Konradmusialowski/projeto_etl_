import pandas as pd
def load_dim_centro(df: pd.DataFrame, conn):
    
    cursor = conn.cursor()
    

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO dw.dim_centro_distribuicao (
                cd_id,
                nome_centro_distribuicao,
                regiao,
                capacidade_armazenagem,
                tipo_cd
               
            )
        VALUES (%s, %s, %s, %s, %s)
        
          
        """, (
            row.get('cd_id'),
            row.get('nome_centro_distribuicao'),
            row.get('regiao'),
            int(row.get('capacidade_armazenagem', 0)),
            row.get('tipo_cd')
            
        ))

    conn.commit()
    cursor.close()

    print("✅ dim_centro_distribuicao carregada com sucesso")


      


def load_fact_movimentacao(df: pd.DataFrame, conn):
    cursor = conn.cursor()

    print("Col load:", df.columns.tolist())
    print(df.head())
    for _, row in df.iterrows():
        cursor.execute("""
                       INSERT INTO dw.dim_fact_movimentacao_estoque (
                        data_movimentacao,
                        cd_id,
                        codigo_produto,
                        descricao_produto,
                        quantidade_entrada,
                        quantidade_saida,
                        quantidade_liquida,
                        saldo_final
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
            row.get('data_movimentacao'),
            int(row.get('cd_id', 0)),
            row.get('codigo_produto'),
            row.get('descricao_produto'),
            int(row.get('quantidade_entrada', 0)),
            int(row.get('quantidade_saida', 0)),
            int(row.get('quantidade_liquida', 0)),
            int(row.get('saldo_final', 0))
        ))

    conn.commit()
    cursor.close()

    print("✅ fact_movimentacao_estoque carregada com sucesso")
