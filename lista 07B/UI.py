# ui.py
from View import View

def menu():
    print("\n=== Menu ===")
    print("1. Inserir Contato")
    print("2. Listar Contatos")
    print("3. Buscar por ID")
    print("4. Atualizar Contato")
    print("5. Excluir Contato")
    print("6. Pesquisar por iniciais")
    print("7. Aniversariantes do mês")
    print("8. Abrir contatos do arquivo")
    print("9. Salvar contatos no arquivo")
    print("0. Sair")

def main():
    v = View()
    caminho = "contatos.json"

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            nascimento = input("Data de nascimento (dd/mm/aaaa): ")
            v.inserir(nome, email, telefone, nascimento)

        elif opcao == "2":
            for c in v.listar():
                print("\n" + str(c))

        elif opcao == "3":
            id = int(input("ID do contato: "))
            c = v.buscar_por_id(id)
            print(c if c else "Contato não encontrado.")

        elif opcao == "4":
            id = int(input("ID do contato a atualizar: "))
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            telefone = input("Novo telefone: ")
            nascimento = input("Nova data de nascimento (dd/mm/aaaa): ")
            if v.atualizar(id, nome, email, telefone, nascimento):
                print("Contato atualizado.")
            else:
                print("Contato não encontrado.")

        elif opcao == "5":
            id = int(input("ID do contato a remover: "))
            v.excluir(id)
            print("Contato removido.")

        elif opcao == "6":
            iniciais = input("Digite as iniciais: ")
            resultados = v.pesquisar_iniciais(iniciais)
            for c in resultados:
                print("\n" + str(c))

        elif opcao == "7":
            mes = int(input("Digite o mês (1-12): "))
            aniversariantes = v.aniversariantes_mes(mes)
            for c in aniversariantes:
                print("\n" + str(c))

        elif opcao == "8":
            v.abrir(caminho)
            print("Contatos carregados.")
            for c in v.listar():
                print("" + str(c))

        elif opcao == "9":
            v.salvar(caminho)
            print("Contatos salvos.")

        elif opcao == "0":
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
