[app]
title = BossGuard
package.name = bossguard
package.domain = org.mehrab
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Pillow সরিয়ে শুধু মৌলিক লাইব্রেরি রাখা হয়েছে
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

# আধুনিক ফোনের জন্য আর্কিটেকচার বাড়ানো হয়েছে
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# আপনার স্ক্রিনশটে থাকা সঠিক এপিআই সেটিংস
android.api = 31
android.minapi = 21
android.ndk_api = 21

# এই লাইনটি আপনার ১০ মিনিটের বাধা ভাঙবে
p4a.branch = master

# এনট্রি পয়েন্ট নিশ্চিত করা হলো
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
