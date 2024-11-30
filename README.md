# PDF Summarizer via Terminal

### Descrição
O **PDF Summarizer via Terminal** é um sistema interativo que utiliza inteligência artificial para resumir arquivos PDF diretamente pela linha de comando. Ele permite que o usuário:
- Selecione PDFs para resumir.
- Salve resumos gerados.
- Consulte resumos criados anteriormente.

Este sistema foi projetado para maximizar a eficiência e simplicidade no tratamento de documentos PDF.

---

## **Funcionalidades**
1. Listagem de arquivos PDF disponíveis.
2. Geração de resumos baseados em entradas personalizadas do usuário.
3. Organização automática dos resumos em uma pasta dedicada.
4. Acesso rápido aos resumos já gerados.
5. Comandos interativos, como limpar histórico e excluir resumos.

---

## **Pré-requisitos**
- **Python 3.7+**
- Biblioteca `pytimedinput`
- Módulo de leitura de PDFs chamado `read_pdf` (implemente o `pdf_main` para extração do conteúdo).

---

## **Como Usar**
### **1. Executar o Programa**
No terminal, execute o programa com:
```bash
python <nome_do_arquivo>.py
