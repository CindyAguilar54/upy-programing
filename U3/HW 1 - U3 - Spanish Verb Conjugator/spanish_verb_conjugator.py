
# INPUT
# Solicitar al usuario un verbo regular en español que termine en -ar, -er o -ir.
verbo = input("Ingrese verbo: ").strip().lower()

# Estructuras de datos requeridas (adaptadas a español latinoamericano: excluyendo 'vosotros')
pronombres = ['yo', 'tu', 'el', 'nosotros', 'ustedes', 'ellos']
terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'an', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'en', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'en', 'en']
}

# PROCESS
# Obtener la raíz (el verbo sin las últimas 2 letras) y el sufijo (las últimas 2 letras)
raiz = verbo[:-2]
sufijo = verbo[-2:]

# Buscar la lista de terminaciones correspondiente en el diccionario
lista_terminaciones = terminaciones[sufijo]

# OUTPUT
# Iterar a través de los pronombres e imprimir cada conjugación correspondiente usando concordancia de índices
for i in range(len(pronombres)):
    conjugacion = raiz + lista_terminaciones[i]
    print(f"{pronombres[i]} {conjugacion}")