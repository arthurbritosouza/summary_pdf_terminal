import google.generativeai as genai
import pypdf
import os
from dotenv import load_dotenv
load_dotenv()
pdf_text = []

def pdf_main(pergunta,caminho_pdf):

    leitor = pypdf.PdfReader(caminho_pdf)
    num_paginas = len(leitor.pages)
    print(num_paginas)

    genai.configure(api_key=os.environ['GENAI_API_KEY'])
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")

    for pages in range(num_paginas):
        page = leitor.pages[pages]
        text = page.extract_text()
        pdf_text.append(text)
    pergunta_mdelo = f"Você é um analisador de pdf proficional faça o que o usuário pedir. Pergunta:{pergunta} {pdf_text}"
    resposta = model.generate_content(pergunta_mdelo)
    return resposta.text
    #print(resposta.text)

