import sys
from PyQt6.QtWidgets import QApplication, QLineEdit, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from pytube import YouTube

app = QApplication(sys.argv)
SAVE_PATH = "YT vids"  # Path to save video's

window = QWidget()
window.setWindowTitle("YT Video downloader")
window.setGeometry(100, 100, 400, 300)

text_box = QLineEdit()
text_box.setPlaceholderText("Enter the link of the video: ")

def button_clicked():
    link = text_box.text()
    try:
        yt = YouTube(link)
    except:
        QMessageBox.critical(window, "Error", "Connection Error")
        return

    mp4_streams = yt.streams.filter(file_extension='mp4')

    d_video = mp4_streams[-1]

    try:
        # downloading the video
        d_video.download(output_path=SAVE_PATH)
        QMessageBox.information(window, "Success", "Video downloaded successfully!")
    except:
        QMessageBox.critical(window, "Error", "Some Error!")

button = QPushButton("Click me!")
button.clicked.connect(button_clicked)

layout = QVBoxLayout()
layout.addWidget(text_box)
layout.addWidget(button)
window.setLayout(layout)

window.show()

sys.exit(app.exec())