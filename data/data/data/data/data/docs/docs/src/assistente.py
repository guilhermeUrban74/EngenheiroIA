
import os
from pathlib import Path
from google import genai

# Configuração da inteligência artificial
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "Configure a variável de ambiente GEMINI_API_KEY."
    )

client = genai.Client(api_key=API_KEY)

MODELO = "gemini-3.8-flash"

# Localização da base de conhecimento
PASTA_PROJETO = Path(__file__).resolve()

while not (PASTA_PROJETO / "README.md").exists():
    PASTA_PROJETO = PASTA_PROJETO.parent

PASTA_DATA = PASTA_PROJETO / "data"

# Carregamento dos arquivos de conhecimento
def carregar_base():
    conhecimento = ""

    for arquivo in PASTA_DATA.glob("**/*.md"):
        conteudo = arquivo.read_text(encoding="utf-8")
        conhecimento += f"\n\n{conteudo}"

    return conhecimento


# Instruções do assistente
INSTRUCOES = """
Você é o EngenheiroIA, um assistente virtual de Engenharia Civil.

Seu objetivo é ajudar estudantes e iniciantes a compreender
conceitos da Engenharia Civil.

Regras:
- Responda em português do Brasil.
- Utilize linguagem simples e didática.
- Consulte a base de conhecimento fornecida.
- Não invente informações.
- Se a base não tiver informações suficientes,
  informe isso claramente.
- Apresente exemplos quando forem úteis.
- Não substitua a avaliação de profissionais habilitados.
"""


# Função para responder às perguntas
def responder(pergunta):
    base = carregar_base()

    prompt = f"""
    {INSTRUCOES}

    BASE DE CONHECIMENTO:
    {base}

    PERGUNTA DO USUÁRIO:
    {pergunta}

    Responda utilizando as informações disponíveis.
    """

    resposta = client.models.generate_content(
        model=MODELO,
        contents=prompt
    )

    return resposta.text


# Início da conversa
def iniciar_assistente():
    print("=" * 50)
    print("       ENGENHEIROIA - ASSISTENTE VIRTUAL")
    print("=" * 50)
    print("Olá! Como posso ajudar com Engenharia Civil?")
    print("Digite 'sair' para encerrar a conversa.")

    while True:
        pergunta = input("\nVocê: ")

        if pergunta.lower().strip() == "sair":
            print("EngenheiroIA: Até a próxima!")
            break

        if not pergunta.strip():
            print("Digite uma pergunta para continuar.")
            continue

        try:
            resposta = responder(pergunta)
            print("\nEngenheiroIA:", resposta)

        except Exception as erro:
            print("\nNão foi possível gerar a resposta.")
            print("Detalhes:", erro)


if __name__ == "__main__":
    iniciar_assistente()
