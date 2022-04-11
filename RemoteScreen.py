import main
from kivy.uix.screenmanager import ScreenManager, Screen

s = None

class Remote(Screen):
    global s
    spin_amount = 5
    def back(self):
        main.App.get_running_app().root.current = 'beginning'

    def control(self, key, event):
        s.send(bytes(f'{event}\n', 'utf-8'))

        if key == "A":
            self.ids.uparrow.source="./imgs/press/arrup.png"

        elif key == "B":
            self.ids.leftarrow.source="./imgs/press/arleft.png"

        elif key == "C":
            self.ids.rightarrow.source="./imgs/press/arright.png"

        elif key == "D":
            self.ids.downarrow.source="./imgs/press/arrdown.png"
    pass


