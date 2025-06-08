import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog

from organizer import scan_folder  # Import your scan function

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agentic File Organizer")
        self.setGeometry(200, 200, 400, 200)

        self.layout = QVBoxLayout()
        self.label = QLabel("Select a folder to organize:")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Select Folder")
        self.button.clicked.connect(self.pick_folder)
        self.layout.addWidget(self.button)

        self.selected_label = QLabel("")  # Show selected path
        self.layout.addWidget(self.selected_label)

        self.stats_label = QLabel("")  # Show file/folder count after scan
        self.layout.addWidget(self.stats_label)

        self.setLayout(self.layout)

    def pick_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Choose a folder to organize")
        if folder:
            self.selected_label.setText(f"Selected: {folder}")

            # Scan and show stats
            files, folders = scan_folder(folder)
            self.stats_label.setText(
                f"Found {len(files)} files and {len(folders)} folders (including subfolders)."
            )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
