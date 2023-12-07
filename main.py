from Pessoa import Pessoa, Tutor, Funcionario
from Animal import Animal, Pet
from Agenda import Horario

def cadastrarTutor():
    while True:
        print("-" * 59)
        print('-' * 20 + "CADASTRO TUTORES" + '-' * 23)
        print("-" * 59)
        print("\n1- Cadastrar Tutor\n2- Pesquisar Tutores\n3- Listar Tutores\n4- Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            def salvarDados(tutores):
                with open('tutor.txt', 'a') as arquivo:
                    for tutor in tutores:
                        arquivo.write(f"dados do tutor {tutor.nome}\n")
                        arquivo.write(f"Nome: {tutor.nome}\n")
                        arquivo.write(f"Email: {tutor.email}\n")
                        arquivo.write(f"Telefone: {tutor.telefone}\n")
                        arquivo.write(f"Nome do pet: {tutor.petNome}\n")
                        arquivo.write(f"-------------------------\n")
                print("Sucesso! Tutor salvo com sucesso")

            listaTutores = []
            print("-" * 60)
            print('-' * 23 + "CADASTRO DE TUTOR" + '-' * 20)
            print("-" * 60 )
            nome = input("Digite o nome da pessoa: ")
            email = input("Digite o email da pessoa: ")
            telefone = int(input("Digite o telefone da pessoa: "))
            petNome = input("Digite o nome do pet da pessoa: ")
            tutor = Tutor(nome, email, telefone, petNome)
            listaTutores = [tutor]
            salvarDados(listaTutores)
            pass

        elif escolha == "2":
            def pesquisarTutor(tutores):
                with open("tutor.txt", "r") as arquivo:
                    conteudo = arquivo.read()
                    if f"dados do tutor {tutor}" in conteudo:
                        print("-------------------------")
                        inicio = conteudo.find(f"dados do tutor {tutor}")
                        fim = conteudo.find("-------------------------", inicio)
                        if inicio != -1 and fim != -1:
                            dados = conteudo[inicio:fim + len("-------------------------")]
                            print("Dados do Pet:\n")
                            print(dados)
                        else:
                            print(f"Tutor com nome '{tutor}' não encontrada.")
                    else:
                        print(f"Tutor com nome '{tutor}' não encontrada.")
            pass
            tutor = input("Digite o nome do tutor que deseja pesquisar: ")
            pesquisarTutor(tutor)
            pass

        elif escolha == "3":
            def listaFunc():
                with open("tutor.txt", "r") as arquivo:
                    conteudo = arquivo.read()
                    print("-------------------------")
                    print(conteudo)

            pass
            listaFunc()

        elif escolha == "4":
            principal()


def cadastrarPet():
    while True:
        print("-" * 59)
        print('-' * 25 + "CADASTRO PET" + '-' * 22)
        print("-" * 59)
        print("\n1- Cadastrar Pets\n2- Pesquisar Pets\n3- Listar Pets\n4- Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            def salvarDados(pets):
                with open('Animal.txt', 'a') as arquivo:
                    for pet in pets:
                        arquivo.write(f"Dados do Pet: {pet.nome}\n")
                        arquivo.write(f"Nome: {pet.nome}\n")
                        arquivo.write(f"Nome do Dono: {pet.nomeDono}\n")
                        arquivo.write(f"Raça: {pet.raça}\n")
                        arquivo.write(f"Idade: {pet.idade}\n")
                        arquivo.write(f"Precisa de vacina?: {pet.vacina}\n")
                        arquivo.write(f"Peso: {pet.peso}\n")
                        arquivo.write(f"-------------------------\n")
                print("Sucesso! Pet salvo com sucesso")

            listaAnimais = []
            print("-" * 60)
            print('-' * 23 + "CADASTRAR PET" + '-' * 24)
            print("-" * 60)
            nome = input("Digite o nome do pet: ")
            nomeDono = input("Digite o nome do dono: ")
            raça = input("Digite a raça do seu pet: ")
            idade = int(input("Digite a idade do seu pet: "))
            vacina = input("Precisa de vacina? S/N: ")
            peso = float(input("Digite o peso do seu pet: "))
            pet = Pet(nome, nomeDono, raça, idade, vacina, peso)
            listaAnimais = [pet]
            salvarDados(listaAnimais)
            pass

        elif escolha == "2":
            def pesquisarPet(pets):
                with open("Animal.txt", "r") as arquivo:
                    conteudo = arquivo.read()
                    if f"Dados do Pet: {nomePet}" in conteudo:
                        print("-------------------------")
                        inicio = conteudo.find(f"Dados do Pet: {nomePet}")
                        fim = conteudo.find("-------------------------", inicio)
                        if inicio != -1 and fim != -1:
                            dados = conteudo[inicio:fim + len("-------------------------")]
                            print("Dados do Pet:\n")
                            print(dados)
                        else:
                            print(f"Pet com nome '{nomePet}' não encontrada.")
                    else:
                        print(f"Pet com nome '{nomePet}' não encontrada.")
            pass
            nomePet = input("Digite o nome do pet que deseja pesquisar: ")
            pesquisarPet(nomePet)

        elif escolha == "3":
            def listaPet():
                with open("Animal.txt", "r") as arquivo:
                    conteudo = arquivo.read()
                    print("-------------------------")
                    print(conteudo)
            pass
            listaPet()

        elif escolha == "4":
            principal()


def cadastrarFuncionario():
    while True:
        print("-" * 59)
        print('-' * 20 + "CADASTRO FUNCIONÁRIOS" + '-' * 18)
        print("-" * 59)
        print("\n1- Cadastrar Funcionarios\n2- Pesquisar Funcionarios\n3- Listar Funcionarios\n4- Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            def salvarDados(funcionarios):
                with open('funcionarios.txt', 'a') as arquivo:
                    for func in funcionarios:
                        arquivo.write(f"Dados do funcionario {func.nome}\n")
                        arquivo.write(f"Nome: {func.nome}\n")
                        arquivo.write(f"Email: {func.email}\n")
                        arquivo.write(f"Telefone: {func.telefone}\n")
                        arquivo.write(f"Cargo: {func.cargo}\n")
                        arquivo.write(f"-------------------------\n")
                print("Sucesso! Funcionário salvo com sucesso")

            listaFunc = []
            print("-" * 60)
            print('-' * 19 + "CADASTRO FUNCIONÁRIOS" + '-' * 20)
            print("-" * 60)
            nome = input("Digite o nome do Funcionario: ")
            email = input("Digite o email do Funcionario: ")
            telefone = int(input("Digite o telefone do Funcionario: "))
            cargo = input("Digite o cargo do Funcionario: ")
            func = Funcionario(nome, email, telefone, cargo)
            listaFunc = [func]
            salvarDados(listaFunc)
            pass

        elif escolha == "2":
            def pesquisarFunc(func):
                with open("funcionarios.txt", "r") as arquivo:
                    conteudo = arquivo.read()
                    if f"Dados do funcionario {nomeFunc}" in conteudo:
                        print("-------------------------")
                        inicio = conteudo.find(f"Dados do funcionario {nomeFunc}")
                        fim = conteudo.find("-------------------------", inicio)
                        if inicio != -1 and fim != -1:
                            dados = conteudo[inicio:fim + len("-------------------------")]
                            print("Dados do funcionario:\n")
                            print(dados)
                        else:
                            print(f"Funcionario com nome '{nomeFunc}' não encontrada.")
                    else:
                        print(f"Funcionario com nome '{nomeFunc}' não encontrada.")
            pass
            nomeFunc = input("Digite o nome do pet que deseja pesquisar: ")
            pesquisarFunc(nomeFunc)

        elif escolha == "3":
            def listaFunc():
                with open("funcionarios.txt", "r") as arquivo:
                    conteudo = arquivo.read()
                    print("-------------------------")
                    print(conteudo)
            pass
            listaFunc()

        elif escolha == "4":
           principal()

def agenda():
    while True:
        print("-" * 59)
        print('-' * 20 + "AGENDA DE HORÁRIOS" + '-' * 21)
        print("-" * 59)
        print("\n1- Listar Horários\n2- Marcar Horário\n3- Voltar")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            def listaAgenda():
                with open("Agenda.txt", "r") as arquivo:
                    conteudo = arquivo.read()
                    print("-------------------------")
                    print(conteudo)
            pass
            listaAgenda()

        elif escolha == "2":
            def salvarDados(horarios):
                with open('Agenda.txt', 'a') as arquivo:
                    for hora in horarios:
                        arquivo.write(f"Nome: {hora.nome}\n")
                        arquivo.write(f"Horario: {hora.horario}\n")
                        arquivo.write(f"Serviço: {hora.servico}\n")
                        arquivo.write(f"-------------------------\n")
                print("Sucesso! Horario salvo com sucesso")

            listaHorario = []
            print("-" * 60)
            print('-' * 23 + "MARCAR HORÁRIO" + '-' * 23)
            print("-" * 60)
            nome = input("Digite o nome do Cliente: ")
            horario = input("Digite o horario do cliente: ")
            servico = input("Digite o servico que o cliente deseja: ")
            hora = Horario(nome, horario, servico)
            listaHorario = [hora]
            salvarDados(listaHorario)
            pass

        elif escolha == "3":
            principal()


def principal():

    while True:
        print("-" * 59)
        print('-' * 23 + "Menu Principal" + '-' * 22)
        print("-" * 59)
        print("\nSeja bem-vindo!\n1-Tutor                     ░░░░╔═══╗░░░░░░║░░\n2-Pet                       ░░▄═╝█║░║══════╣░░\n3-Funcionarios              ░░║═░░╚═╝░░░░░░║░░\n4-Agenda de serviços        ░░╚═════╗╗╔══╗╗║░░\n5-Sair                      ░░░░░░░░╚╚╝░░╚╚╝░░")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrarTutor()

        elif escolha == "2":
            cadastrarPet()

        elif escolha == "3":
            cadastrarFuncionario()

        elif escolha == "4":
            agenda()

        elif escolha == "5":
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    principal()



