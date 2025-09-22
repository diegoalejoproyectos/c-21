import re
import csv

# Rutas de archivo
archivo_entrada = "/mnt/data/DEUDORES.lst"
archivo_salida = "/mnt/data/alumnos.csv"

# Leer el archivo de entrada
with open(archivo_entrada, "r", encoding="latin-1") as f:
    lineas = f.readlines()

# Variables
carrera = ""
curso = ""
datos = []

# Patrón para separar columnas (2 o más espacios consecutivos)
patron = re.compile(r"\s{2,}")

# Recorrer líneas
for linea in lineas:
    linea_strip = linea.strip()

    # Buscar carrera y curso en encabezado
    if linea_strip.startswith("Carrera:"):
        carrera = linea_strip.split("Carrera:")[1].strip()
    if linea_strip.startswith("Curso"):
        curso = linea_strip.split(":")[1].strip()

    # Filtrar registros de alumnos (líneas que comienzan con un número)
    if re.match(r"^\d+\s", linea_strip):
        partes = patron.split(linea_strip)

        # Normalizar a mínimo 11 columnas antes de agregar carrera y curso
        while len(partes) < 11:
            partes.append("")

        # Agregar carrera y curso
        partes.append(carrera)
        partes.append(curso)

        datos.append(partes)

# Guardar en CSV
with open(archivo_salida, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "Nro","Codigo","C.I.","Paterno","Materno","Nombres","E",
        "Tipo de Beca","Monto_Cancelado","Monto_P_Cance","Cuotas",
        "Carrera","Curso"
    ])
    writer.writerows(datos)

archivo_salida
