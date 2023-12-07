class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

class Tutor(Pessoa):
    def __init__(self, nome, email, telefone, petNome):
        super().__init__(nome, email, telefone)
        self.petNome = petNome

class Funcionario(Pessoa):
    def __init__(self, nome, email, telefone, cargo):
        super().__init__(nome, email, telefone)
        self.cargo = cargo





