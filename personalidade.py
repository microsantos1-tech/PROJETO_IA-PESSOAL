import requests

def dar_personalidade(pergunta, texto):
    prompt = f"""Você é uma IA pessoal simpática, direta e animada chamada NYA.
Com base no texto abaixo, responda a pergunta de forma clara e com personalidade.
Seja resumido, use no máximo 5 frases. Responda sempre em português.

Pergunta: {pergunta}

Texto encontrado: {texto}"""

    try:
        resposta = requests.post("http://localhost:11434/api/generate", json={
            "model": "qwen2.5:1.5b",
            "prompt": prompt,
            "stream": False
        })

        dados = resposta.json()
        return dados.get("response", "Não consegui gerar uma resposta.")

    except Exception as e:
        return f"Erro ao conectar com o Ollama: {e}"