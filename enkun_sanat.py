# alla määritellään def komennolla funktio jonka nimi on tulosta valikko
def tulosta_valikko():
    print("\n  EEMILIN SANAPELI\n")
    print("  1 harjoittele sanoja englanniksi")
    print("  2 harjoittele kirjoittamaan sanoja englanniksi")
    print("  3 syötä sanoja sanakirjaan")
    print("  0 poistu ohjelmasta\n")

def syota_sanoja():
    while True:
        print("jos et anna sanoja palataan päävalikkoon")
        sana_suomeksi = input("Anna sana suomeksi: ")
        if sana_suomeksi == "":
            break
        sana_englanniksi = input(f"Anna {sana_suomeksi} sana englanniksi: ")

        sanat_suomeksi = {sana_suomeksi: sana_englanniksi}
        sanat_englanniksi = {sana_englanniksi: sana_suomeksi}

    return (sanat_suomeksi, sanat_englanniksi)

if __name__ == "__main__":
    
    while True:
        tulosta_valikko() # tässä kutsutaan funktiota tulosta valikko
        komento = input("  anna komento: ")

        if komento == "0":
            print("Ohjelma sulkeutuu! Heippa!")
            break # break on komento jolla keskeytetään silmukka
        elif komento == "3":
            syota_sanoja()