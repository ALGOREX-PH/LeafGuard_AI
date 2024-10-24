import solara


@solara.component
def Home():
        # Hero Section
        solara.Title("LeafGuard AI")
        solara.Markdown("The smart way to protect your orchard, understanding diseases over leaves on plants.")
        #with solara.Box(style={"margin-top": "20px"}):
        solara.Button("Get Started Now", style={"background-color": "#7CFC00", "color": "#FFFFFF", "padding": "10px 20px", "border": "none", "cursor": "pointer"})
        #solara.Button("Learn More", style={"background-color": "#228B22", "color": "#FFFFFF", "padding": "10px 20px", "border": "none", "margin-left": "10px", "cursor": "pointer"})

        # Information Section
        with solara.Columns([2,  2], style={"padding": "40px", "background-color": "#F5F5DC"}):
            # First Info Card
            with solara.Card(style={"padding": "20px", "background-color" : "#7CFC00", "text-align": "center"}):
                solara.Image("Images/Image_1.jpg")
                solara.Text("Protect Your Orchard", style = {"font-size" : "20px", "font-weight" : "bold"})
                solara.Markdown("The comprehensive solution to manage orchard health...")
                solara.Button("Learn More", style={"background-color": "#D2691E", "color": "white", "padding": "10px 20px", "border-radius": "5px"})

            # Second Info Card
            with solara.Card(style={"padding": "20px", "background-color" : "#7CFC00", "text-align": "center"}):
                solara.Image("Images/Image_2.jpg")
                solara.Text("Protect Your Cedar Yard", style = {"font-size" : "20px", "font-weight" : "bold"})
                solara.Markdown("Track and prevent diseases such as black rot from spreading...")
                solara.Button("Learn More", style={"background-color": "#D2691E", "color": "white", "padding": "10px 20px", "border-radius": "5px"})

            # Third Info Card
            with solara.Card(style={"padding": "20px", "background-color" : "#7CFC00", "text-align": "center"}):
                solara.Image("Images/Image_3.jpg")
                solara.Text("Cedar Rust & Learn", style = {"font-size" : "20px", "font-weight" : "bold"})
                solara.Markdown("Gain insights into cedar rust and learn effective treatment...")
                solara.Button("Learn More", style={"background-color": "#D2691E", "color": "white", "padding": "10px 20px", "border-radius": "5px"})

            # Fourth Info Card
            with solara.Card(style={"padding": "20px", "background-color" : "#7CFC00", "text-align": "center"}):
                solara.Image("Images/Image_4.jpg")
                solara.Text("Read Apple Scabs", style = {"font-size" : "20px", "font-weight" : "bold"})
                solara.Markdown("Identify apple scabs early with our precise AI detection system...")
                solara.Button("Learn More", style={"background-color": "#D2691E", "color": "white", "padding": "10px 20px", "border-radius": "5px"})

    #solara.Title("Introduction to LeafGuard AI")
    #solara.Text("LeafGuard AI is an advanced AI-driven model designed to enhance agricultural health monitoring by detecting common leaf diseases such as Black Rot, Cedar Rust, and Apple Scabs. Leveraging cutting-edge image recognition technology, LeafGuard AI analyzes leaf images to identify and classify these diseases with high accuracy, providing farmers and agricultural experts with a powerful tool to protect their crops.")
    #solara.Text("By integrating deep learning algorithms with agricultural expertise, LeafGuard AI empowers users to take proactive measures in disease management, ensuring the health and productivity of their plants. The model is optimized for ease of use, requiring only a simple image upload to provide a diagnosis and recommend actionable steps.")
    #solara.Text("With LeafGuard AI, we aim to revolutionize the field of precision agriculture, minimizing crop loss and promoting sustainable farming practices through technology.")
    #solara.Button(label="Go", attributes={"href": "http://localhost:8765/about"})