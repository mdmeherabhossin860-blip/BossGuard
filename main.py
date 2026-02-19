from kivy.app import App
from kivy.uix.label import Label

class BossGuardApp(App):
    def build(self):
        # কোনো বাংলা অক্ষর রাখা যাবে না, আপাতত এটি দিয়ে টেস্ট করুন
        return Label(text='Hello Boss Mehrab, Success!')

if __name__ == '__main__':
    BossGuardApp().run()
