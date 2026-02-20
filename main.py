from kivy.app import App
from kivy.uix.button import Button

class BossGuardApp(App):
    def build(self):
        return Button(
            text='Mission Success, Boss Mehrab!\nYour APK is Ready.',
            font_size='20sp',
            background_color=(0, 0.6, 0, 1) # বিজয়ের সবুজ রঙ
        )

if __name__ == '__main__':
    BossGuardApp().run()
