class Animal:
    def __init__(self, nome, nomeDono, raça, idade, vacina, peso):
        self.nome = nome
        self.nomeDono = nomeDono
        self.raça = raça
        self.idade = idade
        self.vacina = vacina
        self.peso = peso

class Pet(Animal):
    def __init__(self, nome, nomeDono, raça, idade, vacina, peso):
        super().__init__(nome, nomeDono, raça, idade, vacina, peso)