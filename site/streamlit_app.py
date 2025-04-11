import streamlit as st
import requests

st.title("🎈 Previsão de Ações 🪙💹")
st.write(
    "Ferramenta para calcular o valor de ações"
)

# Lista de opções
opcoes = ["aapl"]

# Criando o combobox
empresa = st.selectbox("Empresa:", opcoes)

volume = st.number_input("Volume:", step=0.01)

prev_fecham = st.number_input("Previsão de Fechamento:", step=0.01)

# URL da API (exemplo usando uma API pública)
url = "https://aula-2010-62jk.onrender.com/previsoes"

# Parâmetros opcionais da requisição (se necessário)
payload = {
    "empresa": empresa,
    "volume": volume,
    "prev_fecham" : prev_fecham
}

if st.button("Fazer previsão"):
    # Fazendo a requisição GET
    response = requests.get(url, json=payload)

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        dados = response.json()
        st.success(f"Profecia: {dados['profecia']}")
    else:
        st.write(f"Erro na requisição: {response.status_code}")
        st.write(response.text)
