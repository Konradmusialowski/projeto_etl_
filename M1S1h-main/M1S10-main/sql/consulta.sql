

SELECT
    d.nome_centro_distribuicao,
    f.codigo_produto,
    EXTRACT(YEAR FROM f.data_movimentacao) AS ano,
    EXTRACT(MONTH FROM f.data_movimentacao) AS mes,
    SUM(f.quantidade_entrada) AS total_entrada
FROM dw.dim_fact_movimentacao_estoque f
JOIN dw.dim_centro_distribuicao d
    ON f.cd_id = d.cd_id
GROUP BY
    d.nome_centro_distribuicao,
    f.codigo_produto,
    EXTRACT(YEAR FROM f.data_movimentacao),
    EXTRACT(MONTH FROM f.data_movimentacao)
ORDER BY
    ano,
    mes,
    d.nome_centro_distribuicao,
    total_entrada DESC;