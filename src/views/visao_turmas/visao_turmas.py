import streamlit as st
from src.controllers.turmas import list_class
from src.controllers.schools import list_schools
import pandas as pd

st.title("Escolas da Cidade")
st.subheader("Visão da Turma")

with st.spinner("Carregando Escolas..."):
    schools = list_schools(filters=None)

schools_df = pd.DataFrame(schools)

if not schools_df.empty:
    selected_school = st.selectbox(
        "Selecione a Escola", 
        options=schools_df['NO_ENTIDADE'].unique(),
        index=0
    )

    with st.spinner("Carregando Turmas..."):
        filtered_turmas = list_class(str(selected_school))

    if filtered_turmas:
        df = pd.DataFrame(filtered_turmas)
        df = df.rename(columns={
            "NO_TURMA": "Nome"
        })

        # Definir as colunas de disciplinas
        disciplinas = [
            "IN_DISC_QUIMICA",
            "IN_DISC_FISICA",
            "IN_DISC_MATEMATICA",
            "IN_DISC_BIOLOGIA",
            "IN_DISC_CIENCIAS",
            "IN_DISC_LINGUA_PORTUGUESA",
            "IN_DISC_LINGUA_INGLES",
            "IN_DISC_LINGUA_ESPANHOL",
            "IN_DISC_LINGUA_FRANCES",
            "IN_DISC_LINGUA_OUTRA",
            "IN_DISC_LINGUA_INDIGENA",
            "IN_DISC_ARTES",
            "IN_DISC_EDUCACAO_FISICA",
            "IN_DISC_HISTORIA",
            "IN_DISC_GEOGRAFIA",
            "IN_DISC_FILOSOFIA",
            "IN_DISC_ENSINO_RELIGIOSO",
            "IN_DISC_ESTUDOS_SOCIAIS",
            "IN_DISC_SOCIOLOGIA",
            "IN_DISC_EST_SOCIAIS_SOCIOLOGIA",
            "IN_DISC_INFORMATICA_COMPUTACAO",
            "IN_DISC_PROFISSIONALIZANTE",
            "IN_DISC_ATENDIMENTO_ESPECIAIS",
            "IN_DISC_DIVER_SOCIO_CULTURAL",
            "IN_DISC_LIBRAS",
            "IN_DISC_PEDAGOGICAS",
            "IN_DISC_OUTRAS"
        ]

        # Criar a coluna com os nomes das disciplinas onde o valor é True
        def get_disciplines(row):
            # Filtrar as disciplinas True e retornar os nomes
            return ', '.join([disciplina.replace("IN_DISC_", "").replace("_", " ") for disciplina in disciplinas if row[disciplina]])

        df['Disciplinas'] = df.apply(get_disciplines, axis=1)

        # Exibir o dataframe com quebra de linha nas células de 'Disciplinas'
        st.table(df[['Nome', 'Disciplinas']].apply(lambda x: x.str.wrap(50), axis=1))

    else:
        st.info(f"Nenhuma Turma Encontrada para a Escola {selected_school}")
else:
    st.info("Nenhuma Escola Encontrada!")
