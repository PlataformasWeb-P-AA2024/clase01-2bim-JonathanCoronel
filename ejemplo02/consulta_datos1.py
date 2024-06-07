from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
import datetime

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Canton

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
cantones = session.query(Canton).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("A cada cantón pedirle el número de estudiantes")
for s in cantones:
    print("Canton :%s" % (s.nombre_canton))
    #print("%s" % (datetime.datetime.now().year - s.fundacion))
    print("Numero estudiantes:%s" % (s.obtener_numero_estudiantes()))
    print("---------")

