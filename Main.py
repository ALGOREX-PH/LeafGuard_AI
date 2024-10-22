import solara
from Pages.Home import Home
from Pages.About import About
from Pages.Temp import Temp

routes = [
    solara.Route(path="/", component=Home, label="home"),
    solara.Route(path="about", component=About, label="about"),
    solara.Route(path="temp", component=Temp, label="temp")
]
