from sanasto import Sanasto

# alla määritellään def komennolla funktio jonka nimi on tulosta valikko
def tulosta_valikko():
    print("\n  EEMILIN SANAPELI\n")
    print("  1 harjoittele sanoja englanti -> suomi")
    print("  2 harjoittele sanoja suomi -> englanti")
    print("  3 syötä sanoja sanakirjaan")
    print("  4 Tulosta testisanasto.")
    print("  0 Poistu ohjelmasta\n")

def kysy_englanniksi(sanasto):
    for sanapari in sanasto.anna_sanaparit():
        vastaus = input(f"{sanapari[0]} = ")
        if vastaus == sanapari[1]:
            print("oikein")

def syota_sanoja(sanasto: list):
    while True:
        print("jos et anna sanoja palataan päävalikkoon")
        sana_suomeksi = input("Anna sana suomeksi: ")
        if sana_suomeksi == "":
            break
        sana_englanniksi = input(f"Anna {sana_suomeksi} sana englanniksi: ")

        sanasto.aseta_uusi_sanapari(sana_englanniksi, sana_suomeksi)

    #return (sanat_suomeksi, sanat_englanniksi)

if __name__ == "__main__": 
    kaikki_sanastot = []
    sanasto1 = Sanasto("Testisanasto")

    while True:
        tulosta_valikko() # tässä kutsutaan funktiota tulosta valikko
        komento = input("  anna komento: ")

        if komento == "0":
            print("Ohjelma sulkeutuu! Heippa!")
            break # break on komento jolla keskeytetään silmukka
        elif komento == "1":
            kysy_englanniksi(sanasto1)
        elif komento == "3":
            syota_sanoja(sanasto1)
        elif komento == "4":
            sanasto1.tulosta_sanakirja()