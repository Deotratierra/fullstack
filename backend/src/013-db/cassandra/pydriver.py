
"""
Instalar:
pip install cassandra-driver

Comprobar instalación:
python3 -c "import cassandra;print(cassandra.__version__)"
"""

# =============================================================

# Conectar a una instancia local de Cassandra

from cassandra.cluster import Cluster

cluster = Cluster()

# Podemos definir en su lugar una serie de nodos a los
#   que conectarse formando el cluster:
#cluster = Cluster(['192.168.0.1', '192.168.0.2'])

"""
El conjunto de direcciones IP que pasamos al cluster es simplemente
un conjunto inicial de puntos de contacto. Después de conectarse a uno
de los nodos, el driver descubrirá automáticamente el resto, así que
no es necesario indicar cada uno de los nodos del clúster.
"""

# =============================================================

# Conectar a un keyspace
session = cluster.connect("alvaro") # 'alvaro' es el nombre del keyspace

# Podemos cambiar de keyspace en medio de la sesión:
#session.set_keyspace('espacio')
# o así:
#session.execute('USE espacio;')

# =============================================================

# Ejecutar consultas:
rows = session.execute("SELECT * FROM users;")
for row in rows:
	# Cada fila está representada por un objecto ``namedtuple``
	print(row)
	print(row.firstname)

# Obtener los nombres de las columnas:
print(rows.column_names) # ['lastname', 'email', 'firstname', 'organization']

for (lastname, email, firstname, organization) in rows:
	# Podemos desempacar los datos mediante tuplas
	print(firstname, lastname, email, organization)

for row in rows:
	print(row[0])

# -------------------------------------------------------------

# Pasando parámetros a las consultas:
session.execute(
	"""
	INSERT INTO users (firstname, lastname, email, organization)
    VALUES (%s, %s, %s, %s)
	""",
	("Fernando", "Valbuena", "emailaleatorio@proveedor.com", "Uniplex")
)

""" Debes usar '%s' para todo tipo de argumentos, no sólo para cadenas.
Por ejemplo, lo siguiente sería incorrecto:

>>> session.execute("INSERT INTO USERS (name, age) VALUES (%s, %d)", ("bob", 42))  # wrong

Si necesitamos usar el carácter '%' podemos escaparlo con '%%'. Aunque sólo
pasemos un argumento, debemos pasarlo como una tupla: ``('argumento', )``.
"""

# Tabla de conversiones de tipos de Python a los tipos incorporados en Cassandra:
# https://datastax.github.io/python-driver/getting_started.html#type-conversions
