from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

class BossGuardApp(App):
    def build(self):
        # ব্যাকগ্রাউন্ড কালার বা সুন্দর টেক্সট
        Window.clearcolor = (0.1, 0.1, 0.1, 1) # ডার্ক থিম
        return Label(
            text='Welcome to BossGuard\nCreated by Mehrab Sir',
            halign='center',
            font_size='25sp',
            color=(0, 1, 0, 1) # সবুজ রঙের লেখা
        )

if __name__ == '__main__':
    BossGuardApp().run()
