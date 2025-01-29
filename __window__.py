import sys
import json
import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu, QAction, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from pc_info import get_broadcasting_ips  # Import the function to get broadcasting IPs

class FileDragWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("File Drag Window")
        self.setGeometry(100, 100, 200, 100)  # Initial size
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Create a label to display
        self.label = QLabel("Drag files here", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 200); border: 1px solid black;")

        # Set up the system tray
        self.tray_icon = QSystemTrayIcon(QIcon("resources/icon.png"), self)
        self.tray_icon.setToolTip("File Drag App")
        self.tray_icon.activated.connect(self.tray_icon_activated)

        # Create a context menu for the tray icon
        tray_menu = QMenu()
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)
        tray_menu.addAction(exit_action)
        self.tray_icon.setContextMenu(tray_menu)

        self.tray_icon.show()

        # Hide the window initially
        self.hide()

        self.computer_buttons_layout = QVBoxLayout()  # Layout for computer buttons
        self.computer_widget = QWidget()  # Widget to hold the buttons
        self.computer_widget.setLayout(self.computer_buttons_layout)

    def tray_icon_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def showEvent(self, event):
        super().showEvent(event)
        self.activateWindow()

    def enterEvent(self, event):
        # Enlarge the window when mouse enters
        self.setGeometry(100, 100, 400, 200)  # Enlarged size
        self.display_computer_buttons()  # Display buttons for discovered computers

    def leaveEvent(self, event):
        # Restore the window size when mouse leaves
        self.setGeometry(100, 100, 200, 100)  # Original size
        self.clear_computer_buttons()  # Clear buttons when leaving

    def display_computer_buttons(self):
        self.clear_computer_buttons()  # Clear existing buttons
        broadcasting_ips = get_broadcasting_ips()  # Get the list of broadcasting IPs

        for pc_name, ip in broadcasting_ips:
            button = QPushButton(f"Send to {pc_name} ({ip})", self)
            button.clicked.connect(lambda checked, ip=ip: self.send_file(ip))  # Connect button to send_file method
            self.computer_buttons_layout.addWidget(button)

        self.computer_widget.setGeometry(0, 0, 400, 200)  # Set geometry for the widget
        self.computer_widget.show()  # Show the widget with buttons

    def clear_computer_buttons(self):
        for i in reversed(range(self.computer_buttons_layout.count())): 
            widget = self.computer_buttons_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()  # Remove the button from the layout

    def send_file(self, destination_ip):
        # Logic to send the file to the selected destination IP
        print(f"Sending file to {destination_ip}")  # Placeholder for actual file sending logic

    def exit_app(self):
        self.tray_icon.hide()
        QApplication.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileDragWindow()
    window.show()  # Show the window initially (it will hide immediately)
    sys.exit(app.exec_())
