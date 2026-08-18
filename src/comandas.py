from bancos_dados import conectar
import os
from clientes import listar_clientes

from rich.console import Console
from rich.table import Table



def cadastrar():
    listar_clientes()


    id_cliente = int(input("Digite o id do cliente: "))


    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute(

        "ISERT INTO comandas (id_cliente) VALUES (%s)",

        (id_cliente,),
    )


    conexao.commit()


    comanda_id = cursor.lastrowid

    print(f"Comanda gerada: {comanda_id}")

    cursor.close()

    conexao.close()




def listar_comandas():
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(
        """SELECT cod.id,
        cli.nome
        FROM comandas AS cod
        INNER JOIN clientes AS cli ON (cod.id_cliente = cli.id)"""
    )

    comandas = cursor.fetchall()

    if len(comandas) == 0:
        print("Nenhuma comanda cadastrada")
        return

    tabela = Table("Id", "Cliente", show_header=True)
    tabela.title = (
        "[not italic]:vampire:[/] Comandas [not italic]:vampire:[/]"
    )

    for comanda in comandas:
        id, cliente = comanda
        tabela.add_row(str(id), cliente)

    console = Console()
    console.print(tabela)

    cursor.close()
    conexao.close()


def adicionar_prato_feito_comanda():
    listar_pratos()

    id_prato = int(input("Digite o id do prato feito: "))



def excluir_comanda():
    pass



def alterar_comanda():
    pass



def menu_comanda():


    mensagem = """MENU:

1 - Listar

2 - Cadastrar

3 - Editar

4 - Apagar

5 - Sair


Digite a opção desejada: """


    opcao = int(input(mensagem))


    while opcao != 5:

        os.system("clear")


        if opcao == 1:
            listar_comandas()

        elif opcao == 2:
            cadastrar_comandas()

        elif opcao == 3:
            alterar_comanda()

        elif opcao == 4:

            excluir_comanda()

        elif opcao != 5:

            print("Opção invalida")

        print("\n")


        opcao = int(input(mensagem))

    os.system("clear")