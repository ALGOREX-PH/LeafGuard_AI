import solara
from Pages.Home import Home
from Pages.About import About
from Pages.Temp import Temp
from Pages.Apple_Scabs_Information_Page import Apple_Scabs_Info
from Pages.Black_Rot_Information_Page import Black_Rot_Info
from Pages.Cedar_Rust_Information_Page import Cedar_Rust_Info
from Pages.Chat import Chat
from Pages.Demo import Demo
from solara.alias import rv

#solara.Style("styles/style.css")

rv.NavigationDrawer(color="black")
routes = [
    solara.Route(path="/", component=Home, label = "Home"),
    solara.Route(path="about", component=About, label = "About"),
    solara.Route(path="temp", component=Temp, label = "Temp"),
    solara.Route(path="Apple_Scabs_Info", component= Apple_Scabs_Info, label = "Apple Scabs Info Page"),
    solara.Route(path="Black_Rot_Info", component= Black_Rot_Info, label = "Black Rot Info Page"),
    solara.Route(path="Cedar_Rust_Info", component= Cedar_Rust_Info, label = "Cedar Rust Info Page"),
    solara.Route(path="Demo", component= Demo, label = "Demo"),
    solara.Route(path="Chat", component= Chat, label = "Chat"),
]
