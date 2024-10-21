import solara

@solara.component
def About():
    solara.Title("Welcome to LeafGuard AI")
    with solara.Card("LeafGuard AI", style={"padding": "20px", "max-width": "600px", "margin": "0 auto", "background-color": "#7CFC00"}):
        solara.Text("Detect leaf diseases like Black Rot, Cedar Rust, and Apple Scabs.")
        solara.Button("Get Started", on_click=lambda: solara.navigate("/detect"), style={
            "background-color": "#D2691E", "color": "white", "padding": "10px 20px", "border-radius": "5px"
        })
    with solara.Card("LeafGuard AI", style={"padding": "20px", "max-width": "600px", "margin": "0 auto", "background-color": "#7CFC00"}):
        solara.Text("Detect leaf diseases like Black Rot, Cedar Rust, and Apple Scabs.")
        solara.Button("Get Started", on_click=lambda: solara.navigate("/detect"), style={
            "background-color": "#D2691E", "color": "white", "padding": "10px 20px", "border-radius": "5px"
        })
    with solara.Card("LeafGuard AI", style={"padding": "20px", "max-width": "600px", "margin": "0 auto", "background-color": "#7CFC00"}):
        solara.Text("Detect leaf diseases like Black Rot, Cedar Rust, and Apple Scabs.")
        solara.Button("Get Started", on_click=lambda: solara.navigate("/detect"), style={
            "background-color": "#D2691E", "color": "white", "padding": "10px 20px", "border-radius": "5px"
        })
    