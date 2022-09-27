from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.theming import ThemeManager
from kivy.uix.screenmanager import Screen, WipeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.screenmanager import Screen, ScreenManager
import webbrowser
KV = '''

<Botao@ButtonBehavior+MDLabel>:
	canvas.before:
		Color:
			rgba:1, 1, 1, 1
		Rectangle:
			pos:self.pos
			size:self.size


<Dia>:
	size_hint_y:None
	height:400
	id:box
	MDCard:
		size_hint: None, None
		size:root.size
		pos_hint: {'center_x': 0.5, 'center_y': 0.7}
		BoxLayout:
			orientation:'vertical'
			padding: dp(8)
			BoxLayout:
				size_hint_y:None
				height:50
				MDLabel:
					id:lab
					text:
				Botao:
					size_hint_x:None
					width:55
					text:'    X'
					on_release:
						app.root.ids.boxi.remove_widget(root)
						app.put(root.ids.lab.text)
					canvas.before:
						Color:
							rgba:1, 0, 0, 1
						Rectangle:
							pos:self.pos
							size:self.size
			MDSeparator:
				height:dp(1)
			BoxLayout:
				Botao:
					id:lab2
					on_release:
						app.root.ids.sm.transition.direction = 'left'
						app.change(root.ids.lab.text, root.ids.lab2.text)
<Box>:
	orientation:'vertical'
	canvas:
		Color:
			rgba:0.13, 0.26, 0.36, 1
		Rectangle:
			size:self.size
			pos:self.pos
	Label:
		text:'Titulo'
		size_hint_y:None
		height:40
	TextInput:
		id:titu
		size_hint_y:None
		height:50
	Label:
		size_hint_y:None
		height:70
		text:'Texto'
	TextInput:
		id:mensa
	Button:
		size_hint:None, None
		on_release:
			app.addday(root.ids.titu.text, root.ids.mensa.text)
		size:root.width, 75
		text:'Adicionar'





# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height
		Image:
			id: avatar
			size_hint: None, None
			size: "300dp", "256dp"
			source: "painel.jpg"
        
    MDLabel:
        text: "SensivyDays"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:
		MDList:
			id: md_list
			OneLineIconListItem:
				text:"Pagina Inicial"
				on_press:
					app.root.ids.nav_drawer.set_state("close")
					app.root.ids.sm.current = "Tela01"
				IconLeftWidget:
					icon:'home'
			OneLineIconListItem:
				text:"Suporte/Contato"
				on_press:
					app.root.ids.nav_drawer.set_state("close")
					app.root.ids.sm.current = "Tela03"
				IconLeftWidget:
					icon:'share'
			OneLineIconListItem:
				text:"Fechar Aplicativo"
				on_press:
					app.stop()
				IconLeftWidget:
					icon:'close'
			
			
				



Screen:

    NavigationLayout:
		id:nav_drawer
        ScreenManager:
            id:sm
            Screen:
                name:"Tela01"
                orientation:'vertical'
                
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "SensivyDays"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
						
                
                    BoxLayout:
                        orientation:'vertical'
                        ScrollView:
						    BoxLayout:
							    id:boxi
							    orientation:'vertical'
							    size_hint_y:None
							    height:self.minimum_height
							    Widget:
								    size_hint_y:None
								    height:75
						Button:
							text: "Click aqui para adicionar textos"
							size_hint_y:None
							height:75
							on_release:app.popup()
						    
            Screen:
			    name:'Tela02'
			    BoxLayout:
				    orientation:'vertical'
					MDToolbar:
                        title: "SensivyDays"
                        elevation: 10
                        left_action_items: [['arrow-left', lambda x: app.mude("Tela01")]]
				    BoxLayout:
					    padding:30
					    orientation:'vertical'
					    Botao:
						    id:t2lab
						    text:
						    size_hint_y:None
						    height:150
					    MDSeparator:
						    height:dp(1)
					    Botao:
						    id:t2lab2
						    text:
			Screen:
				name:"Tela03"
				BoxLayout:
					orientation:"vertical"
					MDToolbar:
                        title: "SensivyDays"
                        elevation: 10
                        left_action_items: [['arrow-left', lambda x: app.mude("Tela01")]]
					BoxLayout:
						orientation:"vertical"
						ThreeLineAvatarListItem:
							on_release:app.link()
							text:"Github"
							secondary_text:"Esse é um projeto desenvolvido com intuito de testar conceitos e construir um App"
							tertiary_text:"testando as novas funcionalidade do KivyMD. Acesse o Github deste projeto clicando aqui."
							IconLeftWidget:
								icon: "share"
							
						Widget:
						


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
'''

class Dia(BoxLayout):
	def __init__(self,texto = '', titulo = '', **kwargs):
		super().__init__(**kwargs)
		self.ids.lab.text = titulo
		self.ids.lab2.text = texto
    
class Box(BoxLayout):
	titu = mensa = ''
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.titu = self.ids.titu.text
		self.mensa = self.ids.mensa.text

class ContentNavigationDrawer(BoxLayout):
    pass



class SensivyDays(MDApp):
	Dias = {}
	def build(self):
		return Builder.load_string(KV)
	def mude(self, sn):
		MDApp.get_running_app().root.ids.sm.current = sn
	def popup(self, *args):
		self.pop = Popup(title= 'Adicione seu dia:', content=Box(),size_hint=(None, None), size=(self.root.size), auto_dismiss=False)
		self.pop.open()
	def addday(self, titulo, mensagem, *args):
		self.Dias[titulo] = mensagem
		
		self.root.ids.boxi.add_widget(Dia(mensagem, titulo))
		self.pop.dismiss()
	def change(self, titu, mensa,*args):
		self.root.ids.sm.current = 'Tela02'
		self.root.ids.t2lab.text =str('          ' + titu)
		self.root.ids.t2lab2.text = str('     ' +mensa)
	def put(self, titu, *args):
		self.Dias.pop(titu)
	def link(self):
		url = 'https://github.com/Amospk2/SensivyDays/'
		webbrowser.open(url, new=0, autoraise=True)

SensivyDays().run()
