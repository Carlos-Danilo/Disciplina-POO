import random
class Contato:
    def __init__(self, i, n, e, f):
        self.__id = i
        self.__nome = n
        self.__email = e
        self.__fone = f
    def get_id(self):
        return self.__id    
    def get_nome(self):
        return self.__nome  
    def get_email(self):
        return self.__email  
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"
        
class ContatoUI:
    __contatos = []

    @classmethod
    def main(cls):
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()
            if op == 2: ContatoUI.listar()
            if op == 3: ContatoUI.atualizar()
            if op == 4: ContatoUI.excluir()
            if op == 5: ContatoUI.pesquisar()

    @classmethod
    def menu(cls):
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Fim")
        return int(input("Informe uma opção: "))
    
    @classmethod
    def inserir(cls):
        id = cls.id_unico()
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        c = Contato(id, nome, email, fone)
        cls.__contatos.append(c)

    def id_unico(cls):
        while True:
            novo_id = random.randint(1000, 9999)
            if cls.listar_id(novo_id):
                return novo_id


    @classmethod
    def listar(cls):
        if len(cls.__contatos) == 0:
            print("Nenhum contato cadastrado")
        for c in cls.__contatos:
            print(c)

    @classmethod
    def listar_id(cls, id):
        for c in cls.__contatos:
            if c.get_id() == id: return c
        return None    

    @classmethod
    def atualizar(cls):
        cls.listar()
        id = int(input("Informe o id do contato a ser atualizado: "))
        c = cls.listar_id(id)
        if c == None: print("Esse contato não existe")
        else:
            nome = input("Informe o novo nome: ")
            email = input("Informe o novo e-mail: ")
            fone = input("Informe o novo fone: ")
            cls.__contatos.remove(c)
            c = Contato(id, nome, email, fone)
            cls.__contatos.append(c)

    @classmethod
    def excluir(cls):
        cls.listar()
        id = int(input("Informe o id do contato a ser excluído: "))
        c = cls.listar_id(id)
        if c == None: print("Esse contato não existe")
        else: cls.__contatos.remove(c)

    @classmethod
    def pesquisar(cls):
        nome = input("Informe o nome do contato: ")
        for c in cls.__contatos:
            if c.get_nome().startswith(nome):
                print(c)

ContatoUI.main()

import json
import os

class Cliente:
    """Classe para representar um cliente com id, nome, email e telefone"""
    
    def __init__(self, id, nome, email, fone):
        """Construtor da classe Cliente
        
        Args:
            id (int): Identificador único do cliente
            nome (str): Nome do cliente
            email (str): Email do cliente
            fone (str): Telefone do cliente
        """
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
    
    # Métodos de acesso (getters)
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def get_fone(self):
        return self.__fone
    
    # Métodos modificadores (setters)
    def set_id(self, id):
        self.__id = id
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_email(self, email):
        self.__email = email
    
    def set_fone(self, fone):
        self.__fone = fone
    
    def toString(self):
        """Retorna uma string com os dados do cliente formatados"""
        return f"ID: {self.__id} | Nome: {self.__nome} | Email: {self.__email} | Telefone: {self.__fone}"
    
    def to_dict(self):
        """Converte o cliente para dicionário (para salvar em arquivo)"""
        return {
            'id': self.__id,
            'nome': self.__nome,
            'email': self.__email,
            'fone': self.__fone
        }
    
    @classmethod
    def from_dict(cls, data):
        """Cria um cliente a partir de um dicionário"""
        return cls(data['id'], data['nome'], data['email'], data['fone'])


class ClienteUI:
    """Classe de interface do usuário para gerenciar clientes"""
    
    def __init__(self):
        """Construtor que inicializa a lista de clientes"""
        self.clientes = []
    
    def main(self):
        """Método principal que executa o menu em loop"""
        print("=== SISTEMA DE CADASTRO DE CLIENTES ===\n")
        
        while True:
            opcao = self.menu()
            
            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.listar()
            elif opcao == '3':
                self.listar_id()
            elif opcao == '4':
                self.atualizar()
            elif opcao == '5':
                self.excluir()
            elif opcao == '6':
                self.abrir()
            elif opcao == '7':
                self.salvar()
            elif opcao == '8':
                print("Obrigado por usar o sistema! Até logo!")
                break
            else:
                print("Opção inválida! Tente novamente.\n")
    
    def menu(self):
        """Exibe o menu de opções e retorna a escolha do usuário"""
        print("\n" + "="*50)
        print("MENU PRINCIPAL")
        print("="*50)
        print("1 - Inserir novo cliente")
        print("2 - Listar todos os clientes")
        print("3 - Buscar cliente por ID")
        print("4 - Atualizar dados do cliente")
        print("5 - Excluir cliente")
        print("6 - Abrir lista de arquivo")
        print("7 - Salvar lista em arquivo")
        print("8 - Sair")
        print("="*50)
        return input("Escolha uma opção: ").strip()
    
    def inserir(self):
        """Solicita dados do usuário e insere um novo cliente na lista"""
        print("\n--- INSERIR NOVO CLIENTE ---")
        try:
            id = int(input("ID do cliente: "))
            
            # Verifica se o ID já existe
            if self.buscar_por_id(id):
                print(f"Erro: Já existe um cliente com ID {id}!")
                return
            
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            fone = input("Telefone: ").strip()
            
            if not nome or not email or not fone:
                print("Erro: Todos os campos são obrigatórios!")
                return
            
            cliente = Cliente(id, nome, email, fone)
            self.clientes.append(cliente)
            print(f"Cliente '{nome}' inserido com sucesso!")
            
        except ValueError:
            print("Erro: ID deve ser um número inteiro!")
    
    def listar(self):
        """Lista todos os clientes cadastrados"""
        print("\n--- LISTA DE CLIENTES ---")
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return
        
        print(f"Total de clientes: {len(self.clientes)}")
        print("-" * 80)
        for cliente in self.clientes:
            print(cliente.toString())
    
    def listar_id(self):
        """Lista os dados do cliente com um ID específico"""
        print("\n--- BUSCAR CLIENTE POR ID ---")
        try:
            id = int(input("Digite o ID do cliente: "))
            cliente = self.buscar_por_id(id)
            
            if cliente:
                print("\nCliente encontrado:")
                print("-" * 40)
                print(cliente.toString())
            else:
                print(f"Nenhum cliente encontrado com ID {id}")
                
        except ValueError:
            print("Erro: ID deve ser um número inteiro!")
    
    def atualizar(self):
        """Atualiza os dados de um cliente existente"""
        print("\n--- ATUALIZAR CLIENTE ---")
        try:
            id = int(input("Digite o ID do cliente a ser atualizado: "))
            cliente = self.buscar_por_id(id)
            
            if not cliente:
                print(f"Nenhum cliente encontrado com ID {id}")
                return
            
            print(f"\nDados atuais: {cliente.toString()}")
            print("\nDigite os novos dados (pressione Enter para manter o atual):")
            
            nome = input(f"Nome [{cliente.get_nome()}]: ").strip()
            email = input(f"Email [{cliente.get_email()}]: ").strip()
            fone = input(f"Telefone [{cliente.get_fone()}]: ").strip()
            
            # Atualiza apenas os campos que foram preenchidos
            if nome:
                cliente.set_nome(nome)
            if email:
                cliente.set_email(email)
            if fone:
                cliente.set_fone(fone)
            
            print("Cliente atualizado com sucesso!")
            
        except ValueError:
            print("Erro: ID deve ser um número inteiro!")
    
    def excluir(self):
        """Remove um cliente da lista"""
        print("\n--- EXCLUIR CLIENTE ---")
        try:
            id = int(input("Digite o ID do cliente a ser excluído: "))
            cliente = self.buscar_por_id(id)
            
            if not cliente:
                print(f"Nenhum cliente encontrado com ID {id}")
                return
            
            print(f"\nCliente encontrado: {cliente.toString()}")
            confirmacao = input("Tem certeza que deseja excluir? (s/n): ").lower()
            
            if confirmacao == 's':
                self.clientes.remove(cliente)
                print("Cliente excluído com sucesso!")
            else:
                print("Operação cancelada.")
                
        except ValueError:
            print("Erro: ID deve ser um número inteiro!")
    
    def abrir(self):
        """Lê a lista de clientes de um arquivo JSON"""
        print("\n--- ABRIR ARQUIVO ---")
        nome_arquivo = input("Digite o nome do arquivo (com .json): ").strip()
        
        if not nome_arquivo.endswith('.json'):
            nome_arquivo += '.json'
        
        try:
            if not os.path.exists(nome_arquivo):
                print(f"Arquivo '{nome_arquivo}' não encontrado!")
                return
            
            with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
                
            self.clientes.clear()
            for cliente_data in dados:
                cliente = Cliente.from_dict(cliente_data)
                self.clientes.append(cliente)
            
            print(f"Lista de clientes carregada com sucesso! ({len(self.clientes)} clientes)")
            
        except json.JSONDecodeError:
            print("Erro: Arquivo com formato inválido!")
        except Exception as e:
            print(f"Erro ao abrir arquivo: {e}")
    
    def salvar(self):
        """Salva a lista de clientes em um arquivo JSON"""
        print("\n--- SALVAR ARQUIVO ---")
        if not self.clientes:
            print("Nenhum cliente para salvar!")
            return
        
        nome_arquivo = input("Digite o nome do arquivo (com .json): ").strip()
        
        if not nome_arquivo.endswith('.json'):
            nome_arquivo += '.json'
        
        try:
            dados = [cliente.to_dict() for cliente in self.clientes]
            
            with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=2)
            
            print(f"Lista de clientes salva com sucesso em '{nome_arquivo}'!")
            
        except Exception as e:
            print(f"Erro ao salvar arquivo: {e}")
    
    def buscar_por_id(self, id):
        """Busca um cliente pelo ID e retorna o objeto ou None"""
        for cliente in self.clientes:
            if cliente.get_id() == id:
                return cliente
        return None


# Execução do programa
if __name__ == "__main__":
    app = ClienteUI()
    app.main()