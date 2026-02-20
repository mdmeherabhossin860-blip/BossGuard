from kivy.app import App
from kivy.uix.label import Label

class BossGuardApp(App):
    def build(self):
        # কোনো স্পেশাল ক্যারেক্টার ছাড়া একদম ক্লিন টেক্সট
        return Label(text='Success Boss Mehrab! Your App is Ready.')

if __name__ == '__main__':
    BossGuardApp().run()
