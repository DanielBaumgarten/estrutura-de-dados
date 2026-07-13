'''
Construa um software em Python que implemente uma Pilha de carros e uma Pilha de drones.
As classes carro e drone herdam da classe veículo os atributos e comuns às duas classes.
A classe carro é composta dos atributos marca, modelo e portas. O atributo portas é fracamente privado.
A classe drone é composta dos atributos marca, modelo e quantidade de hélices. O atributo quantidade de hélices é fortemente privado.
Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.
Implemente uma tela com um menu (funcionando) que permita ao usuário:
-> Adicionar e remover carros da Pilha.
-> Adicionar e remover drones da Pilha.
-> Imprimir a Pilha de carros e a Pilha de drones.
'''

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprimir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")


class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas

    def imprimir(self):
        print("\n--- CARRO ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Portas: {self._portas}")


class Drone(Veiculo):
    def __init__(self, marca, modelo, helices):
        super().__init__(marca, modelo)
        self.__helices = helices

    def imprimir(self):
        print("\n--- DRONE ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Hélices: {self.__helices}")


class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        return None

    def vazia(self):
        return len(self.itens) == 0

    def imprimir(self):
        if self.vazia():
            print("Pilha vazia!")
            return

        print("\n=== TOPO DA PILHA ===")

        for item in reversed(self.itens):
            item.imprimir()


pilha_carros = Pilha()
pilha_drones = Pilha()

while True:

    print("\n===== MENU =====")
    print("1 - Adicionar Carro")
    print("2 - Remover Carro")
    print("3 - Adicionar Drone")
    print("4 - Remover Drone")
    print("5 - Imprimir Pilha de Carros")
    print("6 - Imprimir Pilha de Drones")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        portas = int(input("Quantidade de portas: "))

        carro = Carro(marca, modelo, portas)

        pilha_carros.empilhar(carro)

        print("Carro adicionado com sucesso!")

    elif opcao == "2":

        carro = pilha_carros.desempilhar()

        if carro:
            print("Carro removido!")
        else:
            print("Pilha de carros vazia!")

    elif opcao == "3":

        marca = input("Marca: ")
        modelo = input("Modelo: ")
        helices = int(input("Quantidade de hélices: "))

        drone = Drone(marca, modelo, helices)

        pilha_drones.empilhar(drone)

        print("Drone adicionado com sucesso!")

    elif opcao == "4":

        drone = pilha_drones.desempilhar()

        if drone:
            print("Drone removido!")
        else:
            print("Pilha de drones vazia!")

    elif opcao == "5":

        pilha_carros.imprimir()

    elif opcao == "6":

        pilha_drones.imprimir()

    elif opcao == "0":

        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")