idades = [1, 2, 3, 4, 7, 13, 15, 20, 35, 65, 72]

for idade in idades:
    print("A idade é: " + str(idade))
    if idade < 2:
        print("Você é um bebê!!\n")
    elif 2 <= idade < 4:
        print("Você é uma criança!!\n")
    elif 4 <= idade < 13:
        print("Você é um(a) garoto(a)!!\n")
    elif 13 <= idade < 20:
        print("Você é um adolescente!!\n")
    elif 20 <= idade < 65:
        print("Você é um(a) adulto(a)!!\n")
    else:
        print("Você é um(a) idoso(a)!!\n")


