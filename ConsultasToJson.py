import csv
import json

# Read the contents of the question-answer file
with open('Consultas_formateadas.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    qa_list = []
    for row in reader:
        # Strip whitespace from each field
        qa = {k: v.strip() for k, v in row.items()}
        qa_list.append(qa)

# Convert the list of dictionaries to JSON
json_data = json.dumps(qa_list, indent=4)

# Write the JSON data to a file
with open('Consultas.json', 'w') as f:
    f.write(json_data)