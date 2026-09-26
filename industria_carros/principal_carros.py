from carro import Carro
from carro_gasolina import CarroGasolina
from carro_electrico import CarroElectrico

obj_carro = Carro("Sedan X", "azul", "2.0", 4, 5, "diesel")
obj_gasolina = CarroGasolina("Tanque G", "rojo", "3.0", 4, 7)
obj_electrico = CarroElectrico("Compacto E", "blanco", "electrico", 4, 5)

print(obj_carro.arrancar())
print(obj_carro.acelerar(50))
print(obj_carro.frenar(20))
print(obj_carro.apagar())
print(obj_carro.climatizacion("encendida"))
print(obj_carro.sistema_direccion("hidraulica"))
print(obj_carro.tipo_seguridad())
print(obj_carro.luces("encendidas"))
print(obj_carro.sistema_ventanas("cerradas"))
print(obj_carro.sistema_espejo("ajustados"))

print(obj_gasolina.arrancar())
print(obj_gasolina.sistema_direccion("hidraulica"))

print(obj_electrico.arrancar())
print(obj_electrico.sistema_direccion("electrica"))
