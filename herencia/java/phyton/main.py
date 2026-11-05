from herencia.java.phyton.personaje import Personaje

heroe = Personaje("Arturo", 1, 100, 100, 25)

orco = Personaje("Orco Feo", 1, 50, 50, 10)

print("Antes del ataque:")
print(heroe)
print(orco)

print("\n--- ¡Arturo ataca al orco! ---")
heroe.atacar(orco)

print("\nDespués del ataque:")
print(orco)