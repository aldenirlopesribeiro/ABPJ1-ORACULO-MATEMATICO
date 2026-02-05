
renda_mensal=float(input("digite o valor da renda mensal"))
despesa_medicamentos=float(input("digite o valor das despesas com medicamentos"))
despesa_de_aluguel=float(input("digite o valor do aluguel"))
renda_variavel=float(input("digite o valor da renda extra"))

calculo=renda_mensal-despesa_medicamentos-despesa_de_aluguel+renda_variavel

print(f"calculo despesas mensal{calculo}")
#esse programa ajuda o usuario a ter um controle financeiro sobre renda e despesas.
#o calculo final deve traser o resultado financeiro do mes, se positivo ou negativo.
