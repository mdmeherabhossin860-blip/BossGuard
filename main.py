from kivy.app import App
from kivy.uix.label import Label
import os

class BossGuard(App):
    def build(self):
        # আপনার সেই 'নিজ বাড়িতে' ফাইল তৈরির কমান্ড
        try:
            with open("/sdcard/boss_data.txt", "a") as f:
                f.write("জি মেহেরাব স্যার, বস গার্ড এখন সচল।\n")
        except:
            pass
        return Label(text='BOSS GUARD\nAuthorized by Mehrab')

if __name__ == '__main__':
    BossGuard().run()
