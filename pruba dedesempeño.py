




#Lista de estudiantes
estudiantes = []

# Funciones
def registrar():
    id = input("ID: ")
    name = input("name: ")
    age = input("age: ")
    curso = input("Course: ")
    estado = input("Estado: ")

    estudiante = {
        "id": id,
        "name": name,
        "age": age,
        "curso": curso,
        "estado": estado
    }

    estudiantes.append(estudiante)
    print("Estudiante agregado")

def mostrar():
    if len(estudiantes) == 0:
        print("No hay estudiantes")
    else:
        for e in estudiantes:
            print(e)

def buscar():
    j = input("Ingrese ID o nombre: ")
    for e in estudiantes:
        if j == e["id"] or j == e["nombre"]:
            print(e)

def eliminar():
    j = input("ID a eliminar: ")
    for e in estudiantes:
        if e["id"] == j:
            estudiantes.remove(e)
            print("Eliminado")

def actualizar():
    j = input("ID a actualizar: ")
    for e in estudiantes:
        if e["id"] == j:
            e["name"] = input("Nuevo name: ")
            e["age"] = input("Nueva age: ")
            e["curso"] = input("Nuevo curso: ")
            e["estado"] = input("Nuevo estado: ")
            print("Actualizado")

op = ""

while op != "6":
    
    print("\n--- MENÚ ---")
    print("1. register")
    print("2. Display")
    print("3. Search")
    print("4. Update")
    print("5. Delate")
    print("6. Log aut ")

    op = input("Opción: ")
    

    if op == "1":
        registrar()
    elif op == "2":
        mostrar()
    elif op == "3":
        buscar()
    elif op == "4":
        actualizar()
    elif op == "5":
        eliminar()
    elif op == "6":
        print("Adiós")
    else:
        print("Opción inválida")



