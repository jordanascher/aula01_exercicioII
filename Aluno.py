class Aluno:
    
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula=matricula
    
    def imprimir(self):
        print("Nome:", self.nome)
        print("Matricula:", self.matricula)
    
