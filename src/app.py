import streamlit as st
import mysql.connector
import pandas as pd

st.header("Primeiro título :100:")
st.markdown("""
    Primeira **linha** *aqui*
""")

conn = mysql.connector.connect(
    host='localhost',
    user="",
    password="",
    port=3306,
    db="",
    auth_plugin=''
)

cursor = conn.cursor()

cursor.execute("select * from vw_escola")
res = cursor.fetchall()
df = pd.DataFrame(res, columns=cursor.columns_names)

st.write(df)

st.sidebar.header("Sidebar")
st.sidebar.radio("Radio", df['NO_ENTIDADE'].unique())
