from kivy.app import App
from kivymd.theming import ThemeManager
from kivymd.snackbar import Snackbar
from kivy.uix.screenmanager import FadeTransition, Screen
from kivy.uix.boxlayout import BoxLayout
from firebase import firebase
class Mensagem(BoxLayout):
	def __init__(self,texto = '',heig = 80, **kwargs):
		super().__init__(**kwargs)
		self.ids.lab.text = texto
		self.height = heig
		
class Mensagem2(BoxLayout):
	def __init__(self,texto = '',heig = 80, use = '', **kwargs):
		super().__init__(**kwargs)
		self.ids.lab.text = texto
		self.height = heig
		self.ids.us.text = use + ':'

global firebase	
from kivy.clock import Clock	
class Skreen(Screen):
	pass
class ChatKivy(App):
	def check_host(*args):
		import socket
		confiaveis = ['www.google.com', 'www.youtube.com.br', 'https://firebase.google.com/?hl=pt-br']
		for host in confiaveis:
			a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			a.settimeout(.5)
			try:
				b=a.connect_ex((host, 80))
				if b==0: #ok, conectado
					return True
			except:
				pass
			a.close()
		return False

	conect = check_host()
	Snackbar(text="Conectando..").show()
	if conect:
		global firebase
		firebase = firebase.FirebaseApplication("https://primeirotest-fb6c0.firebaseio.com/", None)
		Snackbar(text="Conectado.").show()
		mensa = firebase.get('/msg','')
	else:
		Snackbar(text="Verifique sua conexão.").show()
		mensa = {'ola':'crack'}
	f = 1
	def sinc(self):
		if self.f == 1:
			self.f -= 1
			for a in self.mensa:
				self.root.ids.box.add_widget(Mensagem2(texto = a[1], heig = 120, use = a[0]))
		else:
			global firebase
			novamen = firebase.get('/msg','')
			if len(novamen) > len(self.mensa):
				for v in novamen:
					if v in self.mensa:
						pass
					else:
						if v[0] != self.user:
							self.root.ids.box.add_widget(Mensagem2(texto = v[1], heig = 120, use = v[0]))
						else:
							pass
				self.mensa = novamen

	user = ''
	Se = None
	def aute(self, *args):
		self.Se = self
		self.user = self.root.ids.ti.text
		self.root.ids.sm.current = 'S1'
	trans = FadeTransition()
	theme_cls = ThemeManager()
	menu_items = [
	{'viewclass':'MDMenuItem',
          'text':'Help!'}, {'viewclass':'MDMenuItem', 'text': 'Sair'}]
	a = True
	def focus(self, *args):
		if self.a:
			self.root.ids.bi.height = 450
			self.root.ids.wi.height = 377
			self.a = False
		elif self.a == False:
			self.root.ids.bi. height= 80
			self.root.ids.wi.height = 0
			self.a = True
			
			
	def texto(self, *args):
		heigh = 110
		texto = self.root.ids.TI.text
		texto2 = ''
		O = [30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510]
		for a in texto:
			if len(texto2) in O:
				texto2 += '\n'
				heigh += 15
			texto2 += a
		self.root.ids.TI.text = ''
		self.root.ids.box.add_widget(Mensagem(texto = texto2, heig = heigh))
		data = [self.user, texto2]
		a = firebase.get('/msg','')
		a.append(data)
		data = []
		firebase.put('/msg', '/', a)	
       
	def acao(self, texto):
		if texto == 'Menu lateral':
			self.root.toggle_nav_drawer()
		if texto == 'Help!':
			self.root.ids.sm.current = 'SH'
		if texto == 'Sair':
			self.stop()
ChatKivy().run()