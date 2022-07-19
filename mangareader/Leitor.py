from kivy.app import App
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout

class Box(BoxLayout):
    def __init__(self,source ='',**kwargs):
        super(Box,self).__init__(**kwargs)
        self.ids.ima.source = source

			
class Leitor(App):
	theme_cls = ThemeManager()
	trans = FadeTransition()
	menu_items = [
	{'viewclass':'MDMenuItem',
          'text':'Help!'}, {'viewclass':'MDMenuItem', 'text': 'Sair'}]
	def acao(self, texto):
		if texto == 'Menu lateral':
			self.root.toggle_nav_drawer()
		if texto == 'Help!':
			pass
		if texto == 'Sair':
			self.stop()
	def fun(self, *args):
		self.root.ids.sm.current = 'punpun'
	def tela1(self, *args):
		self.root.ids.sm.current = 'tela1'
	capitulo = []
	def adicionaEps(self, *args):
		for cap in range(self.capitulo[1]):
			if cap < 10:
				if self.capitulo[1] == 31:
					self.root.ids.ep1.add_widget(Box(source = (self.capitulo[0][0]+ str(cap))+ '.jpg'))
				if self.capitulo[1] == 21:
					self.root.ids.ep2.add_widget(Box(source = (self.capitulo[0][0]+ str(cap))+ '.jpg'))
				
			if cap >= 10:
				if self.capitulo[1] == 31:
					self.root.ids.ep1.add_widget(Box(source = (self.capitulo[0][1]+ str(cap))+'.jpg'))
				if self.capitulo[1] == 21:
					self.root.ids.ep2.add_widget(Box(source = (self.capitulo[0][1]+ str(cap))+'.jpg'))
	def build(self):
		self.capitulo=  [['Cap/000', 'Cap/00'], 31]
		self.adicionaEps()
		self.capitulo =  [['Cap2/000', 'Cap2/00'], 21]
		self.adicionaEps()
		
		
	
Leitor().run()