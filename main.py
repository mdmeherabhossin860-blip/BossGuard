from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BossGuardApp(App):
    def build(self):
        layout = BoxLayout(padding=10)
        btn = Button(text="Success Boss Mehrab!\nYour App is Ready", 
                     font_size='20sp',
                     background_color=(0, 1, 0, 1))
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    BossGuardApp().run()
