idade = int(input("Qual a sua idade?"))

if idade >= 18:
    print("Você é adulto")
elif idade < 0:
    print("Você ainda não nasceu")
else:
    print("Você é menor de idade")