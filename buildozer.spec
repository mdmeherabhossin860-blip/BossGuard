[app]
title = BossGuard
package.name = bossguard
package.domain = org.mehrab.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# এটি সবার ফোনের জন্য সবচেয়ে স্থিতিশীল ভার্সন
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# এটি সবচেয়ে গুরুত্বপূর্ণ: এই দুটি আর্কিটেকচার থাকলে সব ফোনে চলবে
android.archs = arm64-v8a, armeabi-v7a

android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

p4a.branch = master
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
