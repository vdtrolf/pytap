import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class MainScreen(FloatLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        box_layout = BoxLayout(orientation='vertical')
        grid_layout = GridLayout(cols=3, spacing=5, size_hint=(None, None), size=(300, 300))
        grid_layout.bind(minimum_size=grid_layout.setter('size'))
        colors = ['#FF0000', '#00FF00', '#0000FF',
                  '#FFFF00', '#FF00FF', '#00FFFF',
                  '#FFA500', '#800080', '#008080']

        for color in colors:
            button = Button(background_color=color, size_hint=(None, None), size=(100, 100))
            button.bind(on_press=self.change_background)
            grid_layout.add_widget(button)
            
        box_layout.add_widget(Widget())  # Spacer
        box_layout.add_widget(grid_layout)
        box_layout.add_widget(Widget())  # Spacer

        self.add_widget(box_layout)
        
    def change_background(self, instance):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*instance.background_color)
            Rectangle(pos=self.pos, size=self.size)
            
class MyApp(App):
    def build(self):
        return MainScreen()
        
if __name__ == '__main__':
    MyApp().run()