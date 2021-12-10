

texto = "brasil, argentina, russia, hungria, alemanha"
texto = texto.replace(" ","")
texto = texto.replace(",","")

consoantes = 0
vogais = 0

for letra in texto:
    if letra in 'aeiou':
        vogais = vogais + 1
    else:
        consoantes = consoantes + 1


#print("Vogais: %s \nConsoantes: %s" % (vogais,consoantes))
#print("Total de letras: %s" % len(texto))

print("Vogais: {} \nConsoantes: {} \nTotal de letras: {}".format(vogais, consoantes, len(texto)))

#print("""
#Vogais: {} \n
#Consoantes: {} \n
#Total de letras: {} \n
#""".format(vogais, consoantes, len(texto)))





        
        
