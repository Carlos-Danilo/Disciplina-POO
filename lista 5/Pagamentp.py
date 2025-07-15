from datetime import datetime, date

class Boleto:
    def __init__(self, codigo_barras: str, emissao: str, vencimento: str, valor: float):
        self.__codigo_barras = codigo_barras
        self.__data_emissao = datetime.strptime(emissao, "%d-%m-%Y").date()
        self.__data_vencimento = datetime.strptime(vencimento, "%d-%m-%Y").date()
        self.__valor = valor
        self.__valor_pago = 0.0

    def get_codigo_barras(self) -> str:
        return self.__codigo_barras

    def get_data_emissao(self) -> date:
        return self.__data_emissao

    def get_data_vencimento(self) -> date:
        return self.__data_vencimento

    def get_valor(self) -> float:
        return self.__valor

    def get_valor_pago(self) -> float:
        return self.__valor_pago

    def set_valor(self, valor: float):
        self.__valor = valor

    def pagar(self, quantia: float):
        if quantia <= 0:
            print("Valor inválido.")
            return
        if self.__valor_pago + quantia > self.__valor:
            print("Pagamento excede o valor do boleto.")
            return
        self.__valor_pago += quantia
        print("Pagamento realizado com sucesso!")

    def situacao(self) -> str:
        if self.__valor_pago == 0:
            return "Em Aberto"
        elif self.__valor_pago < self.__valor:
            return "Pago Pacial"
        else:
            return "Pago"

    def to_string(self) -> str:
        emi = self.__data_emissao.strftime("%d/%m/%Y")
        ven = self.__data_vencimento.strftime("%d/%m/%Y")
        return (
            f"Código de Barras : {self.__codigo_barras}\n"
            f"Emissão          : {emi}\n"
            f"Vencimento       : {ven}\n"
            f"Valor            : R$ {self.__valor:.2f}\n"
            f"Valor Pago       : R$ {self.__valor_pago:.2f}\n"
            f"Situação         : {self.situacao()}"
        )

    def __str__(self) -> str:
        return self.to_string()


def cadastrar_boleto() -> Boleto:
    print("\nCadastro de Boleto ")
    codigo = input("Código de barras: ")
    emissao = input("Data de emissão (dia-mês-ano): ")
    venc = input("Data de vencimento (dia-mês-ano): ")
    valor = float(input("Valor (use ponto como separador): "))
    return Boleto(codigo, emissao, venc, valor)


def mostrar_boleto(boleto: Boleto):
    print("\n=== Dados do Boleto ===")
    print(boleto)


def efetuar_pagamento(boleto: Boleto):
    print("\n=== Pagar Boleto ===")
    restante = boleto.get_valor() - boleto.get_valor_pago()
    print(f"Valor a pagar até R$ {restante:.2f}")
    quantia = float(input("informe a quantia: "))
    boleto.pagar(quantia)


def menu():
    boleto = None
    while True:
        print("Menu")
        print("1 - Cadastrar boleto")
        print("2 - Mostrar boleto")
        print("3 - Pagar boleto")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            boleto = cadastrar_boleto()
        elif opcao == "2":
            if boleto:
                mostrar_boleto(boleto)
            else:
                print("\nNenhum boleto cadastrado.\n")
        elif opcao == "3":
            if boleto:
                efetuar_pagamento(boleto)
            else:
                print("\nNenhum boleto cadastrado.\n")
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
