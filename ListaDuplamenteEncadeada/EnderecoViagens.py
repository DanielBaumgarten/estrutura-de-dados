'''
Monte um algoritmo de lista duplamente encadeada de endereços a serem visitados em uma viagem.
A ordem de inserção será por ordem de chegada.
O Menu deve ter as seguintes opções:
	1) Adicionar na Lista
	2) Remover da Lista
	3) Imprimir em ordem
	4) Imprimir em ordem reversa

'''

class No:
    def __init__(self, endereco):
        self.endereco = endereco
        self.anterior = None
        self.proximo = None


class ListaDupla:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, endereco):
        novo = No(endereco)

        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            novo.anterior = self.fim
            self.fim = novo

        print("Endereço adicionado!")

    def remover(self, endereco):

        atual = self.inicio

        while atual:

            if atual.endereco == endereco:

                if atual.anterior:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo

                if atual.proximo:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior

                print("Endereço removido!")
                return

            atual = atual.proximo

        print("Endereço não encontrado!")

    def imprimir_ordem(self):

        if self.inicio is None:
            print("Lista vazia!")
            return

        atual = self.inicio

        print("\nRoteiro da viagem:")

        while atual:
            print(atual.endereco)
            atual = atual.proximo

    def imprimir_reversa(self):

        if self.fim is None:
            print("Lista vazia!")
            return

        atual = self.fim

        print("\nRoteiro em ordem reversa:")

        while atual:
            print(atual.endereco)
            atual = atual.anterior


lista = ListaDupla()

while True:

    print("\n===== MENU =====")
    print("1 - Adicionar na Lista")
    print("2 - Remover da Lista")
    print("3 - Imprimir em Ordem")
    print("4 - Imprimir em Ordem Reversa")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":

        endereco = input("Digite o endereço: ")
        lista.adicionar(endereco)

    elif opcao == "2":

        endereco = input("Digite o endereço para remover: ")
        lista.remover(endereco)

    elif opcao == "3":

        lista.imprimir_ordem()

    elif opcao == "4":

        lista.imprimir_reversa()

    elif opcao == "0":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida!")