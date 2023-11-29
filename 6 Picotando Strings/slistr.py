#Indexamento []
frase = "Matheus o bom"
#            [começo:fim:espaçamento]
primeira_parte = frase[0:7]
segunda_parte = frase[8:]
frase_picotada = frase[::2]
frase_reversa = frase[::-1]

#print(primeira_parte)
#print(segunda_parte)
#print(frase_picotada)
#print(frase_reversa)


#Slice()
website1 = "http://google.com"
website2 = "http://facebook.com"

slice = slice(7,-4)
print(website1[slice])
print(website2[slice])