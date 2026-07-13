'''
Cadastro de 10 alunos utilizando
Árvore Binária de Busca.

Atributos:
- Nome
- Matrícula
- Nota

Menu:
1 Pré-Ordem
2 Em-Ordem
3 Pós-Ordem
4 Ordem Reversa
5 Buscar aluno
0 Sair

'''
class No:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
        self.esq = None
        self.dir = None


# Inserir aluno na árvore
def inserir(raiz, nome, matricula, nota):
    if raiz is None:
        return No(nome, matricula, nota)

    if matricula < raiz.matricula:
        raiz.esq = inserir(raiz.esq, nome, matricula, nota)
    elif matricula > raiz.matricula:
        raiz.dir = inserir(raiz.dir, nome, matricula, nota)

    return raiz


# Pré-Ordem
def pre_ordem(raiz):
    if raiz:
        print(f"Matrícula: {raiz.matricula} | Nome: {raiz.nome} | Nota: {raiz.nota}")
        pre_ordem(raiz.esq)
        pre_ordem(raiz.dir)


# Em Ordem
def em_ordem(raiz):
    if raiz:
        em_ordem(raiz.esq)
        print(f"Matrícula: {raiz.matricula} | Nome: {raiz.nome} | Nota: {raiz.nota}")
        em_ordem(raiz.dir)


# Pós-Ordem
def pos_ordem(raiz):
    if raiz:
        pos_ordem(raiz.esq)
        pos_ordem(raiz.dir)
        print(f"Matrícula: {raiz.matricula} | Nome: {raiz.nome} | Nota: {raiz.nota}")


# Ordem Reversa
def ordem_reversa(raiz):
    if raiz:
        ordem_reversa(raiz.dir)
        print(f"Matrícula: {raiz.matricula} | Nome: {raiz.nome} | Nota: {raiz.nota}")
        ordem_reversa(raiz.esq)


# Busca por matrícula
def buscar_matricula(raiz, matricula):
    if raiz is None:
        return None

    if matricula == raiz.matricula:
        return raiz

    if matricula < raiz.matricula:
        return buscar_matricula(raiz.esq, matricula)

    return buscar_matricula(raiz.dir, matricula)


# Busca por nome
def buscar_nome(raiz, nome):
    if raiz is None:
        return None

    if raiz.nome.lower() == nome.lower():
        return raiz

    encontrado = buscar_nome(raiz.esq, nome)
    if encontrado:
        return encontrado

    return buscar_nome(raiz.dir, nome)


# Programa principal
raiz = None

print("Cadastro de 10 alunos")

for i in range(10):
    print(f"\nAluno {i+1}")
    nome = input("Nome: ")
    matricula = int(input("Matrícula: "))
    nota = float(input("Nota: "))

    raiz = inserir(raiz, nome, matricula, nota)


while True:
    print("\n--- MENU ---")
    print("1 - Imprimir Pré-Ordem")
    print("2 - Imprimir Em Ordem")
    print("3 - Imprimir Pós-Ordem")
    print("4 - Imprimir Ordem Reversa")
    print("5 - Procurar Aluno")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        pre_ordem(raiz)

    elif opcao == 2:
        em_ordem(raiz)

    elif opcao == 3:
        pos_ordem(raiz)

    elif opcao == 4:
        ordem_reversa(raiz)

    elif opcao == 5:
        tipo = input("Buscar por (N)ome ou (M)atrícula? ").upper()

        if tipo == "M":
            mat = int(input("Digite a matrícula: "))
            aluno = buscar_matricula(raiz, mat)

        else:
            nome = input("Digite o nome: ")
            aluno = buscar_nome(raiz, nome)

        if aluno:
            print("\nAluno encontrado!")
            print("Nome:", aluno.nome)
            print("Matrícula:", aluno.matricula)
            print("Nota:", aluno.nota)
        else:
            print("Aluno não encontrado.")

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")