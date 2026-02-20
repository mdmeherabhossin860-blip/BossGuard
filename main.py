from kivy.app import App
from kivy.uix.label import Label

class BossGuard(App):
    def build(self):
        return Label(text='Success Boss Mehrab!')

if __name__ == '__main__':
    BossGuard().run()
