# Se define una lista vacía para almacenar los estudiantes y sus notas
estudiantes = []


# Se define una función para agregar un estudiante y sus notas al registro
def agregar_estudiante():
  nombre = input("Ingrese el nombre del estudiante: ")
  nota1 = float(input("Ingrese la nota 1: "))
  nota2 = float(input("Ingrese la nota 2: "))
  nota3 = float(input("Ingrese la nota 3: "))
  promedio = (nota1 + nota2 + nota3) / 3
  estudiantes.append({
    "nombre": nombre,
    "nota1": nota1,
    "nota2": nota2,
    "nota3": nota3,
    "promedio": promedio
  })
  print("Estudiante agregado con éxito.")


# Se llama a la función para agregar los 3 estudiantes
for i in range(3):
  agregar_estudiante()

# Se imprime el registro completo de estudiantes y sus notas
print("\nRegistro de estudiantes:")
for estudiante in estudiantes:
  print(f"Nombre: {estudiante['nombre']}")
  print(f"Nota 1: {estudiante['nota1']}")
  print(f"Nota 2: {estudiante['nota2']}")
  print(f"Nota 3: {estudiante['nota3']}")
  print(f"Promedio: {estudiante['promedio']}\n")
