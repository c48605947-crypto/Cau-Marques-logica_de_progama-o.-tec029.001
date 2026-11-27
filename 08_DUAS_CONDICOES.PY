# entrada dados
massa = float(input("informe sua massa muscular: ").replace(",","."))
altura = float(input("informe a altura: ").replace(",","."))

if massa <= 140 and altura >= 1.15:
    print(f"entrada do usuario permitida.")
else:
    print(f"entrada do usuario negada")
