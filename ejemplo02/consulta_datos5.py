from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
import datetime

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Parroquia

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros de 
# la entidad Club
parroquias = session.query(Parroquia).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("A cada cantón pedirle el número de estudiantes")
for s in parroquias:
    print("Parroquia :%s" % (s.nombre_parroquia))
    #print("%s" % (datetime.datetime.now().year - s.fundacion))
    print("%s" % (s.obtener_tipos_jornada_establecimientos()))
    print("---------")

