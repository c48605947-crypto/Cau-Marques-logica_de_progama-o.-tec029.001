#  TODO: Crie um progama que receba do usuario o valor da gasolina 
# e do entanol, e informe para o usuario o melhor valor do combustivel
# para abastecer
# NOTE: compensa mais abstecer com etanol caso o  valo do entanol  
# corresponde a ate 75% do valor da gasolina 
# NOTE: e não se esqueça do detalhe mais importante de todos:


gasolina = float(input("Digite o valor da gasolina: ").replace(",","."))
etanol = float(input("Digite o valor do etanol: ").replace(",","."))

if etanol <= gasolina * 0.75:
    print("Compensa abastecer com etanol!")
else:
    print("Compensa abastecer com gasolina!")
