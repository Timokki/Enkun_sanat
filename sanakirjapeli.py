from sanasto import Sanasto

class SanakirjaPeli:
  def __init__(self):
    self.sanasto1 = Sanasto("Testisanasto")

  def anna_sanapari(self):
    luku = 0
    sanaparit = self.sanasto1.anna_sanaparit()
    while luku < len(sanaparit):
      yield sanaparit[luku]
      luku += 1