/*Verificar volume de registros carregados
# Quantidade de registros por tabela*/
SELECT 'dw.dim_centro_distribuicao' AS tabela, COUNT(*) AS total_registros
FROM dw.dim_centro_distribuicao
UNION ALL
SELECT 'dw.dim_fact_movimentacao_estoque', COUNT(*)
FROM dw.dim_fact_movimentacao_estoque;

/*Verificar chaves primárias nulas (erro grave)*/
SELECT *
FROM dw.dim_centro_distribuicao
WHERE cd_id IS NULL;

/*Movimentações sem centro correspondente não podem existir.*/
SELECT f.*
FROM dw.dim_fact_movimentacao_estoque f
LEFT JOIN dw.dim_centro_distribuicao d
    ON f.cd_id = d.cd_id
WHERE d.cd_id IS NULL;