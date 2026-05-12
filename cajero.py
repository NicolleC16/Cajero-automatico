class CuentaBancaria:

    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def mostrar_saldo(self):
        print("Tu saldo es:", self.saldo)

    def consignar(self, valor):
        if valor > 0:
            self.saldo = self.saldo + valor
            print("Consignación realizada.")
        else:
            print("Valor inválido.")

    def retirar(self, valor):
        if valor > self.saldo:
            print("No tienes suficiente dinero.")
        elif valor <= 0:
            print("Valor inválido.")
        else:
            self.saldo = self.saldo - valor
            print("Retiro exitoso.")


cuenta = CuentaBancaria("Nicolle", 3200000)

while True:

    print("\n CAJERO ")
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
        print("Adiós")
        break

    else:
        print("Opción incorrecta")
