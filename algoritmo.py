#Autores: Justin Vega Madrigal (116550095)

marcadores=['A', 'B', 'C', 'D', "the shop"]
reglas = [ 'apple', 'bag', 'shop', "the", "my brother"]
cadenaDeEntrada = [ 'D', 'C' ]

print ( marcadores )
print ( reglas )

simboloTerminal = bool ( 0 )
auxiliar = 0

for a in cadenaDeEntrada:
    auxiliar = 0
    for b in marcadores:
        auxiliar = auxiliar + 1
        if a == b:
            print ( b )