import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
import pyperclip
import pyautogui
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Controller
kivy.require('2.1.0')

keyboard = Controller()
class VirtualKeyboard(FloatLayout):
    pass

class ToodKeppApp(App):
    def build(self):
        return VirtualKeyboard()
    def callback(self, instance):
        KeyCode = instance.text
        try:
            pyperclip.copy(KeyCode)
            print(f"{KeyCode} has been copied.")
        except Exception as e:
            print(e)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ToodKeppApp().run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
