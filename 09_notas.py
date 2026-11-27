# entrada de dados

nome = input("Digite o nome do aluno: ").strip().title()

nota1 = int(input("Digite a 1ª nota: "))
nota2 = int(input("Digite a 2ª nota: "))

# processamento de dados
media = (nota1 + nota2) / 2

print("Média: {media}")

if media >= 7:
    print(nome + " está aprovado")

elif media >= 5:
    print(nome + " está de recuperação")

else:
    print(nome + " está reprovado")
