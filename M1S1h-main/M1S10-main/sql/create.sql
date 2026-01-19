CREATE TABLE  dw.dim_fact_movimentacao_estoque
(
    data_movimentacao date NOT NULL,
    cd_id integer NOT NULL,
    codigo_produto character varying(50) COLLATE pg_catalog."default" NOT NULL,
    descricao_produto character varying(255) COLLATE pg_catalog."default",
    quantidade_entrada integer DEFAULT 0,
    quantidade_saida integer DEFAULT 0,
    quantidade_liquida integer DEFAULT 0,
    saldo_final integer 0
    
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS dw.dim_fact_movimentacao_estoque
    OWNER to postgres;
CREATE TABLE dw.dim_centro_distribuicao
(
    id_centro integer ,
    cd_id integer,
    nome_centro_distribuicao character varying(150) COLLATE pg_catalog."default",
    regiao character varying(50) COLLATE pg_catalog."default",
    cidade character varying(100) COLLATE pg_catalog."default",
    estado character varying(2) COLLATE pg_catalog."default",
    capacidade_armazenagem integer,
    tipo_cd character varying(50) COLLATE pg_catalog."default"
    
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS dw.dim_centro_distribuicao
    OWNER to postgres;