class bola():

    def __init__(self):

        self.cor = ""
        self.circunferencia = 0
        self.material = ""

    def troca_cor(self):

        self.cor = str(input("Digite uma cor: "))
        return self.cor

class quadrado():

    def __init__(self):

        self.tamanho = 10

    def mudar_valor(self):
        self.tamanho = int(input("Digite um novo valor: "))
        return self.tamanho
    def retomar_valor(self):
        self.tamanho = 10
        return self.tamanho

    def calc_area(self):
        self.tamanho = self.tamanho * self.tamanho
        return self.tamanho

class retangulo():

    def __init__(self):
        self.comprimento = 10
        self.largura = 20

    def mudar_lado(self):

        self.comprimento = int(input("Digite o valor da Altura do seu retangulo: "))
        self.largura = int(input("Digite o valor da Largura do ser Retangulo: "))

        return self.comprimento, self.largura

    def retornar_valor(self):
        self.comprimento = 10
        self.largura = 20

        return self.comprimento, self.largura

    def calc_area(self):

        res = self.comprimento * self.largura
        return res

    def calc_perimetro(self):

        res = (self.comprimento * 2) + (self.largura * 2)
        return res

"""ret = retangulo()
print(ret.largura)
print(ret.comprimento)
print(ret.mudar_lado())
#print(ret.retornar_valor())
print(ret.calc_area())
print(ret.calc_perimetro())"""

class pessoa():

    def __init__(self):

        self.nome = "Juliana"
        self.idade = 10
        self.peso = 45
        self.altura = 1.40

    def envelhecer(self):

        self.envelhecimento = int(input("Digite quantos anos ela envelheceu: "))
        if self.envelhecimento >= 0:
            self.idade_atual = self.envelhecimento + self.idade
            return self.idade_atual
        else:
            print("Valor invalido")

    def engordar(self):
        cont = 0
        self.peso_total = self.peso
        while cont < self.envelhecimento:

            self.peso_total = self.peso_total + 1.2
            cont += 1
        return self.peso_total

    def crescer(self):

        cont = 0
        self.altura_total = self.altura
        while cont < self.envelhecimento and cont < 11:

            self.altura_total = self.altura_total + 0.05
            cont += 1
        return self.altura_total


"""res = pessoa()
print(res.envelhecer())
print(res.engordar())
print(res.crescer())"""



