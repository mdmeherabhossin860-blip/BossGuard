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
android.api = 31
android.minapi = 21
android.ndk_api = 21
p4a.branch = master
android.entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
