cadena = 'Geringoso'
capadepenapa = ''
vocales = "aeiou"

for c in cadena: 
    for vocal in vocales:
        if c == vocal:
            c = c.replace(vocal, vocal + 'p' + vocal)
    capadepenapa = capadepenapa + c
    print(c, end='')