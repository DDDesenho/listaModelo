
def get_usuario():
    nome = input("Nome da primeira pessoa: ")
    salario = float(input("Salario da primeira pessoa: "))
    idade = int(input("Digite uma idade: "))
    sexo = input("Digite um sexo (F/M): ")
    return nome, salario, idade, sexo

def imprime_usuario(nome, salario, idade, sexo):
    print(f"Nome: {nome}")
    print(f"Salario: {salario:.2f}")
    print(f"Idade: {idade}")
    print(f"Sexo: {sexo}")

def verif_maior_idade(idade):
    if idade >= 18:
        print('maior')
    else:
        print('menor')


while True:
    opcao = input('para sair digite  s : ')

    if opcao == 's':
        break
    a,b,c,d = get_usuario()
    verif_maior_idade(c)
    # imprime_usuario(a,b,c,d)
