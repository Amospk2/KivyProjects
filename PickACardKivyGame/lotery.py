#All is in Portuguese. Sorry guys. Tudo em português.
#Esse projeto não tem intuito ser profissional, é apenas uma projeto de entreterimento
#Aqui, tentei reimaginar o " Pick a Card" com o Kivy
#alguns erros como o de responsividade em diferentes telas e etc não foram levados em consideração no desenvolvimento
#É extremamente proibido a venda deste produto.


from kivy.app import App
from random import choice
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock

#Inicio do codico, usamos o Builder do Kivy para construir a screen principal do projeto

Kv = '''
Screen:
    BoxLayout:
        orientation:"vertical"
        canvas:
            Color:
                rgba:0.234, 0.545, 0.887, 1
            Rectangle:
                pos:self.pos
                size:self.size


        BoxLayout:
            size_hint_y:None
            height:30
            canvas:
                Color:
                    rgba:1, 0.325, 0, 1
                Rectangle:
                    pos:self.pos
                    size:self.size
            Label:
                id:ponto
                text: "Você tem: 3 pontos"
                color:0, 0, 0, 1


        BoxLayout:
            BoxLayout:
                padding:10
                orientation:"vertical"
                id:ward
                BoxLayout:
                    size_hint_y:None
                    height:40
                    canvas:
                        Color:
                            rgba:1, 1, 1, 1
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:    
                        text: "Primeiro Quadro"
                        size_hint_y:None
                        height:40
                        color:0, 0, 0, 1
                        font_size:15
                    
                Botao:
                    id:One
                    text:"Click"
                    on_press:app.click(1)


            BoxLayout:
                padding:10
                orientation:"vertical"
                id:wardtwo
                    
                BoxLayout:
                    size_hint_y:None
                    height:40
                    canvas:
                        Color:
                            rgba:1, 1, 1, 1
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:    
                        text: "Segundo Quadro"
                        size_hint_y:None
                        height:40
                        color:0, 0, 0, 1
                        font_size:15
                    
                    
                Botao:
                    id:Two
                    text:"Click"
                    on_press:app.click(2)
                    font_size:15


            BoxLayout:
                padding:10
                id:wardthree
                orientation:"vertical"

                BoxLayout:
                    size_hint_y:None
                    height:40
                    canvas:
                        Color:
                            rgba:1, 1, 1, 1
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:    
                        text: "Terceiro Quadro"
                        size_hint_y:None
                        height:40
                        color:0, 0, 0, 1
                        font_size:15
                    
                    
                Botao:
                    id:Three
                    text:"Click"
                    on_press:app.click(3)
                    font_size:15

        BoxLayout:
            BoxLayout:
                padding:10
                id:wardfour
                orientation:"vertical"

                    
                BoxLayout:
                    size_hint_y:None
                    height:40
                    canvas:
                        Color:
                            rgba:1, 1, 1, 1
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:    
                        text: "Quarto Quadro"
                        size_hint_y:None
                        height:40
                        color:0, 0, 0, 1
                        font_size:15
                    
                Botao:
                    text:"Click"
                    id:Four
                    on_press:app.click(4)
                    font_size:15


            BoxLayout:
                padding:10
                orientation:"vertical"
                id:wardfive
                    
                BoxLayout:
                    size_hint_y:None
                    height:40
                    canvas:
                        Color:
                            rgba:1, 1, 1, 1
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:    
                        text: "Quinto Quadro"
                        size_hint_y:None
                        height:40
                        color:0, 0, 0, 1
                        font_size:15
                    
                Botao:
                    text:"Click"
                    id:Five
                    on_press:app.click(5)
                    font_size:15


            BoxLayout:
                padding:10
                id:wardsix
                orientation:"vertical"

                    
                BoxLayout:
                    size_hint_y:None
                    height:40
                    canvas:
                        Color:
                            rgba:1, 1, 1, 1
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:    
                        text: "Sexto Quadro"
                        size_hint_y:None
                        height:40
                        color:0, 0, 0, 1
                        font_size:15
                    
                Botao:
                    id:Six
                    text:"Click"
                    on_press:app.click(6)
                    font_size:15


        BoxLayout:
            BoxLayout:
                padding:10
                id:wardseven
                orientation:"vertical"
                BoxLayout:
                    size_hint_y:None
                    height:40
                    canvas:
                        Color:
                            rgba:1, 1, 1, 1
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:    
                        text: "Setimo Quadro"
                        size_hint_y:None
                        height:40
                        color:0, 0, 0, 1
                        font_size:15
                    
                Botao:
                    id:Seven
                    text:"Click"
                    on_press:app.click(7)
                    font_size:15


            BoxLayout:
                padding:10
                id:wardeight
                orientation:"vertical"
                    
                BoxLayout:
                    size_hint_y:None
                    height:40
                    canvas:
                        Color:
                            rgba:1, 1, 1, 1
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:    
                        text: "Oitavo Quadro"
                        size_hint_y:None
                        height:40
                        color:0, 0, 0, 1
                        font_size:15
                    
                Botao:
                    id:Eight
                    text:"Click"
                    on_press:app.click(8)
                    font_size:15


            BoxLayout:
                padding:10
                id:wardnine
                orientation:"vertical"
                    
                BoxLayout:
                    size_hint_y:None
                    height:40
                    canvas:
                        Color:
                            rgba:1, 1, 1, 1
                        Rectangle:
                            pos:self.pos
                            size:self.size
                    Label:    
                        text: "Nine Quadro"
                        size_hint_y:None
                        height:40
                        color:0, 0, 0, 1
                        font_size:15
                    
                Botao:
                    id:Nine
                    text:"Click"
                    on_press:app.click(9)
                    font_size:15









        BoxLayout:
            padding:5
            canvas:
                Color:
                    rgba:1, 0, 0, 1
                Rectangle:
                    pos:self.pos
                    size:self.size
            size_hint_y:None
            height:80
            Botao:
                text:"Restart"
                on_press:app.restartOn()
            Widget:
                size_hint_x:None
                width:10
            Botao:
                on_press:app.sair()
                text:"Quit"
    


<Botao@ButtonBehavior+Label>:
	canvas.before:
		Color:
			rgba:0, 0, 0, 0.4
		Rectangle:
			pos:self.pos
			size:self.size
'''

#A estrutura do design é simples, usamos um BoxLayout que contem um button e outro boxlayout com um label
#Este label serve para dar nome a cada quadrinho e o button é o "quadro" onde aparece as respostas
# ao final de cada rodada 




class teste(App):
    pontos = 3
    ListFalse = ListTrue = []
    def redfine(self):
        
        self.ListFalse = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.ListTrue = []
    def build(self):
        return Builder.load_string(Kv)
    
    def GValues(self):
        self.redfine()
        for itens in range(3):
            Value = choice(self.ListFalse)
            self.ListFalse.remove(Value)
            self.ListTrue.append(Value)
        self.truevalues()
        self.falsevalues()
    
#A função Gvalues sorteia 3 valores como os "verdadeiros" - que são adicionados a uma lista de "verdadeiros"
# e o restante vai para outra lista de "falsos"

    def truevalues(self):
        for item in self.ListTrue:
            if item == self.quemchamou:
                self.pontos += 1
                Clock.schedule_once(lambda dt:self.mudapontos("Você tem:"+str(self.pontos)+" pontos"), 2)
                if self.pontos == 0:
                    self.fim = 0
            if item == 1:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.One), 0.5)
                Clock.schedule_once(lambda dt:self.pintaverdeK(App.get_running_app().root.ids.One), 1)
            if item == 2:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Two), 0.5)
                Clock.schedule_once(lambda dt:self.pintaverdeK(App.get_running_app().root.ids.Two), 1)
            if item == 3:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Three), 0.5)
                Clock.schedule_once(lambda dt:self.pintaverdeK(App.get_running_app().root.ids.Three), 1)
            if item == 4:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Four), 0.5)
                Clock.schedule_once(lambda dt:self.pintaverdeK(App.get_running_app().root.ids.Four), 1)
            if item == 5:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Five), 0.5)
                Clock.schedule_once(lambda dt:self.pintaverdeK(App.get_running_app().root.ids.Five), 1)
            if item == 6:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Six), 0.5)
                Clock.schedule_once(lambda dt:self.pintaverdeK(App.get_running_app().root.ids.Six), 1)
            if item == 7:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Seven), 0.5)
                Clock.schedule_once(lambda dt:self.pintaverdeK(App.get_running_app().root.ids.Seven), 1)
            if item == 8:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Eight), 0.5)
                Clock.schedule_once(lambda dt:self.pintaverdeK(App.get_running_app().root.ids.Eight), 1)
            if item == 9:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Nine), 0.5)
                Clock.schedule_once(lambda dt:self.pintaverdeK(App.get_running_app().root.ids.Nine), 1)

#Na função Truevalues definimos quem chamou e caso ele forum dos verdadeiros ele ganha +1 ponto
# no placar       
    def falsevalues(self):
        for item in self.ListFalse:

            if item == self.quemchamou:
                self.pontos -= 1
                Clock.schedule_once(lambda dt:self.mudapontos("Você tem:"+str(self.pontos)+" pontos"), 1)
                if self.pontos == 0:
                    self.fim = 0
            if item == 1:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.One), 0.5)
                Clock.schedule_once(lambda dt:self.pintavermelhoK(App.get_running_app().root.ids.One), 1)

            if item == 2:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Two), 0.5)
                Clock.schedule_once(lambda dt:self.pintavermelhoK(App.get_running_app().root.ids.Two), 1)
            if item == 3:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Three), 0.5)
                Clock.schedule_once(lambda dt:self.pintavermelhoK(App.get_running_app().root.ids.Three), 1)
            if item == 4:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Four), 0.5)
                Clock.schedule_once(lambda dt:self.pintavermelhoK(App.get_running_app().root.ids.Four), 1)
            if item == 5:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Five), 0.5)
                Clock.schedule_once(lambda dt:self.pintavermelhoK(App.get_running_app().root.ids.Five), 1)
            if item == 6:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Six), 0.5)
                Clock.schedule_once(lambda dt:self.pintavermelhoK(App.get_running_app().root.ids.Six), 1)
            if item == 7:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Seven), 0.5)
                Clock.schedule_once(lambda dt:self.pintavermelhoK(App.get_running_app().root.ids.Seven), 1)
            if item == 8:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Eight), 0.5)
                Clock.schedule_once(lambda dt:self.pintavermelhoK(App.get_running_app().root.ids.Eight), 1)
            if item == 9:
                Clock.schedule_once(lambda dt: self.delay(App.get_running_app().root.ids.Nine), 0.5)
                Clock.schedule_once(lambda dt:self.pintavermelhoK(App.get_running_app().root.ids.Nine), 1)

#Na FalseValues identificamos quem chamou e caso ele for falso tiramos -1 ponto dele
    def mudapontos(self, text):
        App.get_running_app().root.ids.ponto.text = text
    def delay(self, Nmbr):
        Nmbr.text="    Wait a moment    "

    def pintavermelhoK(self, Nmbr):
        Nmbr.text="    Você Errou! \n    Os numeros\n    errados eram:\n    " + str(self.ListFalse)
        Nmbr.canvas.before.clear()
        with Nmbr.canvas.before:
            Color(rgba=(1, 0, 0, 0.8))
            Rectangle(pos=(Nmbr.pos), size=(Nmbr.size))
    
    def pintaverdeK(self, Nmbr):
        Nmbr.text="    Você acertou! \n    Os numeros\n    certos eram:\n    "+ str(self.ListTrue)
        Nmbr.canvas.before.clear()
        with Nmbr.canvas.before:
            Color(rgba=(0, 1, 0, 0.8))
            Rectangle(pos=(Nmbr.pos), size=(Nmbr.size))
    vz = fim = 1
    quemchamou = None


#Mudapontos irá adicionar ou retirar os pontos
#Delay é apenas para haver um tempo até relevar o resultado
#Pintaverde e pintavermelho iŕa mudar as cores de cada carta de acordo com o resultado

    def click(self, qc,*Args):
        self.quemchamou = qc
        if self.vz == 1:
            self.GValues()
            self.vz = 0
        else:
            pass
    def restartOn(self):
        if self.fim == 1:
            self.vz=1
            App.get_running_app().root.ids.One.text = App.get_running_app().root.ids.Two.text = App.get_running_app().root.ids.Three.text = App.get_running_app().root.ids.Four.text = App.get_running_app().root.ids.Five.text = App.get_running_app().root.ids.Six.text = App.get_running_app().root.ids.Seven.text = App.get_running_app().root.ids.Eight.text = App.get_running_app().root.ids.Nine.text ="Click Here"
            self.pintacinzaK([App.get_running_app().root.ids.One, App.get_running_app().root.ids.Two, App.get_running_app().root.ids.Three, App.get_running_app().root.ids.Four, App.get_running_app().root.ids.Five, App.get_running_app().root.ids.Six, App.get_running_app().root.ids.Seven, App.get_running_app().root.ids.Eight, App.get_running_app().root.ids.Nine])
        else:
            App.get_running_app().root.ids.ponto.text = "Você zerou seus pontos!"
    
    def pintacinzaK(self, NmbrL):
        for Nmbr in NmbrL:
            Nmbr.canvas.before.clear()
            with Nmbr.canvas.before:
                Color(rgba=(0, 0, 0, 0.4))
                Rectangle(pos=(Nmbr.pos), size=(Nmbr.size))
    def sair(self):
        self.get_running_app().stop()

#Click é quem recebe o QC=quemchamou, e iniciará o processo de loteria
#RestartOn ira iniciar o processo de reinicio de jogo, retornando tudo ao 0
#PintaCinza é a função que torna as cartas como as do inicio do jogo
#Sair função que termina o jogo

teste().run()
