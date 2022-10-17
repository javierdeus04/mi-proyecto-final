from ejemplo.models import Familiar

Familiar(nombre="Carol", direccion="Av. Libertador 6322", numero_pasaporte=123456).save()
Familiar(nombre="Lorena", direccion="Av. 18 de Julio 2164", numero_pasaporte=23532542).save()
Familiar(nombre="Sebastian", direccion="Morquio 536", numero_pasaporte=23523).save()
Familiar(nombre="Facundo", direccion="Colon  318", numero_pasaporte=23532532).save()

print("Se cargo con éxito los usuarios de pruebas")