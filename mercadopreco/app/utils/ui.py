from rich import print
import os
from rich.panel import Panel
from datetime import datetime, timezone

# PARA DEIXAR REGISTRADO OS DADOS DOS ERROS EM UM ARQUIVO SEPARADO FIZ ESSA FUNÇAO DE LOGS
def logs(erro):
    try: 
        with open('logs.txt', 'a') as arquivo_de_logs:
            arquivo_de_logs.readlines(f"[{datetime.now(timezone)}] | LOG: {erro}")
    except Exception as error:
        print(f"ERROR: {error}")


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
