import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente da OpenAI utilizando a chave da variável de ambiente
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def responder(pergunta: str, contexto: str) -> str:
    """Envia uma pergunta sobre a história do mercado financeiro e um contexto

    para a API da OpenAI e retorna apenas o texto da resposta.
    """
    prompt_sistema = (
        "Você é um agente educacional especializado na história do mercado financeiro. "
        "Utilize o contexto fornecido para responder às perguntas do usuário de forma clara e educativa."
    )

    prompt_usuario = (
        f"Contexto:\n{contexto}\n\n"
        f"Pergunta:\n{pergunta}"
    )

    try:
        # Chamada usando o endpoint da Responses API (client.responses.create)
        response = client.responses.create(
            model="gpt-4o",
            instructions=prompt_sistema,
            input=prompt_usuario,
        )
        return response.output_text

    except Exception as e:
        return f"Erro ao comunicar com a API da OpenAI: {e}"
