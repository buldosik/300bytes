from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core import text
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy_garden import mapview
from kivy_garden.mapview import MapView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy_garden.mapview.view import MapMarker
import base


# a = show_table_markerss()
# for i in range(0, len(a)):




class MyGrid(GridLayout):
    
    for i in base.show_table_markerss():
        map_marker = MapMarker()
        map_marker.lat = i[0]
        map_marker.lon = i[1]
        map_marker.source = "Map-Marker-Free-PNG-Image.png"
        map_view = MapView(zoom=11, lat=i[0], lon=i[1])
        map_view.add_widget(map_marker)
    map_marker1 = MapMarker()
    map_marker1.lat = 51.107883
    map_marker1.lon = 17.038538
    map_marker1.source = "Map-Marker-Free-PNG-Image.png"
    map_view = MapView(zoom=11, lat=51.107883, lon=17.038538)
    map_view.add_widget(map_marker1)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(FloatLayout())
        self.add_widget(self.map_view)

class SecondWindow(Screen):
    pass


class event_finderApp(App):
    def build(self):
        # mapview = MapView(zoom=11, lat=50.6394, lon=3.057)
        # return mapview
        # return FloatLayout()
        return MyGrid()

if __name__ == "__main__":
    event_finderApp().run()