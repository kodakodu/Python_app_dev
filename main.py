from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

#App settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(300,200)

#Create all Object/Widget below here
title = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")

button1 =QPushButton("CLick Me")
button2 =QPushButton("CLick Me")
button3 =QPushButton("CLick Me")

#All design here
master_layout = QVBoxLayout()



main_window.show()
app.exec()