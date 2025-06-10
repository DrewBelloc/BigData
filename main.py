from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich import pretty
from convert import toNumber
from ml import train
from time import time

pretty.install()
["Rich and pretty", True]
console = Console()

def main():
    run = True
    option = ""
    console.print(Panel("[bold blue]Bem vindo!", title="[bold color(13)]Big Data", style="magenta"))
    while run:
        if option == "1":
            subMenu = True
            while subMenu:
                error = False
                entrada1 = Prompt.ask("qual o nome da rua")
                entrada2 = Prompt.ask("qual o numero")
                entrada3 = Prompt.ask("qual o lote")
                entrada4 = Prompt.ask("qual a quadra")
                try:
                    entrada1 = float(toNumber(entrada1))
                except:
                    error = True
                    console.log("Nome da rua não encontrado no banco de dados")
                try:
                    entrada2 = float(entrada2)
                    entrada3 = float(entrada3)
                    entrada4 = entrada4.replace("a","1")
                    entrada4 = entrada4.replace("b","2")
                    entrada4 = entrada4.replace("c","3")
                    entrada4 = entrada4.replace("d","4")
                    entrada4 = entrada4.replace("e","5")
                    entrada4 = entrada4.replace("f","6")
                    entrada4 = float(entrada4)
                except:
                    error = True
                    console.log("[bold red]Por favor insira um numero válido")
                if not error:
                    with console.status("Calculando...", spinner="aesthetic"):
                        start = time()
                        valor, precisao = train(2,entrada1,entrada2,entrada3,entrada4)
                        end = time()
                        console.print(Panel(f"[bold blue]Tempo de execução: {(end-start)*10**3:.03}ms\nPrecisão de {precisao*100}%", style="magenta", title="[red]Desempenho"))
                        valor = str(valor)
                        valor = valor.replace("[","")
                        valor = valor.replace("]","")
                        valor = valor.replace(" ","")
                        console.print(Panel(f"[blue]R${valor},00", title="[red]Valor da Taxa", style="magenta"))
                        subMenu = False

        elif option == "2":
            with console.status("Calculando...", spinner="aesthetic"):
                start = time()
                precisao = train(1)
                end = time()
                console.print(Panel(f"[blue]Tempo de execução: {(end-start)*10**3:.03}ms\n{precisao*100}%", title="[red]Desempenho", style="magenta"))
        elif option == "3":
            with console.status("Calculando...", spinner="aesthetic"):
                precisao = train(3)
        elif option == "4":
            run == False
            break
        console.rule("[bold blue]Menu Principal", style="magenta")
        console.print(Panel("[bold cyan]1[/]: [color(12)]Checar Taxa de entrega[/]\n[bold cyan]2[/]: [color(12)]Mostrar Desempenho[/]\n[bold cyan]3[/]: [color(12)]Mostrar Arvore de Decisão\n[bold cyan]4[/]: [color(12)]Sair", border_style="magenta"))
        option = Prompt.ask("menu")

if __name__=="__main__":
    main()
