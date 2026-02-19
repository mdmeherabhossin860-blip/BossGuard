[app]
title = BossGuard
package.name = bossguard
package.domain = org.mehrab
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# (Target API for modern phones)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_path = 
android.sdk_path = 

# (The most important line for GitHub success)
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
