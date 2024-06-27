import os
import time
# Definición de la lista donde se almacenarán los trabajadores
trabajadores = []

# Función para registrar un nuevo trabajador
def registrar_trabajador():
    print("\nRegistro de Trabajador")
    print("-----------------------")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    cargo = input("Ingrese cargo: ")
    while True:
        try:
            sueldo_bruto = float(input("Ingrese sueldo bruto: "))
            break
        except ValueError:
            print("Error: Debe ingresar un valor numérico para el sueldo bruto.")
    
    # Calcular descuentos y sueldo líquido
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    sueldo_liquido = sueldo_bruto - desc_salud - desc_afp
    
    # Guardar los datos en la lista de trabajadores
    trabajadores.append({
        'nombre': nombre,
        'apellido': apellido,
        'cargo': cargo,
        'sueldo_bruto': sueldo_bruto,
        'desc_salud': desc_salud,
        'desc_afp': desc_afp,
        'sueldo_liquido': sueldo_liquido
    })
    

    
    print("¡Trabajador registrado exitosamente!\n")
    time.sleep(4)
    os.system("cls")
    listar_trabajadores()

# Función para listar todos los trabajadores registrados
def listar_trabajadores():
    if len(trabajadores) == 0:
        print("No hay trabajadores registrados.")
    else:
        print("\nListado de Trabajadores")
        print("-----------------------")
        for idx, trabajador in enumerate(trabajadores, start=1):
            print(f"Trabajador {idx}:")
            print(f"Nombre: {trabajador['nombre']} {trabajador['apellido']}")
            print(f"Cargo: {trabajador['cargo']}")
            print(f"Sueldo Bruto: {trabajador['sueldo_bruto']}")
            print(f"Descuento Salud: {trabajador['desc_salud']}")
            print(f"Descuento AFP: {trabajador['desc_afp']}")
            print(f"Sueldo Líquido: {trabajador['sueldo_liquido']}")
            print("-----------------------")
        print()

        time.sleep(5)
        os.system("cls")
        imprimir_planilla()

# Función para imprimir la planilla de sueldos en un archivo de texto
def imprimir_planilla():
    if len(trabajadores) == 0:
        print("No hay trabajadores registrados para imprimir planilla.")
        return
    
    cargos_disponibles = ["CEO", "Desarrollador", "Analista de datos"]
    
    print("\nCargos Disponibles:")
    for i, cargo in enumerate(cargos_disponibles, start=1):
        print(f"{i}. {cargo}")
    
    while True:
        try:
            opcion = int(input("Seleccione el número correspondiente al cargo o 0 para imprimir todos: "))
            if opcion < 0 or opcion > len(cargos_disponibles):
                print("Opción inválida. Intente nuevamente.")
            else:
                break
        except ValueError:
            print("Opción inválida. Intente nuevamente.")
    
    if opcion == 0:
        nombre_archivo = "planilla_todos.txt"
        with open(nombre_archivo, 'w') as f:
            for trabajador in trabajadores:
                f.write(f"Nombre: {trabajador['nombre']} {trabajador['apellido']}\n")
                f.write(f"Cargo: {trabajador['cargo']}\n")
                f.write(f"Sueldo Bruto: {trabajador['sueldo_bruto']}\n")
                f.write(f"Descuento Salud: {trabajador['desc_salud']}\n")
                f.write(f"Descuento AFP: {trabajador['desc_afp']}\n")
                f.write(f"Sueldo Líquido: {trabajador['sueldo_liquido']}\n")
                f.write("-----------------------\n")
        print(f"Planilla de sueldos generada en el archivo '{nombre_archivo}'.")
    else:
        cargo_seleccionado = cargos_disponibles[opcion - 1]
        nombre_archivo = f"planilla_{cargo_seleccionado.lower().replace(' ', '_')}.txt"
        with open(nombre_archivo, 'w') as f:
            for trabajador in trabajadores:
                if trabajador['cargo'] == cargo_seleccionado:
                    f.write(f"Nombre: {trabajador['nombre']} {trabajador['apellido']}\n")
                    f.write(f"Cargo: {trabajador['cargo']}\n")
                    f.write(f"Sueldo Bruto: {trabajador['sueldo_bruto']}\n")
                    f.write(f"Descuento Salud: {trabajador['desc_salud']}\n")

registrar_trabajador()
      
