from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
import markdown
from markdown_katex import KatexExtension

# Markdown to HTML conversion function
def convert_md_to_html(md_file):
    with open(md_file, "r") as f:
        text = f.read()
    return markdown.markdown(text, extensions=["extra", "codehilite", KatexExtension()])

class QuickCardApp(QMainWindow):
    def __init__(self, card_html):
        super().__init__()
        self.setWindowTitle("QuickCard Viewer")
        self.resize(600, 800)

        # Layout and WebView
        layout = QVBoxLayout()
        self.web_view = QWebEngineView()
        self.web_view.setHtml(card_html)  # Load HTML content
        layout.addWidget(self.web_view)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Main application
if __name__ == "__main__":
    import sys

    # Convert card from Markdown to HTML
    card_html = convert_md_to_html("cards/calibration.md")

    # Run Qt app
    app = QApplication(sys.argv)
    viewer = QuickCardApp(card_html)
    viewer.show()
    sys.exit(app.exec())
