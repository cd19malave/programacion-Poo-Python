from botella_termica import BotellaTermica
from termica_plastica import TermicaPlastica
from termica_vidrio import TermicaVidrio

termo_agua = TermicaPlastica("600 ml", "curva", "marcador de agua", "tapa a rosca", "lineas de medida")
termo_te = TermicaVidrio("400 ml", "alta y delgada", "lisa", "tapa de madera", "sin marcas")

print(termo_agua.llenar("agua fria"))
print(termo_agua.servir())
print(termo_agua.precintar())
print(termo_agua.llevar())
print(termo_agua.sostener())
print(termo_agua.uso_en_bebidas("calientes"))
print(termo_agua.reciclar())
print(termo_agua.se_ve_el_liquido())

print(termo_te.llenar("te caliente"))
print(termo_te.servir())
print(termo_te.precintar())
print(termo_te.llevar())
print(termo_te.sostener())
print(termo_te.uso_en_bebidas("calientes y frias"))
print(termo_te.reciclar())
print(termo_te.se_ve_el_liquido())
