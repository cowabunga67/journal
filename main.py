from datetime import datetime
from journal import *

# Hola, voy a hacer cositas :)
rutaDiario = "diario.txt"
ahora = datetime.today()

print("=== Iniciando aplicación de Diario ===")

with open(rutaDiario, "a", encoding="utf-8") as newVer: 	# se abre el archivo en modo "append"
    if lockFile(rutaDiario, ahora):						# si el diario está marcado para no escribir nuevas entradas
        blockNotif(ahora)
    else:												# si está permitido escribir nuevas entradas
        newEntry(newVer, ahora)
        print("Entrada guardada correctamente.")
                
# Como estamos usando open con with, no es necesario hacer .close(), ya que se cierra
# automáticamente una vez que ejecuta todas las líneas de codigo que están dentro de
# su estructura
