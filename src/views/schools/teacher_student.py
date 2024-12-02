import streamlit as st
import pandas as pd
from src.controllers.schools import list_teachers_students, list_schools

st.title("Professores e Alunos por Escola")

with st.spinner("Carregando Escolas..."):
    schools = list_schools(filters=None)

schools_df = pd.DataFrame(schools)

if not schools_df.empty:
  selected_school = st.selectbox(
      "Selecione a Escola", 
      options=schools_df['NO_ENTIDADE'].unique(),
      index=0
  )

  with st.spinner("Carregando Alunos e Docentes..."):
        teacher_students = list_teachers_students(str(selected_school))

  if teacher_students:            
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
        
