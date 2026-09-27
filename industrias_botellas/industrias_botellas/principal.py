from botella import Botella
from botella_plastica import BotellaPlastica
from botella_vidrio import BotellaVidrio

obj_plastica = BotellaPlastica("500 ml", "cuello corto", "liso", "tapa azul", "sin grabados")
obj_vidrio = BotellaVidrio("750 ml", "cuello alargado", "estriado", "tapa de corcho", "vino")

print(obj_plastica.contener_liquidos("agua"))
print(obj_plastica.facilitar_el_vertido())
print(obj_plastica.cerrar_hermetico())
print(obj_plastica.transportar())
print(obj_plastica.manejar())
print(obj_plastica.compatibilidad_con_bebidas("frias"))
print(obj_plastica.reutilizar())
print(obj_plastica.transparencia())

print(obj_vidrio.contener_liquidos("vino"))
print(obj_vidrio.facilitar_el_vertido())
print(obj_vidrio.cerrar_hermetico())
print(obj_vidrio.transportar())
print(obj_vidrio.manejar())
print(obj_vidrio.compatibilidad_con_bebidas("calientes y frias"))
print(obj_vidrio.reutilizar())
print(obj_vidrio.transparencia())
