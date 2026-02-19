from kivy.app import App
from kivy.uix.label import Label

class BossGuardApp(App):
    def build(self):
        return Label(text='Hello Boss Mehrab, Your App is Ready!')

if __name__ == '__main__':
    BossGuardApp().run()
