from buscador import buscar
from extrator import ler_site

def executar_agente():

    while True:
        print("\n" + "="*30)
        pergunta = input("Digite sua pergunta (ou 'sair' para encerrar): ")

        if pergunta.lower() == 'sair':
            print("Encerrando o agente... Até logo!")
            break 

        print("Buscando...")
        links = buscar(pergunta)

        if links:
            for i, l in enumerate(links):
                print(f"{i}: {l['title']}")

            primeiro_link = links[0]['href']
            print(f"Lendo: {primeiro_link}")

            conteudo = ler_site(primeiro_link) 
            
            print("\nRESPOSTA: ")
            print(conteudo)
        else: 
            print("Não achei algo relacionado")

executar_agente()