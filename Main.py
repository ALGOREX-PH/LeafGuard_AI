import solara
from Pages.Home import Home
from Pages.About import About


routes = [
    solara.Route(path="/", component=Home, label="home"),
    solara.Route(path="about", component=About, label="about"),
]
