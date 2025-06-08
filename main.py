import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit
)
from organizer import scan_folder

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agentic File Organizer")
        self.setGeometry(200, 200, 500, 350)

        self.layout = QVBoxLayout()
        self.label = QLabel("Select a folder to organize:")
        self.layout.addWidget(self.label)

        self.button = QPushButton("Select Folder")
        self.button.clicked.connect(self.pick_folder)
        self.layout.addWidget(self.button)

        self.selected_label = QLabel("")
        self.layout.addWidget(self.selected_label)

        self.stats_label = QLabel("")
        self.layout.addWidget(self.stats_label)

        # Add a text area for previewing files/folders
        self.preview_area = QTextEdit()
        self.preview_area.setReadOnly(True)
        self.layout.addWidget(self.preview_area)

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

            # Show file and folder names (limit preview for huge folders)
            max_preview = 15
            preview_text = ""
            if folders:
                preview_text += "Folders:\n"
                preview_text += "\n".join(f"- {f}" for f in folders[:max_preview])
                if len(folders) > max_preview:
                    preview_text += f"\n...and {len(folders) - max_preview} more folders.\n"
                preview_text += "\n"
            if files:
                preview_text += "Files:\n"
                preview_text += "\n".join(f"- {f}" for f in files[:max_preview])
                if len(files) > max_preview:
                    preview_text += f"\n...and {len(files) - max_preview} more files.\n"
            if not (files or folders):
                preview_text = "No files or folders found."

            self.preview_area.setPlainText(preview_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
