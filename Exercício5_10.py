usuarios_cadastrados = ["mauricio", "andre", "taciana", "rafael", "eduardo"]
novos_usuarios = ["ana", "antonio", "Filomena", "RAFAEL", "Eduardo"]

for usuario in novos_usuarios:
    print("Nome de usuário: " + usuario)
    if usuario.lower() in usuarios_cadastrados:
        print("O usuário: "+ usuario + " não está disponível, por favor escolha outro nome.\n" + "O sistema não diferencia letras mauiúsculas e minusculas (Andre = andre).\n")
    else:
        print("Nome de usuário disponível.\n")
