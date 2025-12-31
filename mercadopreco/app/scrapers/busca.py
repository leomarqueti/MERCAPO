from rich import print
from datetime import datetime, timezone
from app.services import gerencia_preco


# PARA DEIXAR REGISTRADO OS DADOS DOS ERROS EM UM ARQUIVO SEPARADO FIZ ESSA FUNÇAO DE LOGS
def logs(erro):
    try: 
        with open('logs.txt', 'a') as arquivo_de_logs:
            arquivo_de_logs.readlines(f"[{datetime.now(timezone)}] | LOG: {erro}")
    except Exception as error:
        print(f"ERROR: {error}")

# ESSA FUNÇÃO FICA RESPONSAVEL POR BUSCAR OS PRODUTOS NO SITE PELA URL E USANDO O NOME DO MERCADO PARA SABER O TIPO DE PESQUISA
def buscar_produto_online(url, mercado,page):

    if mercado == "gaspar":

        try:
            page.goto(f"https://www.varejaogaspar.com.br/produto{url}")
            preco = page.text_content('[data-cy="preco"]')
            return preco
        
        except Exception as error:
            logs(f"Houve um erro na busca dos dados do mercado {mercado}!")
            print(f"Houve um erro na busca dos dados do mercado {mercado}!")
        
    elif mercado == "amigao":
    
        try:
            
            page.goto(f"https://www.amigao.com/{url}")
            preco = page.text_content('.new-price-pdp')
            
            return preco
        except Exception as error:
                logs(f"Houve um erro na busca dos dados do mercado {mercado}!")
                print(f"Houve um erro na busca dos dados do mercado {mercado}!")
