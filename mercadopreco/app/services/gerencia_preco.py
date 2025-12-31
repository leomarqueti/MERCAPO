from playwright.sync_api import sync_playwright
from rich import print
from rich.console import Console
from rich.table import Table

from app.scrapers.busca import buscar_produto_online
from app.utils.ui import *

precos = {
    "gaspar":{

    },
    "amigao":{

    }
}


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