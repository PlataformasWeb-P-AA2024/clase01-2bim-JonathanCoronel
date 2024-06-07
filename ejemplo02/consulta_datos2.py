from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and
import datetime

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Provincia

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
provincias = session.query(Provincia).all()

# Se recorre la lista a través de un ciclo
# repetitivo for en python
print("A cada cantón pedirle el número de estudiantes")
for s in provincias:
    print("Provicnia :%s" % (s.nombre_provincia))
    #print("%s" % (datetime.datetime.now().year - s.fundacion))
    print("Numero Docentes:%s" % (s.obtener_numero_docentes()))
    print("---------")

