from PyQt6.QtWidgets import QApplication
import ui

if __name__ == "__main__":
    app = QApplication([])
    window = AMMedDocsUI()
    window.show()
    app.exec()