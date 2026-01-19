
SELECT distinct
    d.nome_centro_distribuicao,
    f.codigo_produto,
    SUM(f.quantidade_entrada) AS total_entrada,
    SUM(f.quantidade_saida)   AS total_saida
FROM dw.dim_fact_movimentacao_estoque f
JOIN dw.dim_centro_distribuicao d
    ON f.cd_id = d.cd_id
GROUP BY
    d.nome_centro_distribuicao,
    f.codigo_produto
ORDER BY
    d.nome_centro_distribuicao,
    total_saida DESC;