import webview

def start_ui():
    """Inicia la interfaz gráfica con PyWebView."""
    webview.create_window("AM MedDocs", "./index.html", width=1024, height=768)
    webview.start()
