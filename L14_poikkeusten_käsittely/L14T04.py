from operator import index

# Tehdään lista lauseita.
lauseet = ["Minäpä tässä kirjoittelen.", "Jotakin vaan mitä mieleen tulee.", "Olisihan se hyvä, että ajatus kulkee.", "Ja, jos ei kulje, niin tulee hölynpölyä.", "Ei kai sekään haittaa."]
print(lauseet)

for lause in lauseet:
    try:    
        ind = int(input("Mikä indeksi muutetaan? 0,1,2,3,4?: "))
        if ind == [0] or [1] or [2] or [3] or [4]:
            lause = lauseet
            lause[ind] = input("Uusi lause on : ")
        print(lauseet)
        break
    except:
        print("Annoit indeksin, jota ei ole olemassa! Yritä uudelleen.")