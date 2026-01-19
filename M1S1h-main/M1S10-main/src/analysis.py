
import matplotlib.pyplot as plt
from .database import connect_db

# ============================================
# 1. Movimentação total (entrada e saída) por CD
# ============================================
def movimentacao_por_centro():
    conn = connect_db()
    query = """
        SELECT
            c.nome_centro_distribuicao,
            c.regiao,
            SUM(f.quantidade_entrada) AS total_entrada,
            SUM(f.quantidade_saida) AS total_saida
        FROM fact_movimentacao_estoque f
        JOIN dim_centro_distribuicao c
            ON f.id_centro = c.id_centro
        GROUP BY c.nome_centro_distribuicao, c.regiao
        ORDER BY total_saida DESC;
    """
    df = conn.execute(query).fetchall()
    conn.close()
    return df


# ============================================
# 2. Estoque final x capacidade por CD
# ============================================
def estoque_vs_capacidade():
    conn = connect_db()
    query = """
        SELECT
            c.nome_centro_distribuicao,
            c.regiao,
            c.capacidade_armazenagem,
            SUM(f.saldo_final) AS estoque_final,
            (c.capacidade_armazenagem - SUM(f.saldo_final)) AS saldo_disponivel
        FROM fact_movimentacao_estoque f
        JOIN dim_centro_distribuicao c
            ON f.id_centro = c.id_centro
        GROUP BY c.nome_centro_distribuicao, c.regiao, c.capacidade_armazenagem
        ORDER BY saldo_disponivel ASC;
    """
    df = conn.execute(query).fetchall()
    conn.close()
    return df


# ============================================
# 3. Média mensal de saída por centro
# ============================================
def media_saida_mensal_por_centro():
    conn = connect_db()
    query = """
        SELECT
            c.nome_centro_distribuicao,
            DATE_TRUNC('month', f.data_movimentacao) AS mes,
            AVG(f.quantidade_saida) AS media_saida
        FROM fact_movimentacao_estoque f
        JOIN dim_centro_distribuicao c
            ON f.id_centro = c.id_centro
        GROUP BY c.nome_centro_distribuicao, mes
        ORDER BY mes;
    """
    df = conn.execute(query).fetchall()
    conn.close()
    return df


# ============================================
# 4. Média de saída por produto e centro
# ============================================
def media_saida_por_produto_centro():
    conn = connect_db()
    query = """
        SELECT
            c.nome_centro_distribuicao,
            f.codigo_produto,
            AVG(f.quantidade_saida) AS media_saida
        FROM fact_movimentacao_estoque f
        JOIN dim_centro_distribuicao c
            ON f.id_centro = c.id_centro
        GROUP BY c.nome_centro_distribuicao, f.codigo_produto
        ORDER BY media_saida DESC;
    """
    df = conn.execute(query).fetchall()
    conn.close()
    return df
