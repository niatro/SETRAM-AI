def read_file_and_convert_to_list_with_overlap(file_path, chunk_size, overlap):
    with open(file_path, 'r') as file:
        text = file.read()

    # Crear una lista para almacenar los segmentos de texto
    chunks = []
    start = 0
    end = chunk_size

    while end <= len(text):
        # Reemplazar saltos de línea con espacios
        chunk = text[start:end].replace('\n', ' ')
        chunks.append(chunk)
        start += chunk_size - overlap
        end = start + chunk_size

    return chunks

def save_list_to_file(data, output_file_path):
    with open(output_file_path, 'w') as file:
        file.write("data = [\n")
        for sentence in data:
            # Asegurarse de que las comillas se manejen correctamente
            sentence = sentence.replace('"', '\\"')
            file.write(f'  "{sentence}",\n')
        file.write("]\n")

# Ruta del archivo .txt original
input_file_path = './data/manual_vial.txt'

# Ruta del nuevo archivo donde se guardará la lista
output_file_path = './data/manual_vial.py'

# Tamaño de cada segmento de texto (por ejemplo, 1000 caracteres)
chunk_size = 1000

# Solapamiento entre segmentos consecutivos (por ejemplo, 100 caracteres)
overlap = 200

# Leer el archivo original y convertirlo en una lista con solapamiento
data = read_file_and_convert_to_list_with_overlap(input_file_path, chunk_size, overlap)

# Guardar la lista en un nuevo archivo
save_list_to_file(data, output_file_path)
