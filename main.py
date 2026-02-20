from kivy.app import App
from kivy.uix.label import Label

class BossGuardApp(App):
    def build(self):
        return Label(text='Boss Mehrab, Success is Yours!')

if __name__ == '__main__':
    BossGuardApp().run()
