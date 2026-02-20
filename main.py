from kivy.app import App
from kivy.uix.label import Label

class BossSuccess(App):
    def build(self):
        return Label(text='Mission Success, Boss Mehrab!')

if __name__ == '__main__':
    BossSuccess().run()
