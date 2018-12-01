from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class HomeScreen(GridLayout):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.cols = 1

        self.label = Label()
        self.label.text = "Enter Name to Start:"
        self.label.pos = (150, 50)
        self.label.color = (1, 1, 1, 1)
        self.add_widget(self.label)

        playerusername = TextInput()
        playerusername.multiline = False
        playerusername.size = (10, 10)
        playerusername.pos = (200, 200)
        playerusername.color = (0, 0, 0, 1)
        self.add_widget(playerusername)
        self.add_widget(Button(text="Enter Game"))


class MyApp(App):
    def build(self):
        return HomeScreen()


MyApp().run()
