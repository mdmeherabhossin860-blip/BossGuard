[app]
title = BossPower
package.name = bosspower
package.domain = org.mehrab.boss
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# আমরা কিভির একদম লেটেস্ট ভার্সন ব্যবহার করব যাতে পুরনো জট না থাকে
requirements = python3,kivy==master

orientation = portrait
fullscreen = 1
android.permissions = INTERNET, STORAGE

# আর্কিটেকচার একদম স্পেসিফিক করে দেওয়া হলো আপনার Poco এর জন্য
android.archs = arm64-v8a

# এটিই আসল পরিবর্তন - API এবং NDK ভার্সন আপডেট করা হয়েছে
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

# গিটহাবের জন্য ব্রহ্মাস্ত্র
p4a.branch = master
android.entrypoint = main.py
android.skip_setup = False

[buildozer]
log_level = 2
warn_on_root = 1
