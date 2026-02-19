from kivy.app import App
from kivy.uix.label import Label

class BossGuardApp(App):
    def build(self):
        # কোনো বাংলা অক্ষর রাখা যাবে না, এটিই আকাশ পরিষ্কার করবে
        return Label(text='Boss Mehrab, Success is Certain!')

if __name__ == '__main__':
    BossGuardApp().run()
