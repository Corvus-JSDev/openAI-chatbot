import sys
from PyQt6.QtWidgets import *
from backend import ChatBot

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		grid = QGridLayout()
		self.resize(700, 500)  # Width, Height

		# Chat window
		self.chat_area = QTextEdit(self)
		self.chat_area.setGeometry(10, 10, 480, 320)  # (left-padding, right-padding, width, height)

		# Input fields
		self.input_field = QLineEdit(self)
		self.input_field.setGeometry(10, 350, 480, 40)

		# Buttons
		self.button = QPushButton("Send", self)
		self.button.clicked.connect(self.send_msg)
		self.button.setGeometry(10, 405, 80, 35)

		self.show()


	def send_msg(self):
		user_input = self.input_field.text()
		chat = ChatBot()
		chat.get_response(user_input)




app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec())



