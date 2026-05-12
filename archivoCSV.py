import csv

with open("alumnos.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["Alumno", "Calificación"])

    for i in range(1, 21):
        nombre = f"Alumno {i}"
        calificacion = 6 + (i % 5)
        writer.writerow([nombre, calificacion])

print("Archivo alumnos.csv creado correctamente")