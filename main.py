import webbrowser
from pathlib import Path

webbrowser.register("brave", None, webbrowser.BackgroundBrowser("brave-browser"))

path = Path(__file__).parent / "calculator.html"
webbrowser.get("brave").open(path.resolve().as_uri())
