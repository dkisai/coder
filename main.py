import json



# Cargar los datos de ambos archivos JSON
with open('movie_ids_09_28_2023.json', 'r') as file1, open('movie_ids_09_29_2023.json', 'r') as file2:
    data1 = [json.loads(line) for line in file1]
    data2 = [json.loads(line) for line in file2]

# Extraer los valores de 'id' de cada objeto y convertirlos en conjuntos
ids1 = set(item['id'] for item in data1)
ids2 = set(item['id'] for item in data2)

# Encontrar los elementos que se eliminaron (en data1 pero no en data2)
deleted_items = [item for item in data1 if item['id'] not in ids2]

# Encontrar los elementos que se agregaron (en data2 pero no en data1)
added_items = [item for item in data2 if item['id'] not in ids1]

# Guardar los elementos eliminados en 'deleted_items.json'
with open('deleted_items.json', 'w', encoding='utf-8') as deleted_file:
    for item in deleted_items:
        json.dump(item, deleted_file, ensure_ascii=False)
        deleted_file.write('\n')

# Guardar los elementos agregados en 'added_items.json'
with open('added_items.json', 'w', encoding='utf-8') as added_file:
    for item in added_items:
        json.dump(item, added_file, ensure_ascii=False)
        added_file.write('\n')

print("Archivos 'deleted_items.json' y 'added_items.json' creados con éxito.")

