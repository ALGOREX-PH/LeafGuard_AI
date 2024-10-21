import solara


@solara.component
def Home():
    solara.Title("Introduction to LeafGuard AI")
    solara.Text("LeafGuard AI is an advanced AI-driven model designed to enhance agricultural health monitoring by detecting common leaf diseases such as Black Rot, Cedar Rust, and Apple Scabs. Leveraging cutting-edge image recognition technology, LeafGuard AI analyzes leaf images to identify and classify these diseases with high accuracy, providing farmers and agricultural experts with a powerful tool to protect their crops.")
    solara.Text("By integrating deep learning algorithms with agricultural expertise, LeafGuard AI empowers users to take proactive measures in disease management, ensuring the health and productivity of their plants. The model is optimized for ease of use, requiring only a simple image upload to provide a diagnosis and recommend actionable steps.")
    solara.Text("With LeafGuard AI, we aim to revolutionize the field of precision agriculture, minimizing crop loss and promoting sustainable farming practices through technology.")
    