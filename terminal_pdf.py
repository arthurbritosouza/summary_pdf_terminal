import time
from pytimedinput import timedInput
import os
from read_pdf import pdf_main
def _receive_input():
    command = input(">>> ")
    return command

def main():
    os.system("cls" if os.name == "nt" else "clear")

    while True:
        #caminho para salvar o resumo
        path_doc = "/home/arthur/Documentos"
        #llista todos os items desta pasta
        list_doc = os.listdir(path_doc)
        #caminho para os arquivos pdf
        path_pdf = "/home/arthur/Downloads/pdf"
        #caminho para a pasta onde ficaram os resumos salvos
        path_summary = path_doc + "/resumos_pdf"
        list_summary = os.listdir(path_summary)
        PDFs = os.listdir(path_pdf)

        if "resumos_pdf" not in list_doc:
                os.mkdir(f"{path_doc}/resumos_pdf")
        for numero, pdf in enumerate(PDFs):
            print(f"A{numero} - {pdf}")

        print(100 * "-")
        print("Comandos: quit - Sair|clear - Limpar historico|DH - Deletar tudo resumos|A - Escolher PDF|B - Escolher resumo")
        print("Pesquisas anteriores:")
        if list_summary != []:
            for i in range(len(list_summary)):
                print(f"B{i} - {list_summary[i]}")
        else:
            print("Sem resumos anteriores")
        inpt_pdf = input(">>> ")

        if inpt_pdf == "quit":
            break
        elif inpt_pdf == "DH":
            for item in list_summary:
                item_path = os.path.join(path_doc + "/resumos_pdf", item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
            print("Tudo limpo")
            
        elif inpt_pdf == "clear":
            os.system("cls" if os.name == "nt" else "clear")
            
        elif "A" in inpt_pdf  and int(inpt_pdf.split("A")[1]) < len(PDFs):
            pdf_selecionado = PDFs[int(inpt_pdf.split("A")[1])]
            print(f"Você escolheu: {pdf_selecionado}")
            pr = input("O que deseja extrair do PDF:")

            response = pdf_main(pr, f"{path_pdf}/{pdf_selecionado}")
            time.sleep(4)
            print(f"{response}\n\n")

            with open(f"{path_doc}/resumos_pdf/{pr}.txt", "w") as file:
                file.write(f"Pergunta:{pr}\nResposta:{response}")
            print(f"Resumo salvo em: {path_doc}/resumos_pdf/{pr}.txt")
        
        elif "B" in inpt_pdf and int(inpt_pdf.split("B")[1]) < len(os.listdir(f"{path_doc}/resumos_pdf")):
            pdf_selecionado = os.listdir(f"{path_doc}/resumos_pdf")[int(inpt_pdf.split("B")[1])]
            print(f"Voce escolheu: {pdf_selecionado}")

            with open(path_doc + "/resumos_pdf/" + pdf_selecionado , "r") as file:
                print(file.read())
            time.sleep(4)
       
        else:
            print("Erro: entrada inválida. Tente novamente.")

if __name__ == "__main__":
    main()