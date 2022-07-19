from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.lang import Builder
Kv = '''
#:import MDDropdownMenu kivymd.uix.menu.MDDropdownMenu
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
        text: "NavigationTest"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
        theme_text_color: "Custom"
        text_color:[1, 1, 1, 1]
    MDLabel:
    	theme_text_color: "Custom"
        text_color:[1, 1, 1, 1]
        text:'NavigationTest'
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
    	orientation:'vertical'
    	MDToolbar:
    		title:'KivyTest'
    		md_bg_color:0.25, 0.25, 0.25, 1
    		left_action_items:[['menu', lambda x:app.root.toggle_nav_drawer()]]
    		right_action_items: [['dots-vertical', lambda x:MDDropdownMenu(items=app.menu_items, width_mult=3).open(self)]]
    	ScreenManager:
    		id:sm
    		Screen:
    			name:'folder'
    			BoxLayout:
    				orientation:'vertical'
    				Widget:
    					canvas:
    						Color:
    							rgba:0.987, 0.654, 0.321, 1
    						Rectangle:
    							pos:self.pos
    							size:self.size
    		Screen:
    			name:'account-multiple'
    			BoxLayout:
    				orientation:'vertical'
    				Widget:
    					canvas:
    						Color:
    							rgba:0.123, 0.456, 0.789, 1
    						Rectangle:
    							pos:self.pos
    							size:self.size
'''
class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = [1, 1, 1, 1]
                break
        instance_item.text_color = self.theme_cls.primary_color
        
class NewND(MDApp):
	def build(self):
		return Builder.load_string(Kv)
	def callback1(self, *args):
		pass
	def callback2(self, *args):
		MDApp.get_running_app().stop()
	menu_items = []
	def on_start(self):
		self.menu_items = [{'viewclass':'MDMenuItem', 'text':'Help', 'callback':self.callback1}, {'viewclass':'MDMenuItem', 'text':'Sair', 'callback':self.callback2}]
		icons_item = {
            "folder": "Arquivos",
            "account-multiple": "Info."
    	}
		for icon_name in icons_item.keys():
			self.root.ids.content_drawer.ids.md_list.add_widget(ItemDrawer(icon=icon_name, text=icons_item[icon_name]))

NewND().run()