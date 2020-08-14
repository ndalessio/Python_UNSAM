frase = 'todes somos programadores'
palabras = frase.split()
index1 = -1
index2 = -2
frase_t = ''
    
for palabra in palabras:
    if len(palabra) >= 2:
        if palabra[index1] == 'o':
            palabra = palabra[:index1] + 'e' 
            pass
        elif palabra[index2] == 'o' :
            palabra = palabra[:index2] + 'e' + palabra[index2+1:]  
        else:
            pass
    frase_t += palabra + ' '
    
print(frase_t)
