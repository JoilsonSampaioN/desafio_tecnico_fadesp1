-- Criação do esquema relacional para PostgreSQL

CREATE TABLE instituicoes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255),
    sigla_uf VARCHAR(2)
);

CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    instituicao_id INTEGER REFERENCES instituicoes(id),
    nome VARCHAR(255),
    categoria_adm VARCHAR(100),
    organizacao_academica VARCHAR(100)
);

CREATE TABLE bolsistas (
    id SERIAL PRIMARY KEY,
    instituicao_id INTEGER REFERENCES instituicoes(id),
    beneficiario VARCHAR(255),
    linha_fomento VARCHAR(255)
);
