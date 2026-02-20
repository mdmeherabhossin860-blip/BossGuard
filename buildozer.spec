[app]
title = BossGuard
package.name = bossguard
package.domain = org.mehrab
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Pillow এবং অতিরিক্ত সব সরিয়ে শুধু দরকারিটুকু রাখা হয়েছে
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

# আধুনিক অ্যান্ড্রয়েডের জন্য এটি সেরা সেটিংস
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.api = 33
android.minapi = 21
android.ndk = 25b

# গিটহাব সাফল্যের সবচেয়ে বড় চাবিকাঠি
p4a.branch = master
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
