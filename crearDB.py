import sqlite3

# Crear o conectar a la base de datos
conexion = sqlite3.connect("escuela2.db")

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    calificacion INTEGER
)
""")

# Insertar 5 alumnos
cursor.execute("INSERT INTO alumnos (nombre, calificacion) VALUES ('Juan', 8)")
cursor.execute("INSERT INTO alumnos (nombre, calificacion) VALUES ('Ana', 9)")
cursor.execute("INSERT INTO alumnos (nombre, calificacion) VALUES ('Luis', 7)")
cursor.execute("INSERT INTO alumnos (nombre, calificacion) VALUES ('Maria', 10)")
cursor.execute("INSERT INTO alumnos (nombre, calificacion) VALUES ('Pedro', 6)")

# Guardar cambios
conexion.commit()

# Consultar datos
cursor.execute("SELECT * FROM alumnos")

# Mostrar resultados
for fila in cursor.fetchall():
    print(fila)

# Cerrar conexión
conexion.close()

print("Base de datos creada y consultada correctamente")