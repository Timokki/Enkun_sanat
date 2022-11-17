from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
#from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import MDList, OneLineAvatarIconListItem, IconLeftWidget
from kivymd.uix.button import MDFillRoundFlatButton

class EtuSivu(MDScreen):
  'Etu Sivu'

class KyselySivu(MDScreen):
  'Etu Sivu'
  def vastaus_validointi(root):
    root.ids["pisteet"].text = "1/3"
    pisteet = 1

class EnksuAppi(MDApp):
  def build(self):
    Builder.load_file("etusivu.kv")
    Builder.load_file("kysely.kv")

    # Create the screen manager
    sm = ScreenManager()
    sm.add_widget(EtuSivu(name='menu'))
    sm.add_widget(KyselySivu(name='kysely'))

    Window.size = [300, 500]

    return sm

EnksuAppi().run()