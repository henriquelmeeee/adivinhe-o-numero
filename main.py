import random

gerado = random.randint(1, 1000000)
while True:
    valor = int(input('Chute o valor: '))
    if valor == gerado:
        print("Ganhou!")
        gerado = random.randint(1, 1000000)
    else:
        if valor - gerado >= -1000 and not valor - gerado > 0:
            if valor - gerado >= -50:
                print("Pouquíssimo mais pra cima")
            else:
                print("Um pouco mais pra cima")
        elif valor - gerado >= 1 and not valor - gerado > 1000:
            if valor - gerado <= 50:
                print("Pouquíssimo mais pra baixo")
            else:
                print("Um pouco mais pra baixo")
        else:
            print("Mais pra baixo") if valor > gerado else print("Mais pra cima") 