def Menu(ListaGanancias, ListaGastos):
    while True:
        print("     MONITOREO DE FINANZAS    \n")
        print("1: Ganancias de Usuario")
        print("2: Gastos de Usuario")
        print("3: Mostrar Listas")
        print("4: Operaciones")
        print("0: Cerrar")
        try:
            op = int(input("Op = "))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
            continue
        
        match op:
            case 1:
                Ingresos(ListaGanancias)
            case 2:
                Gastos(ListaGastos)
            case 3:
                MostrarListas(ListaGanancias, ListaGastos)
            case 4:
                Operaciones(ListaGanancias, ListaGastos)
            case 0:
                print("Cerrando el programa...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

def Gastos(ListaGastos):
    monto = float(input("Ingrese el monto del gasto: "))
    ListaGastos.append(monto)
    print(f"Gasto de {monto} agregado.")
    
def Ingresos(ListaGanancias):
    monto = float(input("Ingrese el monto del ingreso: "))
    ListaGanancias.append(monto)
    print(f"Ingreso de {monto} agregado.")

def MostrarListas(ListaGanancias, ListaGastos):
    print("\n--- Lista de Ganancias ---")
    if ListaGanancias:
        for i, monto in enumerate(ListaGanancias, 1):
            print(f"{i}. {monto}")
    else:
        print("No hay ganancias registradas.")
    
    print("\n--- Lista de Gastos ---")
    if ListaGastos:
        for i, monto in enumerate(ListaGastos, 1):
            print(f"{i}. {monto}")
    else:
        print("No hay gastos registrados.")
    print()

def Operaciones(ListaGanancias, ListaGastos):
    suma_ganancias = sum(ListaGanancias)
    suma_gastos = sum(ListaGastos)
    
    balance = suma_ganancias - suma_gastos
    
    print("\n--- Resultado de Operaciones ---")
    print(f"Suma de Ganancias: {suma_ganancias}")
    print(f"Suma de Gastos: {suma_gastos}")
    
    if balance > 0:
        print(f"Balance: {balance} (Ganancia)")
    elif balance < 0:
        print(f"Balance: {balance} (Pérdida)")
    else:
        print("Balance: 0 (Sin Ganancia ni Pérdida)")

ListaGanancias = []
ListaGastos = []
Menu(ListaGanancias, ListaGastos)