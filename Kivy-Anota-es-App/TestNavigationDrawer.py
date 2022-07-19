from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.app import App
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.core.window import Window
from kivymd.uix.list import OneLineIconListItem, MDList
import json

KV = '''
#:import MDCard kivymd2.card.MDCard
#:import MDDropdownMenu kivymd.uix.menu.MDDropdownMenu
# Menu item in the DrawerList list.

<ItemDrawer>:
    theme_text_color: "Custom"
    on_release:
    	self.parent.set_color_item(self)
    	app.root.ids.sm.current = str(self.icon)
    	app.root.anim_to_state('closed')
    text_color:[1, 1, 1, 1]

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color:root.text_color

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    canvas:
    	Color:
    		rgba:0.25, 0.25, 0.25, 1
    	Rectangle:
    		pos:self.pos
    		size:self.size
    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/kivy-icon-256.png"

    MDLabel:
        text: "Text01"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
        theme_text_color: "Custom"
        text_color:[1, 1, 1, 1]
    MDLabel:
    	theme_text_color: "Custom"
        text_color:[1, 1, 1, 1]
        text: "Text01"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list


NavigationLayout:
    ContentNavigationDrawer:
    	id: content_drawer
    BoxLayout:
    	orientation: 'vertical'
	    ScreenManager:
	    	id:sm
	        Skreen:
	        	name:'folder'
	        	BoxLayout:
	        		orientation:'vertical'
	        		MDToolbar:
			    		md_bg_color:[0.25, 0.25, 0.25, 1]
			    		title: "Navigation Drawer"
			    		left_action_items: [['menu', lambda x: app.root.toggle_nav_drawer()]]
			    		right_action_items: [['dots-vertical', lambda x:MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)]]
	        		ScrollView:
	        			BoxLayout:
	        				orientation:'vertical'
	        				size_hint_y:None
	        				height:self.minimum_height
	        				id:boxi
	        				Widget:
	        					size_hint_y:None
	        					height:80
	        		Button:
	        			text:'ADD'
	        			size_hint_y:None
	        			height:125
	        			on_release:
	        				root.T = 0
	        				app.popup()
	        Skreen2:
	        	name:'account-multiple'
	        	BoxLayout:
	        		orientation:'vertical'
		        	MDToolbar:
			    		md_bg_color:[0.25, 0.25, 0.25, 1]
			    		title: "Navigation Drawer"
			    		left_action_items: [['arrow-left', lambda x: app.curre('folder')]]
			    		right_action_items: [['dots-vertical', lambda x:MDDropdownMenu(items=app.menu_items, width_mult=4).open(self)]]
		        	BoxLayout:
						padding:30
						orientation:'vertical'
						Botao:
							id:t2lab
							text:'N/A'
							size_hint_y:None
							height:150
						MDSeparator:
							height:dp(1)
						Botao:
							id:t2lab2
							text:'N/A'

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
		height:70
	TextInput:
		id:titu
		size_hint_y:None
		height:150
	Label:
		size_hint_y:None
		height:70
		text:'Texto'
	TextInput:
		id:mensa
	Botao:
		size_hint_y:None
		height:135
		canvas.before:
			Color:
				rgba:0.25, 0.25, 0.25, 1
			Rectangle:
				size:self.size
				pos:self.pos
		on_release:
			app.addday(root.ids.titu.text, root.ids.mensa.text)
		size:root.width, 100
		text:'                                  Adicionar'
		theme_text_color:'Custom'
		text_color:1, 1, 1, 1
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
			Widget:
				size_hint_y:None
				height:1
				canvas:
					Color:
						rgba:0, 0, 0, 1
					Rectangle:
						pos:self.pos
						size:self.size
			BoxLayout:
				Botao:
					id:lab2
					on_release:
						app.root.ids.sm.transition.direction = 'left'
						app.change(root.ids.lab.text, root.ids.lab2.text)


<Botao@ButtonBehavior+MDLabel>:
	canvas.before:
		Color:
			rgba:1, 1, 1, 1
		Rectangle:
			pos:self.pos
			size:self.size

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


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = [1, 1, 1, 1]
                break
        instance_item.text_color = self.theme_cls.primary_color
from kivy.uix.screenmanager import Screen
class Skreen2(Screen):
	def on_pre_enter(self, *kwargs):
		Window.bind(on_keyboard=self.voltar)
	def voltar(self,window,key,*args):
		if key == 27:
			App.get_running_app().curre('folder')
			return True
	def on_pre_leave(self, *args):
		Window.unbind(on_keyboard=self.voltar)
class Skreen(Screen):
	T = 0
	def on_pre_enter(self, *kwargs):
		Window.bind(on_keyboard=self.voltar)
	def voltar(self,window,key,*args):
		if key == 27:
			if self.T == 0:
				App.get_running_app().pop.dismiss()
				self.T = 1
				return True
			elif self.T == 1:
				App.get_running_app().stop()
				return True
	def on_pre_leave(self, *args):
		Window.unbind(on_keyboard=self.voltar)
class TestNavigationDrawer(MDApp):
	def build(self):
		return Builder.load_string(KV)
	pop = None
	def curre(self, tela, *args):
		self.root.ids.sm.current = str(tela)
		self.root.ids.sm.transition.direction = 'right'
	def popup(self, *args):
		self.pop = Popup(title = '         Adicione item:', content=Box(),size_hint=(None,None),size=(self.root.size), auto_dismiss=False)
		self.pop.open()
	def addday(self, titulo, mensagem, *args):
		self.Dias[titulo] = mensagem
		with open('dias.json', 'w') as dia:
			json.dump(self.Dias, dia)
		self.root.ids.boxi.add_widget(Dia(mensagem, titulo))
		self.pop.dismiss()
	def put(self, titu, *args):
		self.Dias.pop(titu)
		with open('dias.json', 'w') as dia:
			json.dump(self.Dias, dia)
	def change(self, titu, mensa,*args):
		self.root.ids.sm.current = "account-multiple"
		self.root.ids.t2lab.text =str('          ' + titu)
		self.root.ids.t2lab2.text = str('     ' +mensa)
	Dias = Dya = {}
	with open('dias.json', 'r') as file:
		Dya = Dias = json.load(file)
	def add(self, *args):
		for D in self.Dya:
			self.root.ids.boxi.add_widget(Dia(self.Dya[D], D))
			self.Dya = {}
	from kivy.properties import ListProperty
	menu_items = ListProperty()
	def callback_for_menu_items(self, *args):
		self.root.toggle_nav_drawer()
	def callback_for_menu_items2(self, *args):
		pass
	def callback_for_menu_items3(self, *args):
		self.stop()
	menu_items = []
	def on_start(self):
		self.menu_items = [{
                "viewclass": "MDMenuItem",
                "text": 'Menu Lateral', 'callback':self.callback_for_menu_items}, {
                "viewclass": "MDMenuItem",
                "text": 'Help', 'callback':self.callback_for_menu_items2}, {
                "viewclass": "MDMenuItem",
                "text": 'Sair', 'callback':self.callback_for_menu_items3}]
		self.add()
		icons_item = {
            "folder": "Itens",
            "account-multiple": "Conteudo"
    	}
		for icon_name in icons_item.keys():
			self.root.ids.content_drawer.ids.md_list.add_widget(ItemDrawer(icon=icon_name, text=icons_item[icon_name]))

TestNavigationDrawer().run()