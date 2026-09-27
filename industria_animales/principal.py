from animal import Animal
from caballo import Caballo
from cocodrilo import Cocodrilo
from pez import Pez
from escarabajo import Escarabajo
from pato import Pato

obj_caballo = Caballo("Tordillo", 5, "grande", "marron")
obj_cocodrilo = Cocodrilo("Cocodrilo", 8, "grande", "verde oscuro")
obj_pez = Pez("Pez payaso", 2, "pequeno", "rayado naranja")
obj_escarabajo = Escarabajo("Escarabajo rinoceronte", 1, "pequeno", "negro brillante")
obj_pato = Pato("Pato", 3, "mediano", "blanco")

print(obj_caballo.moverse())
print(obj_caballo.comunicacion())
print(obj_caballo.reproduccion())
print(obj_caballo.alimentarse())
print(obj_caballo.adaptacion())
print(obj_caballo.instintos())
print(obj_caballo.descanso())
print(obj_caballo.sueno())
print(obj_caballo.interaccion_social())

print(obj_cocodrilo.moverse())
print(obj_cocodrilo.adaptacion())

print(obj_pez.moverse())
print(obj_pez.adaptacion())

print(obj_escarabajo.moverse())
print(obj_escarabajo.instintos())

print(obj_pato.moverse())
print(obj_pato.comunicacion())
