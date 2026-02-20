[app]
title = BossSuccess
package.name = bosssuccess
package.domain = org.mehrab
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# রিকোয়ারমেন্টস একদম ক্লিন রাখা হয়েছে
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# আপনার Poco ফোনের জন্য সঠিক আর্কিটেকচার
android.archs = arm64-v8a

# এই সেটিংসটি এবার ৪ মিনিটের জট ভাঙবে
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# গিটহাব সাফল্যের আসল চাবিকাঠি
p4a.branch = master
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
