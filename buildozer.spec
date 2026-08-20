[app]

title = MathAfro

package.name = mathafro
package.domain = org.alexdynamo

source.dir = .

source.include_exts = py,kv,png,jpg,jpeg,atlas,txt,json,ttf

version = 1.0

requirements =requirements = python3, kivy==2.3.1, https://github.com/kivymd/KivyMD/archive/master.zip, exceptiongroup, asynckivy, asyncgui, materialyoucolor, android, materialshapes, pycairo1,sympy

presplash.filename = mathafro_icon.png
icon.filename = mathafro_icon.png

orientation = portrait

fullscreen = 0

android.presplash_color = black

# Aucune permission nécessaire pour la version actuelle
# android.permissions =

android.accept_sdk_license = True

android.archs = arm64-v8a,armeabi-v7a

android.allow_backup = True


[buildozer]

log_level = 2
warn_on_root = 1
