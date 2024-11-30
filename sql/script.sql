-- Versionamento 2024.10

CREATE DATABASE censo_escolar;

use censo_escolar;

SELECT @@global.secure_file_priv;

use censo_escolar;

create table docente
(
NU_ANO_CENSO int
, CO_PESSOA_FISICA bigint
, NU_DIA int
, NU_MES int
, NU_ANO int
, NU_IDADE_REFERENCIA int
, NU_IDADE int
, TP_SEXO int
, TP_COR_RACA int
, TP_NACIONALIDADE int
, CO_PAIS_ORIGEM int
, CO_UF_NASC int
, CO_MUNICIPIO_NASC int
, CO_UF_END int
, CO_MUNICIPIO_END int
, TP_ZONA_RESIDENCIAL int
, IN_NECESSIDADE_ESPECIAL bool
, IN_CEGUEIRA bool
, IN_BAIXA_VISAO bool
, IN_SURDEZ bool
, IN_DEF_AUDITIVA bool
, IN_SURDOCEGUEIRA bool
, IN_DEF_FISICA bool
, IN_DEF_INTELECTUAL bool
, IN_DEF_MULTIPLA bool
, TP_ESCOLARIDADE int
, TP_NORMAL_MAGISTERIO int
, TP_SITUACAO_CURSO_1 int
, CO_AREA_CURSO_1 int
, CO_CURSO_1 int
, IN_LICENCIATURA_1 bool
, IN_COM_PEDAGOGICA_1 bool
, NU_ANO_INICIO_1 int
, NU_ANO_CONCLUSAO_1 int
, TP_TIPO_IES_1 int
, CO_IES_1 int
, TP_SITUACAO_CURSO_2 int
, CO_AREA_CURSO_2 int
, CO_CURSO_2 int
, IN_LICENCIATURA_2 bool
, IN_COM_PEDAGOGICA_2 bool
, NU_ANO_INICIO_2 int
, NU_ANO_CONCLUSAO_2 int
, TP_TIPO_IES_2 int
, CO_IES_2 int
, TP_SITUACAO_CURSO_3 int
, CO_AREA_CURSO_3 int
, CO_CURSO_3 int
, IN_LICENCIATURA_3 bool
, IN_COM_PEDAGOGICA_3 bool
, NU_ANO_INICIO_3 int
, NU_ANO_CONCLUSAO_3 int
, TP_TIPO_IES_3 int
, CO_IES_3 int
, IN_DISC_QUIMICA bool
, IN_DISC_FISICA bool
, IN_DISC_MATEMATICA bool
, IN_DISC_BIOLOGIA bool
, IN_DISC_CIENCIAS bool
, IN_DISC_LINGUA_PORTUGUESA bool
, IN_DISC_LINGUA_INGLES bool
, IN_DISC_LINGUA_ESPANHOL bool
, IN_DISC_LINGUA_FRANCES bool
, IN_DISC_LINGUA_OUTRA bool
, IN_DISC_LINGUA_INDIGENA bool
, IN_DISC_ARTES bool
, IN_DISC_EDUCACAO_FISICA bool
, IN_DISC_HISTORIA bool
, IN_DISC_GEOGRAFIA bool
, IN_DISC_FILOSOFIA bool
, IN_DISC_ENSINO_RELIGIOSO bool
, IN_DISC_ESTUDOS_SOCIAIS bool
, IN_DISC_SOCIOLOGIA bool
, IN_DISC_EST_SOCIAIS_SOCIOLOGIA bool
, IN_DISC_INFORMATICA_COMPUTACAO bool
, IN_DISC_PROFISSIONALIZANTE bool
, IN_DISC_ATENDIMENTO_ESPECIAIS bool
, IN_DISC_DIVER_SOCIO_CULTURAL bool
, IN_DISC_LIBRAS bool
, IN_DISC_PEDAGOGICAS bool
, IN_DISC_OUTRAS bool
, IN_ESPECIALIZACAO bool
, IN_MESTRADO bool
, IN_DOUTORADO bool
, IN_POS_NENHUM bool
, IN_ESPECIFICO_CRECHE bool
, IN_ESPECIFICO_PRE_ESCOLA bool
, IN_ESPECIFICO_ANOS_INICIAIS bool
, IN_ESPECIFICO_ANOS_FINAIS bool
, IN_ESPECIFICO_ENS_MEDIO bool
, IN_ESPECIFICO_EJA bool
, IN_ESPECIFICO_ED_ESPECIAL bool
, IN_ESPECIFICO_ED_INDIGENA bool
, IN_ESPECIFICO_CAMPO bool
, IN_ESPECIFICO_AMBIENTAL bool
, IN_ESPECIFICO_DIR_HUMANOS bool
, IN_ESPECIFICO_DIV_SEXUAL bool
, IN_ESPECIFICO_DIR_ADOLESC bool
, IN_ESPECIFICO_AFRO bool
, IN_ESPECIFICO_OUTROS bool
, IN_ESPECIFICO_NENHUM bool
, TP_TIPO_DOCENTE int
, TP_TIPO_CONTRATACAO int
, ID_TURMA int
, TP_TIPO_TURMA int
, TP_MEDIACAO_DIDATICO_PEDAGO int
, IN_ESPECIAL_EXCLUSIVA bool
, IN_REGULAR bool
, IN_EJA bool
, IN_PROFISSIONALIZANTE bool
, TP_ETAPA_ENSINO int
, CO_CURSO_EDUC_PROFISSIONAL int
, CO_REGIAO int
, CO_MESORREGIAO int
, CO_MICRORREGIAO int
, CO_ENTIDADE int
, CO_UF int
, CO_MUNICIPIO int
, CO_DISTRITO int
, TP_DEPENDENCIA int
, TP_LOCALIZACAO int
, TP_CATEGORIA_ESCOLA_PRIVADA int
, IN_CONVENIADA_PP bool
, TP_CONVENIO_PODER_PUBLICO int
, IN_MANT_ESCOLA_PRIVADA_EMP bool
, IN_MANT_ESCOLA_PRIVADA_ONG bool
, IN_MANT_ESCOLA_PRIVADA_SIND bool
, IN_MANT_ESCOLA_PRIVADA_SIST_S bool
, IN_MANT_ESCOLA_PRIVADA_S_FINS bool
, TP_REGULAMENTACAO int
, TP_LOCALIZACAO_DIFERENCIADA int
, IN_EDUCACAO_INDIGENA bool
);
 
SET sql_mode = "";
load data infile 'C:\\ProgramData\\MySQL\\\MySQL Server 8.0\\Uploads\\Docentes Rio Claro 2017.csv'
into table censo_escolar.docente
fields terminated by '|'
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
;


create table escola
(
NU_ANO_CENSO int
, CO_ENTIDADE int
, NO_ENTIDADE varchar(100)
, CO_ORGAO_REGIONAL varchar(5)
, TP_SITUACAO_FUNCIONAMENTO int
, DT_ANO_LETIVO_INICIO varchar(11)
, DT_ANO_LETIVO_TERMINO varchar(11)
, CO_REGIAO  int
, CO_MESORREGIAO int
, CO_MICRORREGIAO int
, CO_UF int
, CO_MUNICIPIO int
, CO_DISTRITO int
, TP_DEPENDENCIA int
, TP_LOCALIZACAO int
, TP_CATEGORIA_ESCOLA_PRIVADA int null
, IN_CONVENIADA_PP bool
, TP_CONVENIO_PODER_PUBLICO int null
, IN_MANT_ESCOLA_PRIVADA_EMP bool null
, IN_MANT_ESCOLA_PRIVADA_ONG bool null
, IN_MANT_ESCOLA_PRIVADA_SIND bool null
, IN_MANT_ESCOLA_PRIVADA_SIST_S bool null
, IN_MANT_ESCOLA_PRIVADA_S_FINS bool null
, CO_ESCOLA_SEDE_VINCULADA int null
, CO_IES_OFERTANTE int null
, TP_REGULAMENTACAO int null
, IN_LOCAL_FUNC_PREDIO_ESCOLAR int
, TP_OCUPACAO_PREDIO_ESCOLAR int
, IN_LOCAL_FUNC_SALAS_EMPRESA bool
, IN_LOCAL_FUNC_SOCIOEDUCATIVO bool
, IN_LOCAL_FUNC_UNID_PRISIONAL bool
, IN_LOCAL_FUNC_PRISIONAL_SOCIO bool
, IN_LOCAL_FUNC_TEMPLO_IGREJA bool
, IN_LOCAL_FUNC_CASA_PROFESSOR bool
, IN_LOCAL_FUNC_GALPAO bool
, TP_OCUPACAO_GALPAO int null
, IN_LOCAL_FUNC_SALAS_OUTRA_ESC bool
, IN_LOCAL_FUNC_OUTROS bool
, IN_PREDIO_COMPARTILHADO bool
, IN_AGUA_FILTRADA bool
, IN_AGUA_REDE_PUBLICA bool
, IN_AGUA_POCO_ARTESIANO bool
, IN_AGUA_CACIMBA bool
, IN_AGUA_FONTE_RIO bool
, IN_AGUA_INEXISTENTE bool
, IN_ENERGIA_REDE_PUBLICA bool
, IN_ENERGIA_GERADOR bool
, IN_ENERGIA_OUTROS bool
, IN_ENERGIA_INEXISTENTE bool
, IN_ESGOTO_REDE_PUBLICA bool
, IN_ESGOTO_FOSSA bool
, IN_ESGOTO_INEXISTENTE bool
, IN_LIXO_COLETA_PERIODICA bool
, IN_LIXO_QUEIMA bool
, IN_LIXO_JOGA_OUTRA_AREA bool
, IN_LIXO_RECICLA bool
, IN_LIXO_ENTERRA bool
, IN_LIXO_OUTROS bool
, IN_SALA_DIRETORIA bool
, IN_SALA_PROFESSOR bool
, IN_LABORATORIO_INFORMATICA bool
, IN_LABORATORIO_CIENCIAS bool
, IN_SALA_ATENDIMENTO_ESPECIAL bool
, IN_QUADRA_ESPORTES_COBERTA bool
, IN_QUADRA_ESPORTES_DESCOBERTA bool
, IN_QUADRA_ESPORTES bool
, IN_COZINHA bool
, IN_BIBLIOTECA bool
, IN_SALA_LEITURA bool
, IN_BIBLIOTECA_SALA_LEITURA bool
, IN_PARQUE_INFANTIL bool
, IN_BERCARIO bool
, IN_BANHEIRO_FORA_PREDIO bool
, IN_BANHEIRO_DENTRO_PREDIO bool
, IN_BANHEIRO_EI bool
, IN_BANHEIRO_PNE bool
, IN_DEPENDENCIAS_PNE bool
, IN_SECRETARIA bool
, IN_BANHEIRO_CHUVEIRO bool
, IN_REFEITORIO bool
, IN_DESPENSA bool
, IN_ALMOXARIFADO bool
, IN_AUDITORIO bool
, IN_PATIO_COBERTO bool
, IN_PATIO_DESCOBERTO bool
, IN_ALOJAM_ALUNO bool
, IN_ALOJAM_PROFESSOR bool
, IN_AREA_VERDE bool
, IN_LAVANDERIA bool
, IN_DEPENDENCIAS_OUTRAS bool
, NU_SALAS_EXISTENTES bool
, NU_SALAS_UTILIZADAS int
, IN_EQUIP_TV bool
, IN_EQUIP_VIDEOCASSETE bool
, IN_EQUIP_DVD bool
, IN_EQUIP_PARABOLICA bool
, IN_EQUIP_COPIADORA bool
, IN_EQUIP_RETROPROJETOR bool
, IN_EQUIP_IMPRESSORA bool
, IN_EQUIP_IMPRESSORA_MULT bool
, IN_EQUIP_SOM bool
, IN_EQUIP_MULTIMIDIA bool
, IN_EQUIP_FAX bool
, IN_EQUIP_FOTO bool
, IN_COMPUTADOR bool
, NU_EQUIP_TV int
, NU_EQUIP_VIDEOCASSETE int
, NU_EQUIP_DVD int
, NU_EQUIP_PARABOLICA int
, NU_EQUIP_COPIADORA int
, NU_EQUIP_RETROPROJETOR int
, NU_EQUIP_IMPRESSORA int
, NU_EQUIP_IMPRESSORA_MULT int
, NU_EQUIP_SOM int
, NU_EQUIP_MULTIMIDIA int
, NU_EQUIP_FAX int
, NU_EQUIP_FOTO int
, NU_COMPUTADOR int
, NU_COMP_ADMINISTRATIVO int
, NU_COMP_ALUNO int
, IN_INTERNET bool
, IN_BANDA_LARGA bool
, NU_FUNCIONARIOS int
, IN_ALIMENTACAO bool
, TP_AEE int
, TP_ATIVIDADE_COMPLEMENTAR int
, IN_FUNDAMENTAL_CICLOS bool
, TP_LOCALIZACAO_DIFERENCIADA int
, IN_MATERIAL_ESP_QUILOMBOLA bool
, IN_MATERIAL_ESP_INDIGENA bool
, IN_MATERIAL_ESP_NAO_UTILIZA bool
, IN_EDUCACAO_INDIGENA bool
, TP_INDIGENA_LINGUA int
, CO_LINGUA_INDIGENA int
, IN_BRASIL_ALFABETIZADO bool
, IN_FINAL_SEMANA bool
, IN_FORMACAO_ALTERNANCIA bool
, IN_MEDIACAO_PRESENCIAL bool
, IN_MEDIACAO_SEMIPRESENCIAL bool
, IN_MEDIACAO_EAD bool
, IN_ESPECIAL_EXCLUSIVA bool
, IN_REGULAR bool
, IN_EJA bool
, IN_PROFISSIONALIZANTE bool
, IN_COMUM_CRECHE bool
, IN_COMUM_PRE bool
, IN_COMUM_FUND_AI bool
, IN_COMUM_FUND_AF bool
, IN_COMUM_MEDIO_MEDIO bool
, IN_COMUM_MEDIO_INTEGRADO bool
, IN_COMUM_MEDIO_NORMAL bool
, IN_ESP_EXCLUSIVA_CRECHE bool
, IN_ESP_EXCLUSIVA_PRE bool
, IN_ESP_EXCLUSIVA_FUND_AI bool
, IN_ESP_EXCLUSIVA_FUND_AF bool
, IN_ESP_EXCLUSIVA_MEDIO_MEDIO bool
, IN_ESP_EXCLUSIVA_MEDIO_INTEGR bool
, IN_ESP_EXCLUSIVA_MEDIO_NORMAL bool
, IN_COMUM_EJA_FUND bool
, IN_COMUM_EJA_MEDIO bool
, IN_COMUM_EJA_PROF bool
, IN_ESP_EXCLUSIVA_EJA_FUND bool
, IN_ESP_EXCLUSIVA_EJA_MEDIO bool
, IN_ESP_EXCLUSIVA_EJA_PROF bool
, IN_COMUM_PROF bool
, IN_ESP_EXCLUSIVA_PROF bool
);

load data infile 'C:\\ProgramData\\MySQL\\\MySQL Server 8.0\\Uploads\\Escolas Rio Claro 2017.csv'
into table censo_escolar.escola
fields terminated by '|'
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
;

create table turma
(
NU_ANO_CENSO int
, ID_TURMA int
, NO_TURMA varchar(80)
, TX_HR_INICIAL varchar(2)
, TX_MI_INICIAL varchar(2)
, NU_DURACAO_TURMA int
, NU_MATRICULAS int
, TP_MEDIACAO_DIDATICO_PEDAGO int
, IN_ESPECIAL_EXCLUSIVA bool
, IN_REGULAR bool
, IN_EJA bool
, IN_PROFISSIONALIZANTE bool
, TP_ETAPA_ENSINO int
, CO_CURSO_EDUC_PROFISSIONAL int
, TP_TIPO_TURMA int
, IN_MAIS_EDUCACAO bool
, NU_DIAS_ATIVIDADE int
, IN_DIA_SEMANA_DOMINGO bool
, IN_DIA_SEMANA_SEGUNDA bool
, IN_DIA_SEMANA_TERCA bool
, IN_DIA_SEMANA_QUARTA bool
, IN_DIA_SEMANA_QUINTA bool
, IN_DIA_SEMANA_SEXTA bool
, IN_DIA_SEMANA_SABADO bool
, CO_TIPO_ATIVIDADE_1 int
, CO_TIPO_ATIVIDADE_2 int
, CO_TIPO_ATIVIDADE_3 int
, CO_TIPO_ATIVIDADE_4 int
, CO_TIPO_ATIVIDADE_5 int
, CO_TIPO_ATIVIDADE_6 int
, IN_BRAILLE bool
, IN_RECURSOS_BAIXA_VISAO bool
, IN_PROCESSOS_MENTAIS bool
, IN_ORIENTACAO_MOBILIDADE bool
, IN_SINAIS bool
, IN_COMUNICACAO_ALT_AUMENT bool
, IN_ENRIQ_CURRICULAR bool
, IN_SOROBAN bool
, IN_INFORMATICA_ACESSIVEL bool
, IN_PORT_ESCRITA bool
, IN_AUTONOMIA_ESCOLAR bool
, IN_DISC_QUIMICA bool
, IN_DISC_FISICA bool
, IN_DISC_MATEMATICA bool
, IN_DISC_BIOLOGIA bool
, IN_DISC_CIENCIAS bool
, IN_DISC_LINGUA_PORTUGUESA bool
, IN_DISC_LINGUA_INGLES bool
, IN_DISC_LINGUA_ESPANHOL bool
, IN_DISC_LINGUA_FRANCES bool
, IN_DISC_LINGUA_OUTRA bool
, IN_DISC_LINGUA_INDIGENA bool
, IN_DISC_ARTES bool
, IN_DISC_EDUCACAO_FISICA bool
, IN_DISC_HISTORIA bool
, IN_DISC_GEOGRAFIA bool
, IN_DISC_FILOSOFIA bool
, IN_DISC_ENSINO_RELIGIOSO bool
, IN_DISC_ESTUDOS_SOCIAIS bool
, IN_DISC_SOCIOLOGIA bool
, IN_DISC_EST_SOCIAIS_SOCIOLOGIA bool
, IN_DISC_INFORMATICA_COMPUTACAO bool
, IN_DISC_PROFISSIONALIZANTE bool
, IN_DISC_ATENDIMENTO_ESPECIAIS bool
, IN_DISC_DIVER_SOCIO_CULTURAL bool
, IN_DISC_LIBRAS bool
, IN_DISC_PEDAGOGICAS bool
, IN_DISC_OUTRAS bool
, CO_ENTIDADE int
, CO_REGIAO int
, CO_MESORREGIAO int
, CO_MICRORREGIAO int
, CO_UF int
, CO_MUNICIPIO int
, CO_DISTRITO int
, TP_DEPENDENCIA int
, TP_LOCALIZACAO int
, TP_CATEGORIA_ESCOLA_PRIVADA int
, IN_CONVENIADA_PP bool
, TP_CONVENIO_PODER_PUBLICO int
, IN_MANT_ESCOLA_PRIVADA_EMP bool
, IN_MANT_ESCOLA_PRIVADA_ONG bool
, IN_MANT_ESCOLA_PRIVADA_SIND bool
, IN_MANT_ESCOLA_PRIVADA_SIST_S bool
, IN_MANT_ESCOLA_PRIVADA_S_FINS bool
, TP_REGULAMENTACAO int
, TP_LOCALIZACAO_DIFERENCIADA int
, IN_EDUCACAO_INDIGENA bool
);

SET sql_mode = "";
load data infile 'C:\\ProgramData\\MySQL\\\MySQL Server 8.0\\Uploads\\Turmas Rio Claro 2017.csv'
into table censo_escolar.turma
fields terminated by '|'
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
;

create table matricula
(
NU_ANO_CENSO int
, ID_MATRICULA bigint
, CO_PESSOA_FISICA varchar(12)
, NU_DIA int
, NU_MES int
, NU_ANO int
, NU_IDADE_REFERENCIA int
, NU_IDADE int
, NU_DURACAO_TURMA int
, NU_DUR_ATIV_COMP_MESMA_REDE int
, NU_DUR_ATIV_COMP_OUTRAS_REDES int
, NU_DUR_AEE_MESMA_REDE int
, NU_DUR_AEE_OUTRAS_REDES int
, NU_DIAS_ATIVIDADE int
, TP_SEXO int
, TP_COR_RACA int
, TP_NACIONALIDADE int
, CO_PAIS_ORIGEM int
, CO_UF_NASC int
, CO_MUNICIPIO_NASC int
, CO_UF_END int
, CO_MUNICIPIO_END int
, TP_ZONA_RESIDENCIAL int
, TP_OUTRO_LOCAL_AULA int
, IN_TRANSPORTE_PUBLICO bool
, TP_RESPONSAVEL_TRANSPORTE int
, IN_TRANSP_VANS_KOMBI bool
, IN_TRANSP_MICRO_ONIBUS bool
, IN_TRANSP_ONIBUS bool
, IN_TRANSP_BICICLETA bool
, IN_TRANSP_TR_ANIMAL bool
, IN_TRANSP_OUTRO_VEICULO bool
, IN_TRANSP_EMBAR_ATE5 bool
, IN_TRANSP_EMBAR_5A15 bool
, IN_TRANSP_EMBAR_15A35 bool
, IN_TRANSP_EMBAR_35 bool
, IN_TRANSP_TREM_METRO bool
, IN_NECESSIDADE_ESPECIAL bool
, IN_CEGUEIRA bool
, IN_BAIXA_VISAO bool
, IN_SURDEZ bool
, IN_DEF_AUDITIVA bool
, IN_SURDOCEGUEIRA bool
, IN_DEF_FISICA bool
, IN_DEF_INTELECTUAL bool
, IN_DEF_MULTIPLA bool
, IN_AUTISMO bool
, IN_SINDROME_ASPERGER bool
, IN_SINDROME_RETT bool
, IN_TRANSTORNO_DI bool
, IN_SUPERDOTACAO bool
, IN_RECURSO_LEDOR bool
, IN_RECURSO_TRANSCRICAO bool
, IN_RECURSO_INTERPRETE bool
, IN_RECURSO_LIBRAS bool
, IN_RECURSO_LABIAL bool
, IN_RECURSO_BRAILLE bool
, IN_RECURSO_AMPLIADA_16 bool
, IN_RECURSO_AMPLIADA_20 bool
, IN_RECURSO_AMPLIADA_24 bool
, IN_RECURSO_NENHUM bool
, TP_INGRESSO_FEDERAIS int
, TP_MEDIACAO_DIDATICO_PEDAGO int
, IN_ESPECIAL_EXCLUSIVA bool
, IN_REGULAR bool
, IN_EJA bool
, IN_PROFISSIONALIZANTE bool
, TP_ETAPA_ENSINO int
, ID_TURMA int
, CO_CURSO_EDUC_PROFISSIONAL int
, TP_UNIFICADA int
, TP_TIPO_TURMA int
, CO_ENTIDADE int
, CO_REGIAO int
, CO_MESORREGIAO int
, CO_MICRORREGIAO int
, CO_UF int
, CO_MUNICIPIO int
, CO_DISTRITO int
, TP_DEPENDENCIA int
, TP_LOCALIZACAO int
, TP_CATEGORIA_ESCOLA_PRIVADA int
, IN_CONVENIADA_PP bool
, TP_CONVENIO_PODER_PUBLICO int
, IN_MANT_ESCOLA_PRIVADA_EMP bool
, IN_MANT_ESCOLA_PRIVADA_ONG bool
, IN_MANT_ESCOLA_PRIVADA_SIND bool
, IN_MANT_ESCOLA_PRIVADA_SIST_S bool
, IN_MANT_ESCOLA_PRIVADA_S_FINS bool
, TP_REGULAMENTACAO int
, TP_LOCALIZACAO_DIFERENCIADA int
, IN_EDUCACAO_INDIGENA bool
);

SET sql_mode = "";
load data infile 'C:\\ProgramData\\MySQL\\\MySQL Server 8.0\\Uploads\\Matriculas Rio Claro 2017.csv'
into table censo_escolar.matricula
fields terminated by '|'
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
;

CREATE TABLE ideb(
CO_ENTIDADE int,
DEPENDENCIA_ID int,
ANO int,
IDEB_AI float,
IDEB_AF float,
IDEB_EM float
);

SET sql_mode = "";
load data infile 'C:\\ProgramData\\MySQL\\\MySQL Server 8.0\\Uploads\\ideb_2017_rio claro.csv'
into table censo_escolar.ideb
fields terminated by ';'
enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
;

CREATE TABLE usuario
(
    id INT,
    nome VARCHAR(255),
    email VARCHAR(255),
    data_cadastro DATE,
    data_nascimento DATE,
    senha VARCHAR(255),
    PRIMARY KEY (id)
);

CREATE TABLE bookmark (
    id INT AUTO_INCREMENT,
    id_usuario INT,
    id_escola INT,
    PRIMARY KEY (id)
);

-- ADD CONSTRAINT
ALTER TABLE usuario ADD CONSTRAINT UNIQUE (EMAIL);
ALTER TABLE usuario MODIFY COLUMN id INT AUTO_INCREMENT;
ALTER TABLE usuario MODIFY COLUMN NOME VARCHAR(255) NOT NULL;

-- CRIAR PKS

ALTER TABLE escola ADD CONSTRAINT PRIMARY KEY (CO_ENTIDADE);
ALTER TABLE turma ADD CONSTRAINT PRIMARY KEY (ID_TURMA);
ALTER TABLE docente ADD CONSTRAINT PRIMARY KEY (CO_PESSOA_FISICA, ID_TURMA);
ALTER TABLE matricula ADD CONSTRAINT PRIMARY KEY (ID_MATRICULA);
ALTER TABLE ideb ADD CONSTRAINT PRIMARY KEY (CO_ENTIDADE);

-- RELACIONAMENTO ENTRE AS TABELAS

ALTER TABLE bookmark ADD CONSTRAINT FOREIGN KEY (id_escola) REFERENCES escola(CO_ENTIDADE);
ALTER TABLE bookmark ADD CONSTRAINT FOREIGN KEY (id_usuario) REFERENCES usuario(id);
ALTER TABLE docente ADD CONSTRAINT FOREIGN KEY (ID_TURMA) REFERENCES turma(ID_TURMA);
ALTER TABLE ideb ADD CONSTRAINT FOREIGN KEY (CO_ENTIDADE) REFERENCES escola(CO_ENTIDADE);

-- AULA 21/09
CREATE VIEW Escolas_Ativas AS SELECT * FROM Escola WHERE TP_SITUACAO_FUNCIONAMENTO =1;

CREATE VIEW Colunas_Usadas_Escola AS SELECT NO_ENTIDADE, CO_ENTIDADE, DT_ANO_LETIVO_INICIO, DT_ANO_LETIVO_TERMINO  FROM Escola;
CREATE VIEW Colunas_Usadas_Matricula AS SELECT ID_MATRICULA, NU_IDADE FROM Matricula;
CREATE VIEW Colunas_Usadas_Turma AS SELECT NU_MATRICULAS, NO_TURMA FROM Turma;
CREATE VIEW Colunas_Usadas_Docente AS SELECT CO_PESSOA_FISICA, NU_IDADE_REFERENCIA, TP_SEXO FROM Docente;

CREATE VIEW Num_Professores_Escolas_Ativas AS 
	SELECT
		CASE 
			WHEN e.TP_LOCALIZACAO = 1 THEN 'Urbana' 
			WHEN e.TP_LOCALIZACAO = 2 THEN 'Rural' 
		END AS TP_LOCALIZACAO,
        CASE
			WHEN e.TP_DEPENDENCIA = 1 THEN 'Federal'
			WHEN e.TP_DEPENDENCIA = 2 THEN 'Estadual'
			WHEN e.TP_DEPENDENCIA = 3 THEN 'Municipal'
			WHEN e.TP_DEPENDENCIA = 4 THEN 'Privada'
        END AS TP_DEPENDENCIA,
	COUNT(DISTINCT d.CO_PESSOA_FISICA) AS TOTAL_DOCENTES
	FROM Escola e
    JOIN docente d ON d.CO_ENTIDADE = e.CO_ENTIDADE
    WHERE TP_SITUACAO_FUNCIONAMENTO = 1;

DELIMITER $$
CREATE FUNCTION Dias_Letivos(DT_ANO_LETIVO_INICIO DATE, DT_ANO_LETIVO_TERMINO DATE) 
	RETURNS INT 
    DETERMINISTIC 
    BEGIN 
		RETURN DATEDIFF(DT_ANO_LETIVO_TERMINO, DT_ANO_LETIVO_INICIO);
	END $$
DELIMITER ;

DELIMITER $$
CREATE FUNCTION Validar_Email(email VARCHAR(255))
RETURNS BOOLEAN
DETERMINISTIC
BEGIN
    IF email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' THEN
        RETURN TRUE;
    ELSE
        RETURN FALSE;
    END IF;
END $$
DELIMITER ;

CREATE FUNCTION Etapa_Ensino(TP_ETAPA_ENSINO INT)
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
	CASE TP_ETAPA_ENSINO
        WHEN 1 THEN 'Educação Infantil - Creche'
        WHEN 2 THEN 'Educação Infantil - Pré-escola'
        WHEN 3 THEN 'Educação Infantil - Unificada'
        WHEN 56 THEN 'Educação Infantil e Ensino Fundamental (8 e 9 anos) Multietapa'
        WHEN 4 THEN 'Ensino Fundamental de 8 anos - 1ª Série'
        WHEN 5 THEN 'Ensino Fundamental de 8 anos - 2ª Série'
        WHEN 6 THEN 'Ensino Fundamental de 8 anos - 3ª Série'
        WHEN 7 THEN 'Ensino Fundamental de 8 anos - 4ª Série'
        WHEN 8 THEN 'Ensino Fundamental de 8 anos - 5ª Série'
        WHEN 9 THEN 'Ensino Fundamental de 8 anos - 6ª Série'
        WHEN 10 THEN 'Ensino Fundamental de 8 anos - 7ª Série'
        WHEN 11 THEN 'Ensino Fundamental de 8 anos - 8ª Série'
        WHEN 12 THEN 'Ensino Fundamental de 8 anos - Multi'
        WHEN 13 THEN 'Ensino Fundamental de 8 anos - Correção de Fluxo'
        WHEN 14 THEN 'Ensino Fundamental de 9 anos - 1º Ano'
        WHEN 15 THEN 'Ensino Fundamental de 9 anos - 2º Ano'
        WHEN 16 THEN 'Ensino Fundamental de 9 anos - 3º Ano'
        WHEN 17 THEN 'Ensino Fundamental de 9 anos - 4º Ano'
        WHEN 18 THEN 'Ensino Fundamental de 9 anos - 5º Ano'
        WHEN 19 THEN 'Ensino Fundamental de 9 anos - 6º Ano'
        WHEN 20 THEN 'Ensino Fundamental de 9 anos - 7º Ano'
        WHEN 21 THEN 'Ensino Fundamental de 9 anos - 8º Ano'
        WHEN 41 THEN 'Ensino Fundamental de 9 anos - 9º Ano'
        WHEN 22 THEN 'Ensino Fundamental de 9 anos - Multi'
        WHEN 23 THEN 'Ensino Fundamental de 9 anos - Correção de Fluxo'
        WHEN 24 THEN 'Ensino Fundamental de 8 e 9 anos - Multi 8 e 9 anos'
        WHEN 25 THEN 'Ensino Médio - 1ª Série'
        WHEN 26 THEN 'Ensino Médio - 2ª Série'
        WHEN 27 THEN 'Ensino Médio - 3ª Série'
        WHEN 28 THEN 'Ensino Médio - 4ª Série'
        WHEN 29 THEN 'Ensino Médio - Não Seriada'
        WHEN 30 THEN 'Curso Técnico Integrado (Ensino Médio Integrado) 1ª Série'
        WHEN 31 THEN 'Curso Técnico Integrado (Ensino Médio Integrado) 2ª Série'
        WHEN 32 THEN 'Curso Técnico Integrado (Ensino Médio Integrado) 3ª Série'
        WHEN 33 THEN 'Curso Técnico Integrado (Ensino Médio Integrado) 4ª Série'
        WHEN 34 THEN 'Curso Técnico Integrado (Ensino Médio Integrado) Não Seriada'
        WHEN 35 THEN 'Ensino Médio - Normal/Magistério 1ª Série'
        WHEN 36 THEN 'Ensino Médio - Normal/Magistério 2ª Série'
        WHEN 37 THEN 'Ensino Médio - Normal/Magistério 3ª Série'
        WHEN 38 THEN 'Ensino Médio - Normal/Magistério 4ª Série'
        WHEN 39 THEN 'Curso Técnico - Concomitante'
        WHEN 40 THEN 'Curso Técnico - Subsequente'
        WHEN 64 THEN 'Curso Técnico Misto (Concomitante e Subsequente)'
        WHEN 68 THEN 'Curso FIC Concomitante'
        WHEN 65 THEN 'EJA - Ensino Fundamental - Projovem Urbano'
        WHEN 67 THEN 'Curso FIC integrado na modalidade EJA - Nível Médio'
        WHEN 69 THEN 'EJA - Ensino Fundamental - Anos Iniciais'
        WHEN 70 THEN 'EJA - Ensino Fundamental - Anos Finais'
        WHEN 71 THEN 'EJA - Ensino Médio'
        WHEN 72 THEN 'EJA - Ensino Fundamental - Anos Iniciais e Anos Finais'
        WHEN 73 THEN 'Curso FIC integrado na modalidade EJA - Nível Fundamental (EJA integrada à Educação Profissional de Nível Fundamental)'
        WHEN 74 THEN 'Curso Técnico Integrado na Modalidade EJA (EJA integrada à Educação Profissional de Nível Médio)'
        ELSE 'Etapa de Ensino Desconhecida'
	END
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE Listar_Escolas(offset_param INT, limit_param INT)
BEGIN
    SELECT *
    FROM escola
    ORDER BY CO_ENTIDADE
    LIMIT limit_param OFFSET offset_param;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER Verificar_Tamanho_Senha
BEFORE INSERT ON usuario
FOR EACH ROW
BEGIN
    IF CHAR_LENGTH(NEW.senha) != 40 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'A senha deve ter 40 caracteres (hash SHA-1).';
    END IF;
END $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER Verificar_Email
BEFORE INSERT ON usuario
FOR EACH ROW
BEGIN
    IF Validar_Email(NEW.email) = FALSE THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'O formato do e-mail é inválido.';
    END IF;
END $$
DELIMITER ;