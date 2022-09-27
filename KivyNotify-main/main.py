from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from plyer import notification
from os.path import join, dirname, realpath
from plyer.utils import platform
from kivy.core.audio import SoundLoader


kv = '''

BoxLayout
	orientation:"vertical"
    Button:
        id:button01
        text: "Noticação 2.4s:Desligada"
        on_release:
            app.on_atualize()
    Button:
        id:button02
        text: "Notificação 20m:Desligada"
        on_release:
            app.on_atualize02()

'''

sound = SoundLoader.load('dis1.mp3')
class EyesClock(App):

    On = True
    On02 = True
    event01 = None
    event02 = None
    

    def on_pause(self):
        return True
    
    def on_resume(self):
        pass
    
    def on_atualize(self):
        
        if(self.On):
            App.get_running_app().root.ids.button01.text = "Noticação 2.4s:Ligada"
            self.On = False
            self.event01 = Clock.schedule_interval(self.on_ac01, 15)
        else:
            App.get_running_app().root.ids.button01.text = "Noticação 2.4s:Desligada"
            self.event01.cancel()
            self.On = True

    def on_atualize02(self):
        if(self.On02):
            App.get_running_app().root.ids.button02.text = "Notificação 20m:Ligada"
            self.On02 = False
            self.event02 = Clock.schedule_interval(self.on_ac02, 1200)
        else:
            App.get_running_app().root.ids.button02.text = "Notificação 20m:Desligada"
            self.event02.cancel()
            self.On02 = True

            

    def on_ac01(self, *args):
        sound.play()        

    def on_ac02(self, *args):
        title = "PiPiPiPi"
        message = "Lembresse de piscar! haha 20m"
        ticker = "ticket"
        kwargs = {'title': title, 'message': message, 'ticker': ticker}
		

        kwargs['app_name'] = "Minhas Notificações"
        kwargs['app_icon'] = join(dirname(realpath(__file__)),
                                          'plyer-icon.ico')
                                          

        notification.notify(**kwargs)
        sound.play()
        
        
    def build(self):
        return Builder.load_string(kv)

EyesClock().run()
