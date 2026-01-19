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

/*Verificar datas inválidas ou nulas*/
SELECT *
FROM dw.dim_fact_movimentacao_estoque
WHERE dw.dim_data_movimentacao IS NULL;

/*Entradas  negativas (não permitido)*/
SELECT *
FROM fact_movimentacao_estoque
WHERE quantidade_entrada < 0

/*Verificar duplicidade de movimentações*/
SELECT
    cd_id,
    codigo_produto,
    data_movimentacao,
    COUNT(*) AS total
FROM fact_movimentacao_estoque
GROUP BY
    cd_id,
    codigo_produto,
    data_movimentacao
HAVING COUNT(*) > 1;

/* verificar entradas e saidas*/
SELECT
    cd_id,
    SUM(quantidade_entrada) AS total_entrada,
    SUM(quantidade_saida) AS total_saida
FROM dw.dim_fact_movimentacao_estoque
GROUP BY cd_id;

/*total de saidas e entradas por centro e por produto*/

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

/* quantificar estoque total e capacidade*/
SELECT
    d.nome_centro_distribuicao,
    d.capacidade_armazenagem,
    SUM(f.quantidade_entrada - f.quantidade_saida) AS estoque_calculado
FROM dw.dim_fact_movimentacao_estoque f
JOIN dw.dim_centro_distribuicao d
    ON f.cd_id = d.cd_id
GROUP BY
    d.nome_centro_distribuicao,
    d.capacidade_armazenagem
ORDER BY estoque_calculado DESC;

/*Total de entradas e saídas por produto*/
SELECT
    codigo_produto,
    SUM(quantidade_entrada) AS total_entrada,
    SUM(quantidade_saida)   AS total_saida
FROM dw.dim_fact_movimentacao_estoque
GROUP BY codigo_produto
ORDER BY total_entrada DESC;

/*total de saidas e entradas por centro e por produto*/




/*media*/
SELECT  distinct f.codigo_produto,
   		d.nome_centro_distribuicao,
    
    AVG(f.quantidade_saida) AS media_saida
FROM dw.dim_centro_distribuicao d
JOIN dw.dim_fact_movimentacao_estoque f
    ON f.cd_id = d.cd_id
GROUP BY
    d.nome_centro_distribuicao,
    f.codigo_produto
ORDER BY f.codigo_produto DESC;

/* media por mes */
SELECT DISTINCT
    d.nome_centro_distribuicao,
    f.codigo_produto,
    DATE_TRUNC('month', f.data_movimentacao) AS mes,
    AVG(f.quantidade_saida) AS media_saida_mensal
FROM dw.dim_fact_movimentacao_estoque f
JOIN dw.dim_centro_distribuicao d
    ON f.cd_id = d.cd_id
GROUP BY
    d.nome_centro_distribuicao,
    f.codigo_produto,
    mes
ORDER BY
    d.nome_centro_distribuicao,
    f.codigo_produto,
    mes;

