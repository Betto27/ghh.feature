inventario = []

cont = 0

while cont <= 3:

    inventario.append(str(input("Digite seu nome: ")))
    inventario.append(int(input("Digite sua idade: ")))

    cont += 1

print(inventario)
print(inventario[1])
print(inventario[0])
print(inventario[2])
