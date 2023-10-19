import json

# Abre el archivo de texto con la codificación adecuada
with open('Reglamentacion.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Procesa cada línea y crea un diccionario
data_list = []
current_data = {}
for line in lines:
    line = line.strip()
    if line:
        key, value = map(str.strip, line.split(': ', 1))
        current_data[key] = value
    else:
        data_list.append(current_data)
        current_data = {}

# Agrega el último diccionario a la lista
if current_data:
    data_list.append(current_data)

# Escribe la lista de diccionarios en un archivo JSON
with open('Reglamentacion.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)
