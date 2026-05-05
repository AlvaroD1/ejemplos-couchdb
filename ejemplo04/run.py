import requests
import json

# Cargar datos desde archivo
with open('datos.json', 'r') as f:
    # pasar los datos a estructuras de Python
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    if d['nombre'][0] in ["A", "B", "L"]:
        lista_datos.append(d)

base_datos = "personas004"
# Configurar el acceso a la base de datos
url = f"http://127.0.0.1:5985/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar datos

for doc in lista_datos:
    response = requests.post(
        url,
        json=doc
    )
    print(f"Insertando {doc['nombre']} | {response.status_code}")

# Dentro del ejemplo 3 estamos subiendo los archivos uno por uno lo cual es mas lento,
# mientras que en el ejemplo 4 subimos un solo paquete con todos los datos lo cual es mas eficiente
