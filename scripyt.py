from usuario import Usuario
import datetime
import json
import pytz

#Formatos de fecha y hora, con horario regional.
tz_CL = pytz.timezone('America/Santiago')
datetime_CL = datetime.datetime.now(tz_CL)

#lista para guarar usuarios correctamente registrados.
lista_usuario = []

#lectura del archivo usuarios.txt
with open("usuarios.txt") as u:
    #Leer primera linea del texto. 
    linea = u.readline()  
    #Iteración para agregar cada linea de registros a una lista.
    while linea:
        try:
            #transformar la linea leía a un formato objeto python.
            usuario = json.loads(linea)
            #Agregar a una lista una instancia de la clase Usuario con los datos del objeto python (usuario)
            lista_usuario.append(Usuario(
                usuario.get("nombre"),
                usuario.get("apellido"),
                usuario.get("email"),
                usuario.get("genero")
            ))
        except Exception as e:
            #Si encuentra un error durante la iteración, se registra en un archivo error.log y continua su registro.
            with open("error.log", "a+") as log:
                log.write(f"{datetime_CL.strftime("%d/%m/%Y %H:%M:%S")}, {e} \n")
        finally:
            #Paso a la siguiente linea, para continuar su iteración.
            linea = u.readline()
#Se imprime la lista de usuarios, con las instancias creadas de la clase usuario (se muestra solo el "nombre".) 
print(lista_usuario)