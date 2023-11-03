class Habitacion:
    def __init__(self, numero, costo, tipo):
        self.numero = numero
        self.costo = costo
        self.tipo = tipo
        self.disponible = True

    def ocupar(self):
        self.disponible = False

    def desocupar(self):
        self.disponible = True

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Cliente(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

class Empleado(Persona):
    def __init__(self, nombre, cargo):
        super().__init__(nombre)
        self.cargo = cargo

class Reserva(Habitacion, Cliente):
    def __init__(self, habitacion, cliente, cantidad, monto_prepagado=0):
        Habitacion.__init__(self, habitacion.numero, habitacion.costo, habitacion.tipo)
        Cliente.__init__(self, cliente.nombre)
        self.cantidad = cantidad
        self.monto_prepagado = monto_prepagado

class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.clientes = []
        self.reservaciones = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def realizar_reservacion(self, cliente, tipo_habitacion, cantidad, monto_prepagado=0):
        habitaciones_tipo = [h for h in self.habitaciones if h.tipo == tipo_habitacion]
        habitaciones_disponibles = [h for h in habitaciones_tipo if h.disponible]

        if len(habitaciones_disponibles) < cantidad:
            print(f"No hay suficientes habitaciones disponibles de tipo {tipo_habitacion}.")
            return

        costo_total = habitaciones_tipo[0].costo * cantidad
        habitacion_asignada = habitaciones_disponibles[0]
        for habitacion in habitaciones_disponibles[:cantidad]:
            habitacion.ocupar()
        
        cliente.habitacion_asignada = habitacion_asignada
        reserva = Reserva(habitacion_asignada, cliente, cantidad, monto_prepagado)
        self.reservaciones.append(reserva)
        print(f"Reservación realizada por {cliente.nombre} en {tipo_habitacion}.")
        print(f"Cantidad de habitaciones: {cantidad}")
        print(f"Monto pagado: ${monto_prepagado}")
        print(f"Monto total a pagar: ${costo_total - monto_prepagado}")

    def listar_reservaciones(self):
        print("Reservaciones:")
        for reservacion in self.reservaciones:
            print(f"Cliente: {reservacion.nombre}")
            print(f"Habitación: {reservacion.numero}")
            print(f"Tipo de habitación: {reservacion.tipo}")
            print(f"Cantidad de habitaciones: {reservacion.cantidad}")
            print(f"Monto pagado: ${reservacion.monto_prepagado}")
            costo_total = reservacion.costo
            print(f"Monto total a pagar: ${costo_total - reservacion.monto_prepagado}")
            print("\n")

    def habitaciones_disponibles(self, habitacion):
        cantidad = 0
        for reserva in self.reservaciones:
            if reserva.numero == habitacion.numero:
                cantidad += reserva.cantidad
        return 5 - cantidad

def main():
    hotel = Hotel("Mi Hotel")

    for i in range(5):
        habitacion1 = Habitacion(101 + i, 980, "Estandar")
        hotel.agregar_habitacion(habitacion1)
        habitacion2 = Habitacion(201 + i, 1890, "De lujo")
        hotel.agregar_habitacion(habitacion2)
        habitacion3 = Habitacion(301 + i, 2990, "Suite")
        hotel.agregar_habitacion(habitacion3)

    sesion_iniciada = False

    while True:
        print("Menú:")

        if not sesion_iniciada:
            print("1. Iniciar sesión")
            print("2. Salir")
        else:
            print("1. Listar clientes")
            print("2. Listar habitaciones")
            print("3. Listar reservaciones")
            print("4. Realizar reservación")
            print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if not sesion_iniciada:
            if opcion == "1":
                usuario = input("Nombre de usuario: ")
                contrasena = input("Contraseña: ")

                if usuario == "Juan Carlos Sarabia" and contrasena == "HotelUsuario9090":
                    print("¡Sesión iniciada!")
                    sesion_iniciada = True
                else:
                    print("Nombre de usuario o contraseña incorrectos.")
            elif opcion == "2":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        else:
            if opcion == "1":
                print("Clientes:")
                for reservacion in hotel.reservaciones:
                    print(f"Cliente: {reservacion.nombre} - Habitación: {reservacion.numero} ({reservacion.tipo})")
            elif opcion == "2":
                print("Habitaciones:")
                for habitacion in hotel.habitaciones:
                    estado = "Disponible" if habitacion.disponible else "Ocupada"
                    disponibles = hotel.habitaciones_disponibles(habitacion)
                    print(f"Habitación {habitacion.numero} ({habitacion.tipo}) - Costo: ${habitacion.costo} - Estado: {estado} - Disponibles: {disponibles}")
            elif opcion == "3":
                hotel.listar_reservaciones()
            elif opcion == "4":
                nombre_cliente = input("Nombre del cliente: ")
                tipo_habitacion = input("Tipo de habitación (Estandar/De lujo/Suite): ").capitalize()
                cantidad_habitaciones = int(input("Cantidad de habitaciones a reservar: "))
                monto_prepagado = float(input("Monto prepago: "))
                cliente = Cliente(nombre_cliente)
                hotel.realizar_reservacion(cliente, tipo_habitacion, cantidad_habitaciones, monto_prepagado)
            elif opcion == "5":
                print("Sesión finalizada.")
                sesion_iniciada = False
            else:
                print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

