SELECT 'dw.dim_centro_distribuicao' AS tabela, COUNT(*) AS total_registros
FROM dw.dim_centro_distribuicao
UNION ALL
SELECT 'dw.dim_fact_movimentacao_estoque', COUNT(*)
FROM dw.dim_fact_movimentacao_estoque;