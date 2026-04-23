import pandas as pd
import time

def obtener_alumnos():
    datos = pd.read_excel('Alumnos 2026.xlsx')
    if 'Legajo' in datos.columns:
        datos['Legajo'] = pd.to_numeric(datos['Legajo'], errors='coerce').astype('Int64')
    return datos

def agregar_alumno(legajo, nombres, email):
    datos = obtener_alumnos()
    nuevo_alumno = pd.DataFrame({'Legajo': [legajo], 'Nombres': [nombres], 'Email': [email]})
    datos = pd.concat([datos, nuevo_alumno], ignore_index=True) # Agrega el nuevo alumno al DataFrame existente, ignorando los índices para evitar duplicados
    datos.to_excel('Alumnos 2026.xlsx', index=False) # Guarda los cambios en el archivo Excel después de agregar el nuevo alumno, sin incluir el índice en el archivo
    return datos

def eliminar_alumno(legajo):
    datos = obtener_alumnos()
    datos = datos[datos['Legajo'] != legajo] # Elimina el alumno con el legajo especificado, manteniendo solo los alumnos cuyo legajo no coincide con el proporcionado
    datos.to_excel('Alumnos 2026.xlsx', index=False) # Guarda los cambios en el archivo Excel después de eliminar el alumno
    return datos

def modificar_alumno(legajo, nuevos_nombres=None, nuevo_email=None):
    datos = obtener_alumnos()
    if legajo in datos['Legajo'].values:
        if nuevos_nombres is not None:
            datos.loc[datos['Legajo'] == legajo, 'Nombres'] = nuevos_nombres # Modifica los nombres del alumno con el legajo especificado si se proporcionan nuevos nombres
        if nuevo_email is not None:
            datos.loc[datos['Legajo'] == legajo, 'Email'] = nuevo_email # Modifica el email del alumno con el legajo especificado si se proporciona un nuevo email
        datos.to_excel('Alumnos 2026.xlsx', index=False) # Guarda los cambios en el archivo Excel después de modificar la información del alumno
    return datos

def saludar_usuario():
    print("Bienvenido al sistema de gestion de alumnos.")
    print("Cargando datos...")
    time.sleep(2)
    print("Datos cargados exitosamente.")

def modificar_alumno(legajo, nuevos_nombres=None, nuevo_email=None):
    datos = obtener_alumnos()
    if legajo in datos['Legajo'].values:
        if nuevos_nombres is not None:
            datos.loc[datos['Legajo'] == legajo, 'Nombres'] = nuevos_nombres # Modifica los nombres del alumno con el legajo especificado si se proporcionan nuevos nombres
        if nuevo_email is not None:
            datos.loc[datos['Legajo'] == legajo, 'Email'] = nuevo_email # Modifica el email del alumno con el legajo especificado si se proporciona un nuevo email
        datos.to_excel('Alumnos 2026.xlsx', index=False) # Guarda los cambios en el archivo Excel después de modificar la información del alumno
    return datos
