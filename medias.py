class media():

    def nota(self):

        self.n = int(input("Digite nota: "))
        return self.n

    def res_media(self, notas, cont):

        self.result = notas / cont
        return self.result

""" n1 = int(input("Digite nota: "))
n2 = int(input("Digite nota: "))
n3 = int(input("Digite nota: "))
n4 = int(input("Digite nota: ")) """

# res_media = (n1 + n2 + n3 + n4) / 4
"""cont = 0
notas = 0
while cont < 4:

    res = media()
    notas = notas + res.nota()
    cont += 1

print(res.res_media(notas))"""