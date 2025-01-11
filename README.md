# LiDARMaverickNovVerification
Script en Python para detectar archivos .nov de 0 KB y sus respectivas trayectorias generadas por el sensor LiDAR Maverick.

#AUTORES
- JUAN DAVID ORTIZ
- JENNY GUASHPA

# LiDAR NOV File Checker

Este proyecto es un **script en Python** diseñado para trabajar con datos provenientes del sensor LiDAR **Maverick**. Su principal objetivo es detectar archivos `.nov` con un tamaño de **0 KB** y validar las trayectorias asociadas en archivos `sessionMetadata.json`. Los resultados se almacenan en un archivo Excel generado automáticamente.

## Características
- Identifica archivos `.nov` vacíos (0 KB) dentro de una carpeta especificada.
- Valida trayectorias utilizando archivos `sessionMetadata.json` presentes en subcarpetas.
- Genera un archivo Excel con:
  - La lista de archivos `.nov` vacíos.
  - Las trayectorias encontradas o faltantes.

## Requisitos
Antes de ejecutar el script, asegúrate de tener instalado:
- Python 3.8 o superior.
- Las siguientes bibliotecas de Python:
  - `os` (estándar de Python)
  - `json` (estándar de Python)
  - `pandas` (`pip install pandas`)
  - `openpyxl` (para guardar archivos Excel: `pip install openpyxl`)

## Configuración
Modifica las siguientes variables en el código según tus necesidades:

- **`serieLiDAR`**: Identificador de la serie LiDAR (e.g., `"0007"`).
- **`folderIn`**: Ruta de entrada donde se encuentran los datos del sensor LiDAR.
- **`GDrive`**: Carpeta de destino para guardar el archivo Excel generado.

```python
serieLiDAR = "0007"  # Identificador del sensor LiDAR
folderIn = "E:\\Daniel Solis_John Cadena_0007_Sem2"  # Carpeta de entrada
GDrive = "C:\\Users\\ACER\\Documents\\Reportes_NOV\\"  # Carpeta de salida

### ¿Qué opinas? Si necesitas ajustes o agregar más detalles técnicos, ¡avísame! 🚀

