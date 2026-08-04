
# INPUT
# ==========================================
usuarios = { "amildred" : { "password" : "1234", "rol" : "alumno", "nombre" : "Mildred Ambrosio" },
             "benna" : { "password" : "1234", "rol" : "alumno", "nombre" : "Enna Bonilla" },
             "mraul" : { "password" : "1234", "rol" : "alumno", "nombre" : "Raul May" },
             "aalejandra" : { "password" : "1234", "rol" : "alumno", "nombre" : "Alejandra Alonzo" },
             "vandres" : { "password" : "1234", "rol" : "alumno", "nombre" : "Andres Valdes" },
             "squenny" : { "password" : "1234", "rol" : "alumno", "nombre" : "Quenny Sanchez" },
             "cisabel": { "password" : "1234", "rol" : "maestro", "nombre" : "Isabel Caballero" },
             "telia": { "password" : "1234", "rol" : "coordinador", "nombre" : "Elia Tamayo" },
              }

# PROCESS
# ==========================================
materias = ("Matemáticas", "Programación", "Ingles")

calificaciones = { "amildred" : {"Matemáticas" : 8.5, "Programación": 9.0, "Inglés": 7.5},
                   "benna" : {"Matemáticas" : 10.0, "Programación": 8.0, "Inglés": 5.0},
                   "mraul" : {"Matemáticas" : 9.0, "Programación": 8.5, "Inglés": 9.0},
                   "aalejandra" : {"Matemáticas" : 7.0, "Programación": 10.0, "Inglés": 10.0},
                   "vandres" : {"Matemáticas" : 7.8, "Programación": 9.0, "Inglés": 7.0},
                   "squenny" : {"Matemáticas" : 8.7, "Programación": 8.0, "Inglés": 8.0},
                   }
tematerias_aprobadas= set()
materias_reprobadas= set()
usuario= input("Ingrese su usario: ")
contraseña= input("Ingrese su contraseña: ")

# Validate login with a while loop 
while usuario not in usuarios.keys() or contraseña != usuarios[usuario]["password"]:
    print("Usuario o Contraseña incorrecta")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
else:
    print(f"Bienvenido, {usuarios[usuario]["nombre"]} ({usuarios[usuario]["rol"]}) ")
                   
                   
# BRANCHING BY ROLE
# ==========================================
if usuarios[usuario]["rol"] == "alumno":
    print(f"Boleta de {usuarios[usuario]["nombre"]}")
    for materia in calificaciones[usuario]:
        print(materia, ":", calificaciones[usuario][materia])
        if calificaciones[usuario][materia] >= 8:
            materias_aprobadas.add(materia)
        else:
            materias_reprobadas.add(materia)
    print(f"Materias aprobadas: {materias_aprobadas}")
    print(f"Materias reprobadas: {materias_reprobadas}")    
elif usuarios[usuario]["rol"] == "maestro":
    alumno = input("Ingrese el usuario del alumno deseado: ")
    materia = input("Ingrese la materia deseada: ")
    calificacion = float(input("Ingrese la nueva calificación: "))
    calificaciones[alumno][materia] = calificacion
    print(f"Alumno: {alumno}")
    print(f"Materia: {materia}")
    print(f"Nueva calificación: {calificacion}")
    print("Calificación actualizada.")
else:
    for personal in usuarios:
        if usuarios[personal]["rol"] == "maestro":
            print(f"Maestra/o {usuarios[personal]["nombre"]}")
    for materia in materias:
        print(materia)
    for estudiante in calificaciones:
        print(f"Estudiante {usuarios[estudiante]["nombre"]}: {calificaciones[estudiante]}")
        