# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		# setting title
		self.setWindowTitle("Vishnu's Calculator ")

		# setting geometry
		self.setGeometry(0, 0, 400, 300)

		# calling method
		self.UiComponents()

		# showing all the widgets
		self.show()

	# method for widgets
	def UiComponents(self):

		# creating a label
		self.label = QLabel(self)

		# setting geometry to the label
		self.label.setGeometry(5, 5, 390, 40)

		# creating label multi line
		self.label.setWordWrap(True)

		# setting style sheet to the label
		self.label.setStyleSheet("QLabel"
								"{"
								"border : 5px solid black;"
								"background : white;"
								"}")



        # creating a push button
		button1 = QPushButton("1", self)

		# setting geometry of button
		button1.setGeometry(0, 100, 100, 50)

		# adding action to a button
		button1.clicked.connect(self.action1)

		# setting icon to the button
		# button1.setIcon(QIcon('mars_logo.png'))

		# creating a push button
		button2 = QPushButton("2", self)
		button2.setGeometry(100, 100, 100, 50)
		button2.clicked.connect(self.action2)

		button3 = QPushButton("3", self)
		button3.setGeometry(200, 100, 100, 50)
		button3.clicked.connect(self.action3)

		button4 = QPushButton("4", self)
		button4.setGeometry(0, 150, 100, 50)
		button4.clicked.connect(self.action4)

		button5 = QPushButton("5", self)
		button5.setGeometry(100, 150, 100, 50)
		button5.clicked.connect(self.action5)

		button6 = QPushButton("6", self)
		button6.setGeometry(200, 150, 100, 50)
		button6.clicked.connect(self.action6)

		button7 = QPushButton("7", self)
		button7.setGeometry(0, 200, 100, 50)
		button7.clicked.connect(self.action7)

		button8 = QPushButton("8", self)
		button8.setGeometry(100, 200, 100, 50)
		button8.clicked.connect(self.action8)

		button9 = QPushButton("9", self)
		button9.setGeometry(200, 200, 100, 50)
		button9.clicked.connect(self.action9)

		button0 = QPushButton("0", self)
		button0.setGeometry(0, 250, 100, 50)
		button0.clicked.connect(self.action0)

		button_equal = QPushButton("=", self)
		button_equal.setGeometry(300, 250, 100, 50)
		button_equal.clicked.connect(self.action_equal)

		button_plus = QPushButton("+", self)
		button_plus.setGeometry(300, 200, 100, 50)
		button_plus.clicked.connect(self.action_plus)

		button_minus = QPushButton("-", self)
		button_minus.setGeometry(300, 150, 100, 50)
		button_minus.clicked.connect(self.action_minus)

		button_dot = QPushButton(".", self)
		button_dot.setGeometry(100, 250, 100, 50)
		button_dot.clicked.connect(self.action_dot)

		button_divide = QPushButton("/", self)
		button_divide.setGeometry(300, 50, 100, 50)
		button_divide.clicked.connect(self.action_divide)

		button_multiply = QPushButton("*", self)
		button_multiply.setGeometry(300, 100, 100, 50)
		button_multiply.clicked.connect(self.action_multiply)

		button_clear = QPushButton("Clear", self)
		button_clear.setGeometry(0, 50, 300, 50)
		button_clear.clicked.connect(self.action_clear)

		button_del = QPushButton("Del", self)
		button_del.setGeometry(200, 250, 100, 50)
		button_del.clicked.connect(self.action_del)
	# action method

	def action(self):

		# printing pressed
		print("you pressed")

	def action0(self):

		# printing pressed
		text = self.label.text()
		self.label.setText(text + "0")

	def action1(self):

		# printing pressed
		text = self.label.text()
		self.label.setText(text + "1")

	def action2(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "2")

	def action3(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "3")

	def action4(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "4")

	def action5(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "5")

	def action6(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "6")

	def action7(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "7")

	def action8(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "8")

	def action9(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "9")

	def action_dot(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + ".")

	def action_plus(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "+")

	def action_minus(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "-")

	def action_multiply(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "*")

	def action_divide(self):
		# printing pressed
		text = self.label.text()
		self.label.setText(text + "/")

	def action_del(self):
		# printing pressed
		text = self.label.text()
		print(text[:len(text)-1])
		self.label.setText(text[:len(text)-1])

	def action_clear(self):
		# printing presse
		self.label.setText("")

	def action_equal(self):

		# get the label text
		equation = self.label.text()

		try:
			# getting the ans
			ans = eval(equation)

			# setting text to the label
			self.label.setText(str(ans))

		except:
			# setting text to the label
			self.label.setText("Wrong Input")
		     

# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
