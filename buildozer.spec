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
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license = True


[buildozer]
log_level = 2
warn_on_root = 1
