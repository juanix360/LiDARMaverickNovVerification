# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 08:24:37 2025

@author: Juan Ortiz, Jenny Guashpa
"""
import os
import json
import pandas as pd
from datetime import datetime

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#DATOS IMPORTANTE A CAMBIAR
serieLiDAR = "0007"
folderIn = r"C:\Users\Usuario\Desktop\Juan_Ortiz\Documents LiDAR Maverick\Data_Lidar"

#Cambiar SOLO la direccion de la PC
GDrive=r"C:\Users\Usuario\Desktop\Juan_Ortiz\Documents LiDAR Maverick/"

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#SALIDA DE ARCHIVOS

# Obtener la fecha de modificación de la carpeta
mod_time = os.path.getmtime(folderIn)  # Devuelve la fecha en formato timestamp
mod_date = datetime.fromtimestamp(mod_time).strftime("%d%m%Y")  # Formatear a 'YYYY-MM-DD'

# Concatenar la fecha al string
folderOut = f"{GDrive}{serieLiDAR}_{mod_date}.xlsx"

# Crear lista para almacenar los datos
zero_byte_files = []
json_check_results = []
valid_files = []

# Verificar si la carpeta existe
def get_zero_byte_files(folder_path):
    if os.path.exists(folder_path):
        # Recorrer los archivos en la carpeta especificada
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):  # Verificar que sea un archivo
                file_size = os.path.getsize(file_path)  # Obtener tamaño en bytes
                if file_size == 0 and file_name.endswith('.novb'):  # Filtrar archivos .novb de 0 bytes
                    zero_byte_files.append({"Nombre": file_name})
                if file_size != 0 and file_name.endswith('.novb'):
                    valid_files.append({"Nombre": file_name})
    else:
        print(f"Error: La carpeta no existe en la ruta especificada -> {folder_path}")

# Buscar archivos JSON en subcarpetas
def check_json_files(folderIn, file_list):
    global json_check_results
    json_check_results = [] 
 # Iterar sobre todos los archivos listados en la lista proporcionada
    for file_info in file_list:
        file_name = file_info["Nombre"]
        matching_folders = []  # Lista para almacenar múltiples carpetas coincidentes

        # Buscar archivos JSON en subcarpetas
        for root, dirs, files in os.walk(folderIn):
            if "sessionMetadata.json" in files:
                json_path = os.path.join(root, "sessionMetadata.json")
                with open(json_path, 'r') as json_file:
                    json_data = json.load(json_file)
                    if json_data.get("collectionSystemTrajectoryName") == file_name:
                        matching_folders.append(os.path.basename(root))  # Agregar carpeta a la lista
        # Si se encontraron carpetas coincidentes, agregarlas al resultado
        if matching_folders:
            # Crear una fila por cada carpeta que contiene el archivo
            for folder in matching_folders:
                json_check_results.append({"Nombre": file_name, "Carpeta_NOV": folder})
        else:
            # Si no se encontraron carpetas, agregar una fila con la carpeta vacía
            json_check_results.append({"Nombre": file_name, "Carpeta_NOV": ""})

# Llamar la función para obtener archivos de 0 bytes
get_zero_byte_files(folderIn)

# Verificar si se encontraron archivos de 0 bytes
if zero_byte_files:
    # Crear un DataFrame con los archivos que cumplen la condición
    df_zero_bytes = pd.DataFrame(zero_byte_files)
    print("Archivos de 0 bytes encontrados:")
    print(df_zero_bytes)  # Mostrar el contenido de zero_byte_files
        # Guardar los resultados en una hoja del archivo Excel
else:
    print("No se encontraron archivos de 0 bytes.")
    
if valid_files:
    # Crear un DataFrame con los archivos que cumplen la condición
    df_valid_files = pd.DataFrame(valid_files)
    print("Archivos de 0 bytes encontrados:")
    print(valid_files)  # Mostrar el contenido de valid_files
        # Guardar los resultados en una hoja del archivo Excel
else:
    print("No se encontraron archivos de 0 bytes.")

# Verificar los archivos JSON
check_json_files(folderIn, zero_byte_files)

# Crear un DataFrame con los resultados de la verificación de JSON
if json_check_results:
    df_json_check = pd.DataFrame(json_check_results)
    print("Resultados de verificación JSON:")
    print(df_json_check)
   # Guardar los resultados en una hoja del archivo Excel
    if os.path.exists(folderOut):
        with pd.ExcelWriter(folderOut, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            df_json_check.to_excel(writer, sheet_name='NOVs_0KB', index=False)
    else:
        with pd.ExcelWriter(folderOut, engine='openpyxl', mode='w') as writer:
            df_json_check.to_excel(writer, sheet_name='NOVs_0KB', index=False)
else:
    print("No se encontraron resultados de JSON.")

# Verificar los archivos JSON
check_json_files(folderIn, valid_files)

# Crear un DataFrame con los resultados de la verificación de JSON
if json_check_results:
    df_valid_files = pd.DataFrame(json_check_results)
    print("Resultados de verificación JSON:")
    print(df_valid_files)
   # Guardar los resultados en una hoja del archivo Excel
    if os.path.exists(folderOut):
        with pd.ExcelWriter(folderOut, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
            df_valid_files.to_excel(writer, sheet_name='NOVs_X_Carpeta', index=False)
    else:
        with pd.ExcelWriter(folderOut, engine='openpyxl', mode='w') as writer:
            df_valid_files.to_excel(writer, sheet_name='NOVs_X_Carpeta', index=False)
else:
    print("No se encontraron resultados de JSON.")