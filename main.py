from kivy.app import App
from kivy.uix.label import Label

class BossGuardApp(App):
    def build(self):
        # আপাতত শুধু ইংরেজি দিয়ে টেস্ট করুন যাতে লাল বাতি না জ্বলে
        return Label(text='Hello Boss Mehrab, Success!')

if __name__ == '__main__':
    BossGuardApp().run()
