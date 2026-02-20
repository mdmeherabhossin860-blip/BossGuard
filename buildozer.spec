[app]
title = BossGuard
package.name = bossguard
package.domain = org.mehrab
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# শুধু দরকারি লাইব্রেরি রাখা হয়েছে
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

# আপনার রিকোয়েস্ট অনুযায়ী ইন্টারনেট পারমিশন যোগ করা হলো
android.permissions = INTERNET

# আপনার ফোনের জন্য সঠিক আর্কিটেকচার
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# আপনার স্ক্রিনশটের বর্তমান স্থিতিশীল এপিআই সেটিংস
android.api = 31
android.minapi = 21
android.ndk_api = 21

# ১০ মিনিটের জট খোলার প্রধান চাবিকাঠি
p4a.branch = master
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
