from ddgs import DDGS

def buscar(pergunta):
    with DDGS() as ddgs:

        res = ddgs.text(pergunta, region='pt-br', max_results=3)
        resultados = list(res)
        
        print(f"DEBUG: Encontrei {len(resultados)} resultados") 
        return resultados