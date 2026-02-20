from kivy.app import App
from kivy.uix.button import Button

class BossApp(App):
    def build(self):
        return Button(text="Success Boss Mehrab!\nMission Accomplished", 
                      font_size='25sp',
                      background_color=(0, 0.7, 0, 1))

if __name__ == '__main__':
    BossApp().run()
