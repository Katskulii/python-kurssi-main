from collections import OrderedDict
# Tehdään kokoelma, johon talletetaan 10  auton rekisterinumeot ja merkit. Tulostetaan sitten autot aakkosjärjestyksessä merkin mukaan sekä rek.numeron mukaan.
autot = {
    "Mersu": "ABC-123",
    "Bemari": "ALS-256",
    "Sitikka": "ÖKK-789",
    "Rover": "YRS-122",
    "Ferrari": "AÄK-356",
    "Maserati": "JHK-346",
    "Toyota": "LJH-389",
    "Ford": "UTR-087",
    "Audi": "SRH-347",
    "Cupra": "DHT-568"
}

autot1 = OrderedDict(sorted(autot.items()))
print(autot1)

uusi = sorted(autot.items(), key = lambda x:x[1])
jarkatyt = dict(uusi)
print(jarkatyt)
    