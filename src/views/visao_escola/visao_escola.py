import streamlit as st
from src.controllers.schools import list_school_qtd_dashboard
import pandas as pd

# Título da página
st.title("Escolas da Cidade")
st.subheader("Visão da Escola")

# Carregando os dados
with st.spinner("Carregando Escolas..."):
    bookmarks = list_school_qtd_dashboard()

# Convertendo os dados em DataFrame
df = pd.DataFrame(bookmarks)

# Verificando se há dados
if df.empty:
    st.info("Nenhuma Escola Encontrada!")
else:
    # Renomeando as colunas
    df = df.rename(columns={
        "CO_ENTIDADE": "Código",
        "NO_ENTIDADE": "Nome",
        "Docentes": "Qtd. Professores",
        "Matricula": "Qtd. Alunos",
        "Turmas": "Qtd. Turmas",
    })
    
    # Paginação - Definindo o número de registros por página
    rows_per_page = 10
    total_rows = len(df)
    total_pages = (total_rows // rows_per_page) + (1 if total_rows % rows_per_page != 0 else 0)

    # Controlando a página atual
    page = st.slider("Escolha a página", min_value=1, max_value=total_pages, step=1, value=1)

    # Calculando os índices para a página selecionada
    start_row = (page - 1) * rows_per_page
    end_row = start_row + rows_per_page

    # Exibindo os dados da página selecionada
    st.dataframe(df.iloc[start_row:end_row], use_container_width=True)
    
    # Exibindo informações sobre a navegação
    st.text(f"Página {page} de {total_pages}")
