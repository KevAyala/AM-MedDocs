import webview
from ui import API

if __name__ == "__main__":
    api = API()
    webview.create_window("AM MedDocs", "./index.html", width=1024, height=768, js_api=api)
    webview.start()