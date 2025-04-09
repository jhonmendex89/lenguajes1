# origines de datos (disco)
# bases datos: relaciones (mysql, oracle, etc) / 
# no solo relacionales (mongo, redis, casandra, etc)
# objetos (memoria)
# archivos (xls, pdf, txt, csv, xml, json)

#diccionario python
import json
"""personas = {
 123:{
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Madrid",
    "casado": False
}}

print(personas[123]["edad"])
print(personas.items())

cedula = int(input("Ingrese su cedula: "))
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")

personas[cedula] = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad
}

for clave, valor in personas.items():
    print(clave, valor) 

"""
#lectura y escritura archivos 
#path: ruta donde se encuentra un recurso
#tipo path: 
# relativo ej. lenguajes1/jhonMendez/index.py
# absoluto ej. C:\Users\jhonm\OneDrive\Escritorio\lenguajes1\jhonMendez\estudiantes.json
estudiantes_txt_path="jhonMendez/estudiantes.txt"
estudiantes_json_path="jhonMendez/estudiantes.json"

#tipo operacion archivos:
# r: read
# a: append
# w: write
# x: create
# b: binary

#lectura de un archivo txt
with open(estudiantes_txt_path,"r") as estudiantes_txt:
    print(estudiantes_txt.read())


estudiantes = []
     
#lectura de un archivo json
with open(estudiantes_json_path,"r") as estudiantes_json:
    #desserizacion - json str-> dict
    estudiantes_dic = json.load(estudiantes_json)
    estudiantes.append(estudiantes_dic)
    print(type(estudiantes_dic))

print(type(estudiantes))
 

 #escritura de un archivo json
with open(estudiantes_json_path,"w") as estudiantes_json:
    #serializar  - dict -> json
    estudiante_dict = {
        "nombre": "Juan",
        "edad": 25,
        "ciudad": "Madrid",
        "casado": False
    }
    json.dump(estudiante_dict, estudiantes_json, indent=2)