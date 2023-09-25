class SistemaMotocicleta:
    def __init__(self, marca_moto, modelo_moto, precio_moto):
        self.marca_moto = marca_moto
        self.modelo_moto = modelo_moto
        self.precio_moto = precio_moto
        self.ventas_consolidadas = 0
        self.encargos_moto = 0

    def mostrar_marca(self):
        return f"Marca de la motocicleta: {self.marca_moto}"

    def mostrar_modelo(self):
        return f"Modelo de la motocicleta: {self.modelo_moto}"

    def gestionar_venta(self, cantidad):
        if cantidad > 0:
            self.ventas_consolidadas += cantidad
            print(f"Se vendieron {cantidad} unidades de {self.modelo_moto}.")
        else:
            print("Se alcanzó una cantidad de ventas")

    def gestionar_encargo(self, cantidad):
        if cantidad > 0:
            self.encargos_moto += cantidad
            print(f"Se realizaron {cantidad} encargos de {self.modelo_moto}.")
        else:
            print("Vienen esta cantidad de encargos")

    def mostrar_existencias(self):
        return f"Existencias de {self.modelo_moto}: {self.ventas_consolidadas} vendidas, {self.encargos_moto} en encargo."





# " Ejemplo "
moto1 = SistemaMotocicleta("Honda", "CBR 1000RR", 12500000)
moto2 = SistemaMotocicleta("Yamaha", "YZF R6", 14350000)

print(moto1.mostrar_marca())
print(moto1.mostrar_modelo())

moto1.gestionar_venta(5)
moto1.gestionar_encargo(3)

print(moto1.mostrar_existencias())
