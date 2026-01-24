import pandas as pd
import numpy as np
import re,os

# -------------------------
# Função auxiliar
# -------------------------
def snake_case(col: str) -> str:
    col = col.strip().lower()
    col = re.sub(r'[^\w]+', '_', col)
    return col


# =========================
# TRANSFORMA CENTROS
# =========================
def transform_centros(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Padronizar colunas
    df.columns = [snake_case(c) for c in df.columns]

    # Remover duplicatas
    df.drop_duplicates(inplace=True)
     # Converter tipos
    df['capacidade_armazenagem'] = pd.to_numeric(
        df.get('capacidade_armazenagem', 0),
        errors='coerce'
    ).fillna(0).astype(int)

    df['tipo_cd'] = df.get('tipo_cd', 'NÃO INFORMADO').fillna('NÃO INFORMADO')
    # Tratar valores nulos (texto)
    df.fillna('NAO INFORMADO', inplace=True)
    print("Colunas disponíveis:", df.columns.tolist())


    return df


# =========================
# TRANSFORMA MOVIMENTAÇÃO
# =========================
def transform_movimentacao(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Padronizar colunas
    df.columns = [snake_case(c) for c in df.columns]

    # Converter data
    df['data_movimentacao'] = pd.to_datetime( df['data_movimentacao'],format='%D/%m/%Y' , errors='coerce')

    # Tratar nulos
    df['quantidade_entrada'] = df['quantidade_entrada'].fillna(0)
    df['quantidade_saida'] = df['quantidade_saida'].fillna(0)

    # Criar coluna quantidade (entrada - saída)
    # df['quantidade'] = df['quantidade_entrada'] - df['quantidade_saida']

     # Garantir numéricos
    df['quantidade_entrada'] = df['quantidade_entrada'].fillna(0).astype(int)
    df['quantidade_saida'] = df['quantidade_saida'].fillna(0).astype(int)

    # Criar quantidade líquida
    df['quantidade_liquida'] = (
        df['quantidade_entrada'] - df['quantidade_saida']
    )
    
    # Ordenar para cálculo correto do saldo
    df.sort_values(
        by=['codigo_produto', 'cd_id', 'data_movimentacao'],
        inplace=True
    )
    pasta_saida = "saida"
    os.makedirs(pasta_saida, exist_ok=True)
    caminho = os.path.join(pasta_saida, 'movimentação')
    df.to_csv(caminho + ".csv", index=False, sep=';', encoding='utf-8')
    df.to_excel(caminho + ".xlsx", index=False)
    

    # =========================
    # GROUP BY ENTRADA
    # =========================
    df_entrada = (
        df[df['quantidade_entrada'] > 0]
        .groupby(['cd_id', 'codigo_produto'], as_index=False)
        .agg(total_entrada=('quantidade_entrada', 'sum'))
    )

    # =========================
    # GROUP BY SAÍDA
    # =========================
    df_saida = (
        df[df['quantidade_saida'] > 0]
        .groupby(['cd_id', 'codigo_produto'], as_index=False)
        .agg(total_saida=('quantidade_saida', 'sum'))
    )

    # =========================
    # CONFRONTO ENTRADA x SAÍDA
    # =========================
    df_confronto = pd.merge(
        df_entrada,
        df_saida,
        on=['cd_id', 'codigo_produto'],
        how='outer'
    ).fillna(0)

        # Saldo consolidado
    df_confronto['saldo_consolidado'] = (
        df_confronto['total_entrada'] - df_confronto['total_saida']
    )
    df_confronto['saldo_consolidado'] = df_confronto['saldo_consolidado'].fillna(0)

    print("\nResumo ENTRADA x SAÍDA:")
    print(df_confronto.head())
    print(df.info)

    # =========================
    # SALDO FINAL ACUMULADO
    # =========================
    df['saldo_final'] = df_confronto.sort_values('data_movimentacao').groupby(
        ['cd_id', 'data_movimentacao', 'codigo_produto']
    )['saldo_consolidado'].cumsum()

    df['saldo_final'] = df['saldo_final'].fillna(0)

    return df
