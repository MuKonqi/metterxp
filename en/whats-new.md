---
layout: page-en
title: MetterXP 2.0.0
---
# MetterXP 2.0.0
## What's New:

Added multiple language support. New language: English


A total of 10 themes were added in version 2.0.0 with the theme in version 1.2-1.


Switched to subprocess.Popen instead of os.system in the original MetterXP file. This allows the application to get rid of its crooked appearance when initializing some modules, while at the same time the user always 
made it not open MetterXP.


Removed "Update MetterXP" button in original MetterXP file, added "MetterXP options" button.


Added a menu option called MetterXP to the original MetterXP file. This has options: About MetterXP, MetterXP options, Update MetterXP, Uninstall MetterXP


Switched from the yukle.py installer to the apiutaller installer and uninstaller.


In addition to apiutaller, Uninstall MetterXP module was made to delete the application.


Added install/reinstall/uninstall Flatpak apps.


Added custom GUI application launch.


The ability to configure Plank has been removed.


Added a new reset option for the .bashrc file.


The bloat lines have been reduced.


Renamed button, text, space text and many more. This made the code more tidy. Note: The last n's are the number of that thing.

Old: islemsecimbutonn, yazi, b_metin

New: buttonn, textn, spacen


Most def()s and buttons etc. The name of things was made in English. This provides convenience to people globally.


Deleted python3.policy file, added [io.github.mukonqi.metterxp](https://mukonqi.github.io/metterxp).policy. This made it say "Authentication is required for MetterXP" instead of "Authentication is required" and prevented apps that needed the python3.policy file from getting corrupted when deleting the app.