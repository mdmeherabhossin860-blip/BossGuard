import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class PowerApp(App):
    def build(self):
        layout = BoxLayout()
        # এখানে আপনার জন্য একটি বিশেষ মেসেজ থাকবে
        msg = Label(text="Mission Successful!\nMehrab Sir, Your APK is Ready.", 
                    halign='center', font_size='20sp')
        layout.add_widget(msg)
        return layout

if __name__ == '__main__':
    PowerApp().run()
