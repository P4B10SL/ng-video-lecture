import re
import json

# Abre el archivo de texto
with open('Reglamentacion.txt', 'r') as file:
    content = file.read()

# Divide el contenido del archivo en bloques separados por líneas en blanco
blocks = re.split(r'\n\s*\n', content)

# Inicializa una lista vacía para almacenar los diccionarios resultantes
result = []

# Itera a través de los bloques
for block in blocks:
    # Inicializa un diccionario vacío para almacenar cada entrada
    entry = {}
    # Divide cada bloque en líneas separadas
    lines = block.split('\n')
    # Itera a través de cada línea y extrae la clave y el valor
    for line in lines:
        key_value = re.match(r'([^:]+):(.+)', line)
        if key_value:
            key = key_value.group(1).strip()
            value = key_value.group(2).strip()
            entry[key] = value
    result.append(entry)

# Escribe el resultado en un archivo JSON
with open('Reglamentacion.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)
