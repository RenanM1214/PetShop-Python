class Agenda:
    def __init__(self, nome, horario, servico):
        self.nome = nome
        self.horario = horario
        self.servico = servico

class Horario(Agenda):
    def __init__(self, nome, horario,servico):
        super().__init__(nome, horario,servico)
