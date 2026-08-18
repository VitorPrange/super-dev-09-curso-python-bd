from funcionario import menu_funcionario
from pratos_feitos import menu_pratos_feitos
from clientes import menu_clientes
from bebidas import menu_bebidas
from mesas import menu_mesas
from comandas import menu_comanda
import os


def __main():
    os.system("clear")
    mensagem = """MENU:
1 - Funcionarios
2 - Pratos feitos
3 - Clientes
4 - Bebidas
5 - Mesas
6 - Comandas
10 - Sair

Digite a opção desejada: """

    opcao = int(input(mensagem))

    while opcao != 10:

        os.system("clear")

        if opcao == 1:
            menu_funcionario()
        elif opcao == 2:
            menu_pratos_feitos()
        elif opcao == 3:
            menu_clientes()
        elif opcao == 4:
            menu_bebidas()
        elif opcao == 5:
            menu_mesas()
        elif opcao == 6:
            menu_comanda()
        elif opcao != 10:

            print("Opção invalida")

        print("\n")

        opcao = int(input(mensagem))

    os.system("clear")

if __name__ == "__main__":
    __main()



#