import streamlit as st

st.title("🎈 Previsão de Ações 🪙💹")
st.write(
    "Ferramenta para calcular o valor de ações"
)

# Lista de opções
opcoes = ["aapl"]

# Criando o combobox
escolha = st.selectbox("Empresa:", opcoes)

