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
    """Carrega os arquivos da pasta data e cria um contexto textual."""

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")

    contextos = []

    # 1. Histórico de atendimento
    csv_atendimento = os.path.join(data_dir, "historico_atendimento.csv")

    if os.path.exists(csv_atendimento):
        df_atendimento = pd.read_csv(csv_atendimento)

        contextos.append(
            "--- Histórico de Perguntas e Temas ---\n"
            + df_atendimento.to_string(index=False)
        )

    # 2. Perfil educacional
    json_perfil = os.path.join(data_dir, "perfil_investidor.json")

    if os.path.exists(json_perfil):
        with open(json_perfil, "r", encoding="utf-8") as f:
            dados_perfil = json.load(f)

        contextos.append(
            "--- Perfil Educacional ---\n"
            + json.dumps(
                dados_perfil,
                ensure_ascii=False,
                indent=2
            )
        )

    # 3. Produtos e conceitos financeiros
    json_produtos = os.path.join(data_dir, "produtos_financeiros.json")

    if os.path.exists(json_produtos):
        with open(json_produtos, "r", encoding="utf-8") as f:
            dados_produtos = json.load(f)

        contextos.append(
            "--- Conceitos e Instrumentos Financeiros ---\n"
            + json.dumps(
                dados_produtos,
                ensure_ascii=False,
                indent=2
            )
        )

    # 4. Dados históricos ilustrativos
    csv_transacoes = os.path.join(data_dir, "transacoes.csv")

    if os.path.exists(csv_transacoes):
        df_transacoes = pd.read_csv(csv_transacoes)

        contextos.append(
            "--- Dados Históricos Ilustrativos ---\n"
            + df_transacoes.to_string(index=False)
        )

    return "\n\n".join(contextos)


# --------------------------------------------------
# Interface
# --------------------------------------------------

st.title("🏛️ Agente IA - História do Mercado Financeiro")

st.write(
    "Bem-vindo! Este agente educacional ajuda a compreender "
    "a história do mercado financeiro, crises econômicas, "
    "bolsas de valores, inflação, juros e outros acontecimentos "
    "que influenciaram a economia mundial."
)

st.divider()

st.subheader("💡 Sugestões de perguntas")

st.markdown("""
- **O que foi a crise de 1929?**
- **Quais foram as causas da crise financeira de 2008?**
- **Como surgiu a bolsa de valores?**
- **Qual é a relação entre inflação e juros?**
- **O que aconteceu durante a Black Monday de 1987?**
- **Como uma crise financeira pode afetar a população?**
- **O que é uma ação?**
- **O que são commodities?**
""")

st.divider()

# Carrega os dados
contexto_dados = carregar_dados()

# Campo de pergunta
pergunta = st.text_input(
    "Faça sua pergunta sobre a história do mercado financeiro:"
)

if st.button("Enviar Pergunta", type="primary"):

    if pergunta.strip():

        with st.spinner("O agente está pensando..."):

            try:
                resposta = responder(
                    pergunta=pergunta,
                    contexto=contexto_dados
                )

                st.markdown("### 🤖 Resposta do Agente:")
                st.write(resposta)

            except Exception as e:

                st.error(
                    "Ocorreu um erro ao comunicar com a API do Gemini."
                )

                st.caption(f"Detalhes técnicos: {e}")

    else:
        st.warning(
            "Por favor, digite uma pergunta antes de enviar."
        )