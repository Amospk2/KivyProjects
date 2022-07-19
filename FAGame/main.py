#import
from kivy.core.audio import SoundLoader
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.properties import ListProperty
from kivy.uix.popup import Popup
from random import randint
import json
class G(ScreenManager):
	pass
	
class Contador(Label):
	pass
class Bos(Image):
	pass	
class chao(Image):
	pass
class chao2(Image):
	pass
class chao3(Image):
	pass
	
class Game(Screen):
	sound = SoundLoader.load('sound8bit.mp3')
	sound.play()
	A = 100
	SP = -650 * 1/30
	B = J = vivo = sound.loop = True
	pont = []
	
	with open('Pontuação.json', 'r') as file:
			pont = json.load(file)
	def on_enter(self, *args):
		Clock.schedule_interval(self.update, 1/40)
		Clock.schedule_interval(self.per, 1/40)
		Clock.schedule_interval(self.conte,1)
	def conte(self, *arga):
		if self.vivo:
			self.ids.conta.text = str(int(self.ids.conta.text)+1)
	def per(self, *args):
		if self.ids.bos.x != self.ids.player.x and self.ids.bos.y != self.ids.player.y:
			if self.ids.player.x < self.ids.bos.x:
				self.ids.bos.x -= 3
			if self.ids.player.x > self.ids.bos.x:
				self.ids.bos.x += 3	
			if self.ids.player.y < self.ids.bos.y:
				self.ids.bos.y -= 3
			if self.ids.player.y > self.ids.bos.y:
				self.ids.bos.y += 3
				
			if self.colisao(self.ids.player, self.ids.bos):
				self.confirmacao()
				self.vivo = self.B = self.J = False
				
	def colisao(self, wid1, wid2):
		if wid1.right <= wid2.x:
			return False
		if wid1.x >= wid2.right:
			return False
		if wid1.top <= wid2.y:
			return False
		if wid1.y >= wid2.top:
			return False
		return True
	def update(self, *args):
		if int(self.ids.conta.text) > self.pont[0]:
			self.pont[0] = int(self.ids.conta.text)
			with open('Pontuação.json', 'w') as file:
				json.dump(self.pont, file)
		self.ids.player.speed += self.SP
		self.ids.player.y += self.ids.player.speed * 1/30
		if self.ids.player.y <= self.A:
			self.ids.player.y = self.A
		if self.ids.player.x <= 0:
			self.ids.player.x = 0
		if self.ids.player.x >= 500:
			self.ids.player.x= 500
		if self.ids.player.y >= 915:
			self.ids.player.y = 914
		if self.ids.player.y >= self.ids.chao3.y and self.ids.player.x <= self.ids.chao2.x + 200:
			self.A = 430
			self.SP = -650 * 1/30
		elif self.ids.player.y >= self.ids.chao3.y and self.ids.player.x >= self.ids.chao3.x - 50:
			self.A = 430
			self.SP = -650 * 1/30
		else:
			self.A = 100
			self.SP = -650 * 1/30
		if self.ids.player.y == 430:
			self.ids.player.speed = -15
	def pd(self, *args):
		Clock.schedule_interval(self.pdC, 0.01)
	def pdC(self, *args):
		self.ids.player.x += 4.9
	def pds(self, *args):
		Clock.unschedule(self.pdC)
	def pulo(self):
		if self.J:
			self.ids.player.speed = self.height * 0.55
	def pe(self, *args):
		Clock.schedule_interval(self.peC, 0.01)
	def peC(self, *args):
		self.ids.player.x -= 4.9
	def pes(self, *args):
		Clock.unschedule(self.peC)
	
	def confirmacao(self,*args,**kwargs):
		box = BoxLayout(orientation='vertical',padding=10,spacing=10)
		botoes = BoxLayout(padding=10,spacing=10)
		texto = BoxLayout(spacing=10, padding = 10, orientation = 'vertical')
		pop = Popup(title='   Jogar Novamente?',content=box,size_hint=(None,None),size=(400,300), auto_dismiss=False)
		sim = Button(text='Nao',on_release=App.get_running_app().stop)
		nao = Button(text='Sim',on_release=self.restart, on_press=pop.dismiss)
		text = Label(text='\nSua pontuacao foi {}\nRecord atual:{}\n'.format(self.ids.conta.text, self.pont[0]))
		box.add_widget(texto)
		texto.add_widget(text)
		botoes.add_widget(nao)
		botoes.add_widget(sim)
		box.add_widget(botoes)
		if self.B:
			pop.open()
		return True
	def restart(self, *args):
		self.ids.player.speed = 0
		self.J = self.B = self.vivo = True
		self.ids.player.x = 200
		self.ids.player.y = 800
		self.ids.bos.x = self.ids.bos.y = 0
		self.ids.conta.text = '0'
		

class Player(Image):
	speed = NumericProperty(0)		
		
class main(App):
	def build(self):
		return G()
		
		
main().run()