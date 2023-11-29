temp = int(input("Qual a temperatura lá fora?"))

if temp >= 0 and temp <=30 :
    print("Temperatura ambiente")
    print("Vá sair")
elif not(temp < 0 or temp > 30):
    print("Temperatura extrema")
    print("Se possível, permaneça em casa")