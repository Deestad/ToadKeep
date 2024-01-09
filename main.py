#!/usr/bin/python3
import os
import threading
import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from KivyOnTop import register_topmost, unregister_topmost
import pyperclip
import pyautogui
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Controller

# Configuration

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '300')
Config.set('graphics', 'borderless', '1')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
kivy.require('2.1.0')

keyboard = Controller()
class VirtualKeyboard(FloatLayout):
    pass
class ButtonSet(FloatLayout):
    pass



class ToodKeppApp(App):
    def build(self):
        Window.set_title('Toad Keep')
        # Make Window Topmost
        if os.name == "nt":
            register_topmost(Window, 'Toad Keep')
        self.icon = 'ToadKeep.ico'
        return VirtualKeyboard()

    def callback(self, instance):
        KeyCode = instance.text
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
