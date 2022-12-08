# Pyydetään käyttäjältä sukunimiä ja tallennetaan ne tiedostoon.

tiedostonimi = "Sukunimet.txt"
tiedosto = open(tiedostonimi, "w")
sukunimi = "*"
while sukunimi != "":
    sukunimi = input("Anna henkilön sukunimi, enter lopettaa ")
    if sukunimi != "":
        tiedosto.write(sukunimi + "\n")
tiedosto.close

# Tehdään ohjelma, jolla avataan luotu kansio luettavaksi ja tulostetaan annetut sukunimet riveittäin konsoliin.
dump = input("Paina enter jatkaaksesi.")

tiedosto = open(tiedostonimi, "r")
jep = input("Tiedostoon kirjoitettiin seuraavat nimet(paina enter): ")
rivit = tiedosto.read()
print(rivit)
tiedosto.close()
print("tehtävä suoritettu onnistuneesti.")