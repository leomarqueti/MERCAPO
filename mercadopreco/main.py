from rich import print
from app.utils.ui import *
from app.services.gerencia_preco import *

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

