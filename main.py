from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SC(BoxLayout):
    pass

class SentimentClassifierApp(App):
    def build(self):
        return SC()

SentimentClassifierApp().run()

