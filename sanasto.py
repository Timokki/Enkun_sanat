class Sanasto:

  def __init__(self, olion_nimi):
    self.sanakirja = [("salt", "suola"),("butter", "voi"),("a bowl", "kulho")] # sanakirja muuttuja on self, eli olion oma muuttuja ja se on tyypiltään Dictionary, eli sanakirjatyyppi.
    self.sanakirjan_nimi = olion_nimi
    
  def aseta_uusi_sanapari(self, sana_suomeksi: str, sana_englanniksi: str):
    self.sanakirja.append((sana_englanniksi, sana_suomeksi))

  def tulosta_sanakirja(self):
    for sanapari in self.sanakirja:
      print(sanapari[0], "on suomeksi:", sanapari[1])

  def anna_sanaparit(self):
    return self.sanakirja[:]
  