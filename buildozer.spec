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

# এখানে আপনার চাওয়া INTERNET পারমিশন যোগ করা হয়েছে
android.permissions = INTERNET

# আধুনিক ফোনের জন্য সঠিক আর্কিটেকচার
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# আপনার Poco ফোনের জন্য স্থিতিশীল এপিআই লেভেল
android.api = 31
android.minapi = 21
android.ndk_api = 21

# গিটহাব সাফল্যের সবচেয়ে বড় চাবিকাঠি
p4a.branch = master
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
