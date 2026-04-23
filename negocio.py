from datos import (obtener_alumnos, agregar_alumno, eliminar_alumno, modificar_alumno)


def _email_valido(email):
    email_limpio = email.strip()
    if not email_limpio:
        return False

    if "@" not in email_limpio:
        return False

    parte_local, separador, dominio = email_limpio.partition("@")
    if not separador or not parte_local or not dominio or "." not in dominio:
        return False

    return True

def listar_alumnos():
    alumnos = obtener_alumnos()
    return alumnos

def buscar_alumno(legajo):
    alumnos = obtener_alumnos()
    alumno = alumnos[alumnos['Legajo'] == legajo]
    return alumno

def cantidad_alumnos():
    alumnos = obtener_alumnos()
    cantidad = len(alumnos)
    return cantidad

def agregar_nuevo_alumno(legajo, nombres, email):
    nombres_limpios = nombres.strip()
    email_limpio = email.strip()

    if not nombres_limpios:
        return "Los nombres no pueden estar vacios."

    if not _email_valido(email_limpio):
        return "Email invalido. Debe tener un formato como usuario@dominio.com."

    alumnos = obtener_alumnos()
    if (alumnos['Legajo'] == legajo).any():
        return "Ya existe un alumno con ese legajo."

    agregar_alumno(legajo, nombres_limpios, email_limpio)
    return "Alumno agregado correctamente."


def eliminar_alumno_por_legajo(legajo):
    alumnos = obtener_alumnos()
    if not (alumnos['Legajo'] == legajo).any():
        return "No existe un alumno con ese legajo."

    eliminar_alumno(legajo)
    return "Alumno eliminado correctamente."

def modificar_alumno_por_legajo(legajo, nuevos_nombres=None, nuevo_email=None):
    alumnos = obtener_alumnos()
    if not (alumnos['Legajo'] == legajo).any():
        return "No existe un alumno con ese legajo."

    if nuevos_nombres is not None:
        nuevos_nombres_limpios = nuevos_nombres.strip()
        if not nuevos_nombres_limpios:
            return "Los nombres no pueden estar vacios."
        nuevos_nombres = nuevos_nombres_limpios

    if nuevo_email is not None:
        nuevo_email_limpio = nuevo_email.strip()
        if not _email_valido(nuevo_email_limpio):
            return "Email invalido. Debe tener un formato como usuario@dominio.com."
        nuevo_email = nuevo_email_limpio

    modificar_alumno(legajo, nuevos_nombres, nuevo_email)
    return "Alumno modificado correctamente."
