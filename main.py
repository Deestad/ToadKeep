#!/usr/bin/python3

import os
import threading

# KIVY
import kivy
from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'borderless', '1')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
kivy.require('2.1.0')
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput


from kivy.uix.tabbedpanel import TabbedPanel

# Functionality Imports
import pyperclip
import pyautogui
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Controller

# System specific imports
if os.name == 'nt':
    from KivyOnTop import register_topmost, unregister_topmost
# Configuration

with open("ToadKeep.kv", encoding='utf-8') as f:
    Builder.load_string(f.read())


keyboard = Controller()

class VirtualKeyboard(TabbedPanel):
    pass

class ButtonSet(FloatLayout):
    pass


class ToodKeppApp(App):
    def build(self):
        self.title = 'Toad Keep'
        self.icon = 'ToadKeep.ico'
        if os.name == "nt":
            self.win_build()
        return VirtualKeyboard()



    def win_build(self):
        # Make Window Topmost
        register_topmost(self, 'Toad Keep')

    def callback(self, instance):
        KeyCode = instance.text
        CopyBox = self.root.ids.copybox
        CopyBox.text = f"{CopyBox.text}{KeyCode}"
        try:
            pyperclip.copy(KeyCode)
            print(f"{KeyCode} has been copied.")
        except Exception as e:
            print(e)

    def end(self, instance):
        ToodKeppApp.stop(self)

    def minimize(self, instance):
        ToodKeppApp.get_running_app().root_window.minimize()


# Press the green Button in the gutter to run the script.
if __name__ == '__main__':
    ToodKeppApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
