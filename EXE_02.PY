# TODO: Crie um programa que receba do usuario o nome, a massa 
# ea altura, calcule seu IMC (indice de massa coporal).
# Apos mostra o IMV, o programa deve informa de acordo com o 
# valor do seu IMC:
# - IMC < 18.5: "usuario esta abaixo do peso ideal"
# - IMC < 25: "usuario esta peso ideal"
# - IMC < 30: "usuario esta acima do peso "
# - IMC < 35: "usuario esta obeso"
# - IMC < 40: "usuario esta com obecida nivel 2"
# - Se não estive em nenhum dos casos acima: 
# - "Usuario esta com obesidade morbida "


# entrada de dados

nome = input("Digite seu nome: ")

massa = float(input("Digite sua massa em kg: ").replace(",","."))
altura = float(input("Digite sua altura em metros: ").replace(",","."))

# saida de dados

imc = massa / (altura ** 2)

print("IMC de " + nome + ": " + str(round(imc, 2)))

if imc < 18.5:
    print(nome + " está abaixo do peso ideal")

elif imc < 25:
    print(nome + " está no peso ideal")

elif imc < 30:
    print(nome + " está acima do peso")

elif imc < 35:
    print(nome + " está obeso")

elif imc < 40:
    print(nome + " está com obesidade nível 2")

else:
    print(nome + " está com obesidade mórbida")
