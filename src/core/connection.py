import streamlit as st
import mysql.connector

# Conexão ao banco de dados
def get_connection():
    return mysql.connector.connect(
        host=st.secrets.db_credentials.host,
        user=st.secrets.db_credentials.user,
        password=st.secrets.db_credentials.password,
        database=st.secrets.db_credentials.db,
        port=16202
    )