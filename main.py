from kivy.app import App
from kivy.uix.label import Label

class BossGuardApp(App):
    def build(self):
        return Label(text='জি মেহেরাব স্যার বলেন, আপনার অ্যাপ তৈরি!')

if __name__ == '__main__':
    BossGuardApp().run()
