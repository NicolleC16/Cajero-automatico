# Tarea de Veronica: Mensaje de Bienvenida (AB#2)
print("=╔══════════════════════════════════════╗")
print("=║                                      ║")
print("=║           BANCO DIGITAL S.A.         ║")
print("=║                                      ║")
print("=║       Cajero Automático v1.0         ║")
print("=║    Tu dinero, siempre disponible     ║")
print("=║                                      ║")
print("=╚══════════════════════════════════════╝")

# Codigo base del cajero.
class CuentaBancaria:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f"Hola {self.nombre}, tu saldo es: ${self.saldo:.2f}")

    def consignar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print(f"Consignación realizada con éxito. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print("Error: El valor de la consignación debe ser mayor a 0.")

    def retirar(self, valor):
        if valor > self.saldo:
            print("Error: No tienes suficiente dinero para este retiro.")
        elif valor <= 0:
            print("Error: Valor de retiro inválido.")
        else:
            self.saldo = self.saldo - valor
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")

cuenta = CuentaBancaria("Nicolle", 3200000)

while True:
    print("\n--- MENÚ CAJERO ---")
    print("1. Ver saldo")
    print("2. Retirar")
    print("3. Consignar")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        cuenta.mostrar_saldo()
    elif opcion == "2":
        valor = float(input("¿Cuánto quieres retirar?: "))
        cuenta.retirar(valor)
    elif opcion == "3":
        valor = float(input("¿Cuánto quieres consignar?: "))
        cuenta.consignar(valor)
    elif opcion == "4":
        """
        # Tarea de Daniel: Mensaje de despedida (AB#7)
        """
        print(f"Cerrando sesion, hasta luego {cuenta.nombre}")
        break
    else:
        print("Opción incorrecta, intenta de nuevo.")