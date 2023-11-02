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
    id = f"{match[0]}-{match[1]}"
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

# Combine the datasets
data = []
for qa in qa_list:
    id = qa['idRespuestaEsperada(idArticulo)'].strip()   # Assuming 'idArticulo' is the third column
    if id in regulation_dict:
        data.append({
            "id": id,
            "title": regulation_dict[id]['title'],
            "context": regulation_dict[id]['context'],
            "question": qa['Consulta'].strip(),  # Assuming 'Question' is the second column
            "answers": {
                "text": [regulation_dict[id]['context']],
                "answer_start": [1]
            }
        })

# Convert the data to JSON
json_data = json.dumps(data, indent=4)

# Write the JSON data to a file
with open('DatasetCombinado.json', 'w') as f:
    f.write(json_data)