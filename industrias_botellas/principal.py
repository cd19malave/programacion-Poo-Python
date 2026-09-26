from botella import Botella
from botella_vidrio import BotellaVidrio
from botella_plastica import BotellaPlastica

obj_botella = Botella("vidrio", "750 ml", "cuello", "estriado", "tapa de rosca", "logo IB")
obj_vidrio = BotellaVidrio("750 ml", "cuello", "estriado", "tapa de rosca", "logo IB")
obj_plastico = BotellaPlastica("500 ml", "cuerpo", "liso", "tapa rosca", "serigrafia")

print(obj_botella.hacer_saludo("Carlos"))
print(obj_botella.contener_liquidos("agua"))
print(obj_botella.facilitar_el_vertido())
print(obj_botella.cerrar_hermetico())
print(obj_botella.transportar())
print(obj_botella.manejar())
print(obj_botella.compatibilidad_con_bebidas("calientes y frias"))
print(obj_botella.reutilizar())
print(obj_botella.transparencia())

print(obj_vidrio.compatibilidad_con_bebidas("calientes y frias"))
print(obj_vidrio.transparencia())

print(obj_plastico.compatibilidad_con_bebidas("frias"))
print(obj_plastico.transparencia())
