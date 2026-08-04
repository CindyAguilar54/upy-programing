
# INPUT
# ==========================================
materias = ('Matemáticas', 'Programación', 'Inglés')

usuarios = {
    'amildred': {'password': '1234', 'rol': 'alumno', 'nombre': 'Mildred Ambrosio'},
    'benna': {'password': '1234', 'rol': 'alumno', 'nombre': 'Enna Bonilla'},
    'mraul': {'password': '1234', 'rol': 'alumno', 'nombre': 'Raul May'},
    'aalejandra': {'password': '1234', 'rol': 'alumno', 'nombre': 'Alejandra Alonzo'},
    'vandres': {'password': '1234', 'rol': 'alumno', 'nombre': 'Andres Valdes'},
    'squenny': {'password': '1234', 'rol': 'alumno', 'nombre': 'Quenny Sanchez'},
    'cisabel': {'password': '1234', 'rol': 'maestro', 'nombre': 'Isabel Caballero'},
    'telia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Elia Tamayo'}
}

calificaciones = {
    'amildred': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'benna': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'mraul': {'Matemáticas': 7.0, 'Programación': 7.5, 'Inglés': 8.0},
    'aalejandra': {'Matemáticas': 9.5, 'Programación': 9.0, 'Inglés': 9.5},
    'vandres': {'Matemáticas': 6.0, 'Programación': 6.5, 'Inglés': 7.0},
    'squenny': {'Matemáticas': 8.0, 'Programación': 8.5, 'Inglés': 9.0}
}

# PROCESS
# ==========================================
usuario_actual = None
rol_actual = None
nombre_actual = None

# Validate login with a while loop 
while usuario_actual is None:
    username_input = input("Usuario: ").strip()
    password_input = input("Contraseña: ").strip()
    
    if username_input in usuarios and usuarios[username_input]['password'] == password_input:
        usuario_actual = username_input
        rol_actual = usuarios[username_input]['rol']
        nombre_actual = usuarios[username_input]['nombre']
        print(f"Bienvenido, {nombre_actual} ({rol_actual})")
    else:
        print("Credenciales incorrectas. Intente de nuevo.")

# BRANCHING BY ROLE
# ==========================================
if rol_actual == 'alumno':
    print(f"\nBoleta de {nombre_actual}")
    
    aprobadas = set()
    pendientes = set()
    
    for materia in materias:
        cal = calificaciones[usuario_actual].get(materia, 0.0)
        print(f"{materia}: {cal}")
        if cal >= 8.0:
            aprobadas.add(materia)
        else:
            pendientes.add(materia)
            
    print(f"Materias aprobadas: {aprobadas}")
    print(f"Materias pendientes: {pendientes}")

elif rol_actual == 'maestro':
    print("\n--- Lista de Alumnos ---")
    for uname, info in usuarios.items():
        if info['rol'] == 'alumno':
            print(f"- Usuario: {uname} | Nombre: {info['nombre']}")
            
    alumno_elegido = input("\nAlumno (username): ").strip()
    materia_elegida = input("Materia: ").strip()
    nueva_cal = float(input("Nueva calificación: "))
    
    if alumno_elegido in calificaciones and materia_elegida in materias:
        calificaciones[alumno_elegido][materia_elegida] = nueva_cal
        print("Calificación actualizada.")
    else:
        print("Error: Alumno o materia inválidos.")

elif rol_actual == 'coordinador':
    print("\n--- REPORTE DE COORDINACIÓN (Read-Only) ---")
    
    print("\n1. Lista de Profesores:")
    for uname, info in usuarios.items():
        if info['rol'] == 'maestro':
            print(f"- {info['nombre']} ({uname})")
            
    print("\n2. Lista de Materias:")
    for materia in materias:
        print(f"- {materia}")
        
    print("\n3. Lista de Alumnos y Calificaciones:")
    for uname, info in usuarios.items():
        if info['rol'] == 'alumno':
            print(f"\nAlumno: {info['nombre']} ({uname})")
            for materia in materias:
                cal = calificaciones.get(uname, {}).get(materia, "N/A")
                print(f"   {materia}: {cal}")