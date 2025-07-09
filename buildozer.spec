[app]
title = FaceAppOffline
package.name = faceapp
package.domain = org.faceapp
source.dir = .
source.include_exts = py,png,jpg,mp3,html,json,xml
version = 1.0
requirements = kivy==2.2.1, flask, opencv-python, numpy, requests, jinja2, email
orientation = portrait
fullscreen = 1
android.permissions = INTERNET, CAMERA
android.minapi = 21

[buildozer]
log_level = 2
warn_on_root = 1
