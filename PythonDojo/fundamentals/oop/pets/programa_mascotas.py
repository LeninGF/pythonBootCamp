from mascota.mascotas import Mascota
from ninja.personas import Ninja

gata_fifi = Mascota(nombre='FIFI', tipo='Gato', golosinas='atún', sonido='eeee')
ninja_silvi = Ninja(nombre='Silvana', apellido='Arevalo', mascotas=gata_fifi, premio='oreo', comida_mascotas='Pizza')

print(f"Estado inicial mascota: {gata_fifi.estado()}")
ninja_silvi.alimentar()
ninja_silvi.bañar()
ninja_silvi.caminar()
print(f"Estado final mascota: {gata_fifi.estado()}")
