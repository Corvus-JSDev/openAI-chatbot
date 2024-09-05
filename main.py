import sys
from PyQt6.QtWidgets import *
from backend import ChatBot

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.chat = ChatBot()
		self.resize(700, 500)  # Width, Height

		# Chat window
		self.chat_area = QTextEdit(self)
		self.chat_area.setGeometry(10, 10, 480, 320)  # (left-padding, top-padding, width, height)

		# Input fields
		self.input_field = QLineEdit(self)
		self.input_field.setGeometry(10, 350, 480, 40)

		# Buttons
		self.button = QPushButton("Send", self)
		self.button.clicked.connect(self.send_msg)
		self.button.setGeometry(500, 350, 100, 40)

		# Err msg
		self.error_msg = QLabel("", self)
		self.error_msg.setGeometry(10, 380, 550, 100)

		self.show()


	def send_msg(self):
		try:
			user_input = self.input_field.text().strip()
			self.chat_area.append(f"You: {user_input}")

			reply = self.chat.get_response(user_input)
			self.chat_area.append(f"\n<p style='font-weight: 600;'>BOT: {reply}</p>\n")

		except:
			self.error_msg.setText("ERROR: Invalid API key and/or deprecated engine model.\nPlease check console for details.")

			print("ERROR: Invalid API key and/or deprecated engine model.\nPlease check backend.py to update the engine\nAlso create an .env file to input your API key")

		self.input_field.clear()




app = QApplication(sys.argv)
main_window = MainWindow()
sys.exit(app.exec())



