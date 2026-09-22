import json
import os
import pandas as pd
import streamlit as st
from agente import responder

# Configuração da página
st.set_page_config(
    page_title="Agente IA - História do Mercado Financeiro",
    page_icon="📈",
    layout="centered"
)


def carregar_dados():
    """Carrega os arquivos da pasta ../data e os converte em um contexto textual simples."""
    # Define o caminho base relativo para a pasta data a partir da raiz do projeto
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")

    contextos = []

    # 1. historico_atendimento.csv
    csv_atendimento = os.path.join(data_dir, "historico_atendimento.csv")
    if os.path.exists(csv_atendimento):
        df_atendimento = pd.read_csv(csv_atendimento)
        contextos.append("--- Histórico de Atendimento ---\n" + df_atendimento.to_string(index=False))

    # 2. perfil_investidor.json
    json_perfil = os.path.join(data_dir, "perfil_investidor.json")
    if os.path.exists(json_perfil):
        with open(json_perfil, "r", encoding="utf-8") as f:
            dados_perfil = json.load(f)
            contextos.append("--- Perfil do Investidor ---\n" + json.dumps(dados_perfil, ensure_ascii=False, indent=2))

    # 3. produtos_financeiros.json
    json_produtos = os.path.join(data_dir, "produtos_financeiros.json")
    if os.path.exists(json_produtos):
        with open(json_produtos, "r", encoding="utf-8") as f:
            dados_produtos = json.load(f)
            contextos.append("--- Produtos Financeiros ---\n" + json.dumps(dados_produtos, ensure_ascii=False, indent=2))

    # 4. transacoes.csv
    csv_transacoes = os.path.join(data_dir, "transacoes.csv")
    if os.path.exists(csv_transacoes):
        df_transacoes = pd.read_csv(csv_transacoes)
        contextos.append("--- Transações ---\n" + df_transacoes.to_string(index=False))

    # Junta todo o contexto formatado
    return "\n\n".join(contextos)


# --- Interface Streamlit ---

st.title("🏛️ Agente IA - História do Mercado Financeiro")
st.write(
    "Bem-vindo! Este agente educacional tira dúvidas sobre a história do mercado financeiro "
    "e analisa dados de perfil, transações, produtos e atendimentos."
)

st.divider()

# Exemplos de perguntas
st.subheader("💡 Sugestões de Perguntas")
st.markdown("""
- *Como surgiram as primeiras Bolsas de Valores no mundo?*
- *Qual é a história do crash da bolsa em 1929?*
- *Com base no perfil do investidor e nas transações nos arquivos, qual é o resumo do comportamento financeiro?*
- *Como evoluíram os produtos financeiros ao longo da história até os descritos no arquivo?*
""")

st.divider()

# Carrega os dados de contexto da pasta data
contexto_dados = carregar_dados()

# Campo de entrada de texto
pergunta = st.text_input("Faça sua pergunta sobre a história do mercado ou sobre os dados:")

if st.button("Enviar Pergunta", type="primary"):
    if pergunta.strip():
        with st.spinner("O agente está consultando o contexto e gerando a resposta..."):
            resposta = responder(pergunta=pergunta, contexto=contexto_dados)
            st.markdown("### 🤖 Resposta do Agente:")
            st.write(resposta)
    else:
        st.warning("Por favor, digite uma pergunta antes de enviar.")