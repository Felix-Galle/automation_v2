import sys
from PyQt5.QtWidgets import QApplication
from __window__ import FileDragWindow  # Import the window class

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create and show the main window
    window = FileDragWindow()
    window.show()  # This will show the window and will hide right away due to the logic inside the window class

    # Start the event loop
    sys.exit(app.exec_())
