[app]
title = BossSuccess
package.name = bosssuccess
package.domain = org.mehrab.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# আপনার ফোনের জন্য সঠিক আর্কিটেকচার
android.archs = arm64-v8a

# এখানে পরিবর্তন করা হয়েছে ৪ মিনিটের জট কাটাতে
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# বিজয়ের চাবিকাঠি
p4a.branch = master
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
