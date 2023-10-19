import unicodedata
import re

# Abre el archivo de texto con manejo de errores
with open('Reglamentacion.txt', 'r', encoding='latin-1', errors='ignore') as file:
    content = file.read()

# Elimina los caracteres con tilde y la letra "ñ"
normalized_content = unicodedata.normalize('NFKD', content).encode('ASCII', 'ignore').decode('utf-8')
normalized_content = re.sub(r'[^\w\s]', '', normalized_content)

# Escribe el contenido normalizado en un nuevo archivo
with open('Reglamentacion_sin_tildes.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(normalized_content)
