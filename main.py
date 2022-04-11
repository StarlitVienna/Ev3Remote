from kivymd.app import MDApp as App
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
import socket
import RemoteScreen

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
Window.softinput_mode = "below_target"


class ScreenManagement(ScreenManager):
    pass


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def connect(self, IP, PORT):
        try:
            self.s.connect((IP, int(PORT)))
        except Exception as e:
            print(e)
            return

        #self.s.send(bytes('<3', 'utf-8'))
        self.open_remote()


    def open_remote(self):
        App.get_running_app().root.current = 'Remote'
        RemoteScreen.s = self.s


    def on_touch_move(self, touch):
        print(touch.pos)

    def arrow_up_press(self):
        self.ids.uparrow.source = './imgs/arrowupblankpress.png'

    def arrow_up_release(self):
        self.ids.uparrow.source = './imgs/arrowupblank.png'





class KivyApp(App):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        kv = Builder.load_file("./main.kv")

        return kv


if __name__ == '__main__':
    KivyApp().run()
