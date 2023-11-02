import re
import json
import csv

# Read the contents of the regulation file
with open('Reglamentacion_sin_tildes.txt', 'r') as f:
    regulation_text = f.read()

# Parse the regulation text into a dictionary
regulation_dict = {}
pattern = r"Documento: (\d+)\nArticulo: (\d+)\nCapitulo: (.+?)\n\n(.+?)(?=\n\nDocumento: |\Z)"
matches = re.findall(pattern, regulation_text, re.DOTALL)
for match in matches:
    id = match[1]  # Use the 'Articulo' column as the ID
    title = match[2].strip()
    context = match[3].strip()
    regulation_dict[id] = {
        "title": title,
        "context": context
    }

# Read the contents of the question-answer file
with open('Consultas_formateadas.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    qa_list = list(reader)

# Print the first few items of qa_list
print(qa_list[:5])

# Print the first few items of regulation_dict
print(list(regulation_dict.items())[:5])

# Combine the datasets
data = []
for qa in qa_list:
    id = qa[' idRespuestaEsperada(idArticulo) '].strip()  # Include spaces in the key
    print(f"Checking ID: {id}")  # Print the ID being checked
    if id in regulation_dict:
        print(f"Found ID: {id}")  # Print the ID if it was found
        data.append({
            "id": id,
            "title": regulation_dict[id]['title'],
            "context": regulation_dict[id]['context'],
            "question": qa[' Consulta'].strip(),  # Include spaces in the key
            "answers": {
                "text": [regulation_dict[id]['context']],
                "answer_start": [1]
            }
        })

# Write the JSON data to a file
with open('output.json', 'w') as f:
    json.dump(data, f, indent=4)