import streamlit as st
import pandas as pd
from src.controllers.schools import list_teachers_students, list_schools

st.title("Professores e Alunos por Escola")

with st.spinner("Carregando..."):
    escolas = list_schools()
    escolas_select_box_df = pd.DataFrame(escolas)
    escolas_select_box_df = escolas_select_box_df.set_index('NO_ENTIDADE')['CO_ENTIDADE'].to_dict()    
    escola_selecionada = st.selectbox("Selecione a escola:", list(escolas_select_box_df.keys()), index=0)    

    # Usando session_state para armazenar a escola selecionada anterior
    if 'escola_selecionada_antiga' not in st.session_state:
        st.session_state.escola_selecionada_antiga = None

    # Verifica se houve mudança no valor selecionado
    if escola_selecionada != st.session_state.escola_selecionada_antiga:
        st.session_state.escola_selecionada_antiga = escola_selecionada  # Atualiza a seleção anterior
        
        # Se o valor selecionado não for vazio, obtém o código da escola selecionada
        if escola_selecionada:
            codigo_escola = escolas_select_box_df[escola_selecionada]
            teacher_students = list_teachers_students(codigo_escola)
            teacher_students_df = pd.DataFrame(teacher_students)
            
            # Exibe a escola filtrada
            if teacher_students_df.empty:
                st.info("O número de pessoas é zero!")
            else:
                teacher_students_df = teacher_students_df.rename(columns={
                  "CO_ENTIDADE": "Código da escola",
                  "NO_ENTIDADE": "Nome da escola",
                  "person_code": "Código do aluno ou docente",
                  "type": "Tipo (Aluno ou Docente)"
                })
                st.dataframe(teacher_students_df, use_container_width=True)
        else:
            st.info("Selecione uma escola!")
