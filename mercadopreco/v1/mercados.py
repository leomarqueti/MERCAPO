from playwright.sync_api import sync_playwright
from rich import print
import os
from rich.panel import Panel
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from datetime import datetime, timezone

MERCADOS = {
    "gaspar" : {
        'cebola' : '/2207/cebola-media-0500g-aprox-3-unid',
        'coca-cola': '/10035/refr-coca-cola-pet-2lt-tradicional',
        'molho de tomate': '/298/molho-tom-val-300g-sachet-trad-trad',
        'Arroz 1kg' : '/7253/arroz-pateko-1kg-lft1-parbol'
    },
    "amigao" : {
        'cebola' : '/cebola-kg-437/p',
        'coca-cola': '/refrigerante-coca-cola-pet-2l-4992/p',
        'molho de tomate': '/molho-de-tomate-tradicional-pomodoro-300g-6001776/p',
        'Arroz 1kg' : '/arroz-parboilizado-longo-fino-tipo-1-prato-fino-pacote-1kg-11476/p'
    }
}

precos = {
    "gaspar":{

    },
    "amigao":{

    }
}

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

# ESSA FUNÇÃO CRIA A TABELA DE PREÇO DOS MERCADOS , TEMOS UM LOOP PRINCIPAL QUE DENTRO DELE TEMOS A FUNÇAO QUE FAZ AS BUSCA DOS SITE PARA CADA MERCADO
def criar_tabela_de_preco(tabela_preco, nome_mercado1, nome_mercado2,mercado1,mercado2):

    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        for produto in mercado1:


            tabela_preco[nome_mercado1][produto] = float(buscar_produto_online(mercado1[produto],nome_mercado1,page).replace("R$", "")
                .replace(".", "")
                .replace(",", ".")
                .strip())
            
            tabela_preco[nome_mercado2][produto] = float(buscar_produto_online(mercado2[produto],nome_mercado2,page).replace("R$", "")
                .replace(".", "")
                .replace(",", ".")
                .strip())
        browser.close()

# PARA DEIXAR REGISTRADO OS DADOS DOS ERROS EM UM ARQUIVO SEPARADO FIZ ESSA FUNÇAO DE LOGS
def logs(erro):
    try: 
        with open('logs.txt', 'a') as arquivo_de_logs:
            arquivo_de_logs.readlines(f"[{datetime.now(timezone)}] | LOG: {erro}")
    except Exception as error:
        print(f"ERROR: {error}")

# CRIEI ESSA FUNÇÃO PARA CRIAR UMA LISTA DA COMPRA DE CADA MERCADO PARA O USUARIO COMPARAR
def listar_tabela_de_preco():
    limpar()

    for mercado, produtos in precos.items():
        console = Console()

        table = Table(title=f"preços {mercado}")
        table.add_column("Mercado", style="cyan", no_wrap=True)
        table.add_column("Produto", style="magenta")
        table.add_column("Preço", style="green", justify="right")
        preco_total = 0
        print(f"Mercado: {mercado}")

        for produto, preco in produtos.items():
            preco_total += preco
            table.add_row(
                mercado,
                produto,
                f"[bold green]R$ {preco:.2f}[/]"
            )
        console.print(table)
        
        print(f"Preço total da compra: R${preco_total}")
    
    pausar()
    limpar()

def somar_total_lista(lista):

    total = 0

    for item in lista:
        total += item
    
    return total

def menor_preco(precos, nome_mercado1, nome_mercado2):
    console = Console()

    table = Table(title="Menor preço por produto")
    table.add_column("Mercado", style="cyan", no_wrap=True)
    table.add_column("Produto", style="magenta")
    table.add_column("Preço", style="green", justify="right")

    produtos_comuns = (
        precos[nome_mercado1].keys()
        & precos[nome_mercado2].keys()
    )
    valor_total_menor_preco = 0

    for produto in produtos_comuns:
        preco1 = precos[nome_mercado1][produto]
        preco2 = precos[nome_mercado2][produto]

        if preco1 < preco2:
            table.add_row(
                nome_mercado1,
                produto,
                f"[bold green]R$ {preco1:.2f}[/]"
            )
            valor_total_menor_preco += preco1
        else:
            table.add_row(
                nome_mercado2,
                produto,
                f"[bold green]R$ {preco2:.2f}[/]"
            )
            valor_total_menor_preco += preco2


    console.print(table)
    print(f'[green]Valor total menor preço: {valor_total_menor_preco:.2f}[/green]')

    print(f"Valor total do mercado Gaspar: {somar_total_lista(precos["gaspar"].values())}")
    print(f"Valor total do mercado Amigão: {somar_total_lista(precos["amigao"].values())}")

def mostrar_menu():
    print(Panel("[1] Lista de compras economica \n""[2] Lista de cada mercado \n""[3] Sair", title="MERCADOS", style="green"))

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    print("""
[bright_green]
 ███╗   ███╗███████╗██████╗  ██████╗ █████╗ ██████╗  ██████╗ 
 ████╗ ████║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗
 ██╔████╔██║█████╗  ██████╔╝██║     ███████║██████╔╝██║   ██║
 ██║╚██╔╝██║██╔══╝  ██╔══██╗██║     ██╔══██║██╔═══╝ ██║   ██║
 ██║ ╚═╝ ██║███████╗██║  ██║╚██████╗██║  ██║██║     ╚██████╔╝
 ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝      ╚═════╝ 
[/bright_green]
[bold bright_white]MercadoPreço[/bold bright_white]
[dim]Comparador de preços de supermercados • Python + Playwright + Rich[/dim]
""")
    
def pausar():
    print("\n[bright_yellow]Pressione Enter para voltar ao menu...[/bright_yellow]")
    input()
    limpar()

def pegar_valor(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Digite um valor inteiro... ")

def main():
    banner()
    print("[bold bright_green]Inicializando MercadoPreço...[/]\n")
    try:
        criar_tabela_de_preco(precos,"gaspar","amigao",MERCADOS["gaspar"],MERCADOS["amigao"])
        limpar()
        
        while True:
            banner()
            mostrar_menu()
            op = pegar_valor("Digite a opção da sua escolha?")
            if op == 1:
                limpar()
                menor_preco(precos,"gaspar","amigao")
                pausar()
                limpar()
            elif op == 2:
                listar_tabela_de_preco()
            elif op == 3:
                break
            else:
                print("Digite um valor valido!!!")
    except Exception as error:
        print(f"O sistema teve algum erro de carregamento!! erro: {error}")

if __name__ == "__main__":
    main()






