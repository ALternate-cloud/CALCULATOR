import webbrowser
import os
from pathlib import Path

path = Path(__file__).parent / "calculator.html"
webbrowser.open(path.resolve().as_uri())
