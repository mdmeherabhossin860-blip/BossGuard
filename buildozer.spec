[app]
title = BossGuard
package.name = bossguard
package.domain = org.mehrab.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# রিকোয়ারমেন্টস একদম ক্লিন রাখা হয়েছে যাতে দ্রুত কম্পাইল হয়
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# আপনার Poco ফোনের জন্য সঠিক আর্কিটেকচার
android.archs = arm64-v8a, armeabi-v7a

# ৪ মিনিটের সেই অভিশপ্ত জট কাটানোর সেটিংস
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# গিটহাব সাফল্যের আসল সিক্রেট
p4a.branch = master
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
