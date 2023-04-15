#teste 1: Igualdade e não igualdade com strings: 
fruta = "abacaxi"
print("A variável armazenada é:")
print(fruta)
print("\nResultado do teste para a confirmação da variável fruta (fruta == 'abacaxi'):")
print(fruta == 'abacaxi')
print("\nResultado do teste para a confirmação da variável fruta (fruta == 'banana'):")
print(fruta == 'banana')

#teste 2: Uso da função .lower():
carro = "Volvo"
print("\nA variável armazenada (carro) é:")
print(carro)
print("\nResultado do teste para a confirmação da variável carro com o uso do método .lower() (carro.lower() == 'volvo'):")
print(carro.lower() == 'volvo')
print("\nResultado do teste para a confirmação da variável carro com o uso do método .lower() (carro.lower() == 'parati'):")
print(carro.lower() == 'parati')      

#teste 3: Testes numéricos:
idade = 18
print("\nA variável armazenada (idade) é:")
print(idade)
print("\nA idade armazenada é 18 anos? (idade == 18)")
print(idade == 18)
print("\nA variável armazenada (idade) é maior que 18: (idade > 18)")
print(idade > 18)
print("\nA variável armazenada (idade) é menor ou igual a 18: (idade <= 18)")
print(idade <= 18)

#teste 4: Testes usando and e or:
carro1 = "volvo"
carro2 = "fiat"
carro3 = "ford"
print("\nAs variáveis armazenadas são: (carro1, carro2, carro3)")
print(carro1, carro2, carro3)
print("\nTeste 1: verificar se carro1 é volvo e carro2 é fiat: (carro1 == 'volvo and carro2 == 'fiat')")
print((carro1 == "volvo") and (carro2 == "fiat"))
print("\nTeste 2: verificar se carro1 ou carro2 é volvo: (carro1 == 'volvo' or carro2 == 'volvo')")
print((carro1 == 'volvo') or (carro2 == 'volvo'))
print("\nTeste 2: verificar se carro2 ou carro3 é bmw: (carro2 == 'bmw' or carro2 == 'bmw')")
print((carro2 == 'bmw') or (carro3 == 'bmw'))

# teste 5: Testes para verificar se um item está em uma lista:
países = ['brasil', 'honduras', 'argentina', 'paraguai', 'itália']
print("\nA lista de países gravados é:")
print(países)
print("\nTeste para verificar se 'chile' consta em [países]:")
print('chile' in países)
print("\nTeste para verificar se 'brasil' consta em [países]:")
print("brasil" in países)
