from kivy.app import App
from kivy.uix.label import Label

class BossGuardApp(App):
    def build(self):
        # কোনো স্পেশাল ক্যারেক্টার বা বাংলা ছাড়া একদম ক্লিন টেক্সট
        return Label(text='Boss Mehrab Success')

if __name__ == '__main__':
    BossGuardApp().run()
