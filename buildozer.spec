[app]
title = BossPower
package.name = bosspower
package.domain = org.mehrab.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# requirements একদম ফিক্সড করে দেওয়া হলো
requirements = python3,kivy==2.2.1,hostpython3==3.10.12

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# আপনার Poco ফোনের জন্য সঠিক এবং শক্তিশালী আর্কিটেকচার
android.archs = arm64-v8a

# এনডিকে ২৫বি এর সাথে এপিআই ৩৩ এর মেলবন্ধন (সবচেয়ে স্টেবল)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# এই লাইনটি আপনার ৬ মিনিটের বাধা ভাঙবে
p4a.branch = master
android.entrypoint = main.py
android.skip_setup = False

[buildozer]
log_level = 2
warn_on_root = 1
