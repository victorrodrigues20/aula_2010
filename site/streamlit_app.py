import streamlit as st

st.title("🎈 Previsão de Ações 🪙💹")
st.write(
    "Ferramenta para calcular o valor de ações"
)

# Lista de opções
opcoes = ["aapl"]

# Criando o combobox
escolha = st.selectbox("Empresa:", opcoes)

volume = st.number_input("Volume:", step=0.01)

prev_fecham = st.number_input("Previsão de Fechamento:", step=0.01)


