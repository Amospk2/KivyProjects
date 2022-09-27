
from kivy.app import App
from random import choice
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.utils import rgba
from kivy.graphics import Color, Rectangle

class Tela(Screen):
    pass


class memory(App):
    image_source01 = StringProperty('source/carta.jpg')

    pontos = 5
    ListFalse = ListTrue = []

    valores = ['source/carta.jpg', 'source/carta.jpg', 'source/carta.jpg', 'source/carta.jpg',
               'source/carta.jpg', 'source/carta.jpg', 'source/carta.jpg', 'source/carta.jpg',
               'source/carta.jpg', 'source/carta.jpg', 'source/carta.jpg', 'source/carta.jpg']




    image_source01 = StringProperty('source/carta.jpg')
    image_source02 = StringProperty('source/carta.jpg')
    image_source03 = StringProperty('source/carta.jpg')

    image_source04 = StringProperty('source/carta.jpg')
    image_source05 = StringProperty('source/carta.jpg')
    image_source06 = StringProperty('source/carta.jpg')

    image_source07 = StringProperty('source/carta.jpg')
    image_source08 = StringProperty('source/carta.jpg')
    image_source09 = StringProperty('source/carta.jpg')

    image_source10 = StringProperty('source/carta.jpg')
    image_source11 = StringProperty('source/carta.jpg')
    image_source12 = StringProperty('source/carta.jpg')

    vz = 0
    select = []
    acertos = []
    quemchamou = None


    def build(self):
        return Tela()

    def on_start(self):
        self.GValues()
        return super().on_start()

    def GValues(self):
        self.pontos = 5
        App.get_running_app().root.ids.ponto.text = "Voce tem " + str(self.pontos) + " pontos"
        self.vz = 0
        self.select = []
        self.acertos = []


        imagens = ['source/maca.jpg', 'source/banana.jpg', 'source/melancia.jpg',
               'source/melao.jpg', 'source/pera.jpg', 'source/uva.jpg']

        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        B = []
        C = []
        a_valor = ''

        while len(A) != 0:
            C.append(choice(A))
            C.append(choice(A))
            if(C[0] != C[1]):
                A.remove(C[0])
                A.remove(C[1])

                B.append(C)
            C = []


        for itens in B:
            a_valor = choice(imagens)
            self.valores[(itens[0])-1] = a_valor
            self.valores[(itens[1])-1] = a_valor
            imagens.remove(a_valor)


    def quemc(self):
        item = self.quemchamou
        if item == 1:
            Clock.schedule_once(lambda dt: self.delay(1), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(1), 1.5)
        if item == 2:
            Clock.schedule_once(lambda dt: self.delay(2), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(2), 1.5)
        if item == 3:
            Clock.schedule_once(lambda dt: self.delay(3), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(3), 1.5)
        if item == 4:
            Clock.schedule_once(lambda dt: self.delay(4), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(4), 1.5)
        if item == 5:
            Clock.schedule_once(lambda dt: self.delay(5), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(5), 1.5)
        if item == 6:
            Clock.schedule_once(lambda dt: self.delay(6), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(6), 1.5)
        if item == 7:
            Clock.schedule_once(lambda dt: self.delay(7), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(7), 1.5)
        if item == 8:
            Clock.schedule_once(lambda dt: self.delay(8), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(8), 1.5)
        if item == 9:
            Clock.schedule_once(lambda dt: self.delay(9), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(9), 1.5)
        if item == 10:
            Clock.schedule_once(lambda dt: self.delay(10), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(10), 1.5)
        if item == 11:
            Clock.schedule_once(lambda dt: self.delay(11), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(11), 1.5)
        if item == 12:
            Clock.schedule_once(lambda dt: self.delay(12), 0.5)
            Clock.schedule_once(lambda dt:self.muda_imagem(12), 1.5)



    def mudapontos(self, text):
        App.get_running_app().root.ids.ponto.text = text

    def delay(self, item):
        if item == 1:
            self.image_source01 = ''
        if item == 2:
            self.image_source02 = ''
        if item == 3:
            self.image_source03 = ''
        if item == 4:
            self.image_source04 = ''
        if item == 5:
            self.image_source05 = ''
        if item == 6:
            self.image_source06 = ''
        if item == 7:
            self.image_source07 = ''
        if item == 8:
            self.image_source08 = ''
        if item == 9:
            self.image_source09 = ''
        if item == 10:
            self.image_source10 = ''
        if item == 11:
            self.image_source11 = ''
        if item == 12:
            self.image_source12 = ''

        self.pt_end = 1



    def muda_imagem(self, item):

        if item == 1:
            self.image_source01 = self.valores[0]
        if item == 2:
            self.image_source02 = self.valores[1]
        if item == 3:
            self.image_source03 = self.valores[2]
        if item == 4:
            self.image_source04 = self.valores[3]
        if item == 5:
            self.image_source05 = self.valores[4]
        if item == 6:
            self.image_source06 = self.valores[5]
        if item == 7:
            self.image_source07 = self.valores[6]
        if item == 8:
            self.image_source08 = self.valores[7]
        if item == 9:
            self.image_source09 = self.valores[8]
        if item == 10:
            self.image_source10 = self.valores[9]
        if item == 11:
            self.image_source11 = self.valores[10]
        if item == 12:
            self.image_source12 = self.valores[11]

        if self.vz == 2:
            Clock.schedule_once(lambda dt:self.check(), 1)

    def despinta(self, item):

        if item == 1:
            self.image_source01 = 'source/carta.jpg'
        if item == 2:
            self.image_source02 = 'source/carta.jpg'
        if item == 3:
            self.image_source03 = 'source/carta.jpg'
        if item == 4:
            self.image_source04 = 'source/carta.jpg'
        if item == 5:
            self.image_source05 = 'source/carta.jpg'
        if item == 6:
            self.image_source06 = 'source/carta.jpg'
        if item == 7:
            self.image_source07 = 'source/carta.jpg'
        if item == 8:
            self.image_source08 = 'source/carta.jpg'
        if item == 9:
            self.image_source09 = 'source/carta.jpg'
        if item == 10:
            self.image_source10 = 'source/carta.jpg'
        if item == 11:
            self.image_source11 = 'source/carta.jpg'
        if item == 12:
            self.image_source12 = 'source/carta.jpg'



    def click(self, qc):
        if(self.pontos == 0):
            pass
        elif (qc in self.acertos or self.quemchamou == qc):
            pass
        else:
            if self.vz < 2:
                self.quemchamou = qc
                self.quemc()
                self.vz+=1
                self.select.append(qc)



    def check(self):
        if self.vz == 2:
            if self.valores[self.select[0]-1] == self.valores[self.select[1]-1]:
                self.acertos.append(self.select[0])
                self.acertos.append(self.select[1])
                self.pontos += 1
                App.get_running_app().root.ids.ponto.text = "Voce tem " + str(self.pontos) + " pontos"
                self.pinta(self.select, (0, 1, 0, 1))
            else:
                self.pontos -= 1
                App.get_running_app().root.ids.ponto.text = "Voce tem " + str(self.pontos) + " pontos"
                self.despinta(self.select[0])
                self.despinta(self.select[1])
            self.vz = 0
            self.select = []
            if(self.pontos == 0):
                App.get_running_app().root.ids.ponto.text = "Você perdeu!"
                self.pinta([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], (1, 0, 0, 1))
            if(len(self.acertos) == 12):
                App.get_running_app().root.ids.ponto.text = "Você ganhou!"



    def restartOn(self):
        self.GValues()
        self.image_source01 = 'source/carta.jpg'
        self.image_source02 = 'source/carta.jpg'
        self.image_source03 = 'source/carta.jpg'
        self.image_source04 = 'source/carta.jpg'
        self.image_source05 = 'source/carta.jpg'
        self.image_source06 = 'source/carta.jpg'
        self.image_source07 = 'source/carta.jpg'
        self.image_source08 = 'source/carta.jpg'
        self.image_source09 = 'source/carta.jpg'
        self.image_source10 = 'source/carta.jpg'
        self.image_source11 = 'source/carta.jpg'
        self.image_source12 = 'source/carta.jpg'
        self.pinta([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], (0, 0, 0, 0))

    def pinta(self, list, cor):
        list_w = [
            App.get_running_app().root.ids.ward, App.get_running_app().root.ids.wardtwo,
            App.get_running_app().root.ids.wardthree, App.get_running_app().root.ids.wardfour,
            App.get_running_app().root.ids.wardfive, App.get_running_app().root.ids.wardsix,
            App.get_running_app().root.ids.wardseven, App.get_running_app().root.ids.wardeight,
            App.get_running_app().root.ids.wardnine, App.get_running_app().root.ids.wardteen,
            App.get_running_app().root.ids.wardeleven, App.get_running_app().root.ids.wardtwelve
        ]

        for i in list:
            q = list_w[i-1]
            q.canvas.before.clear()
            with q.canvas.before:
                Color(rgba = cor)
                Rectangle(size=q.size, pos = q.pos)


memory().run()
