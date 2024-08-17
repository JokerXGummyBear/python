from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CalculatorProject(object):

    def __init__(self):
        self.current_input = ""
        self.operation = ""
        self.result = ""

    def setupUi(self, CalculatorProject):
        CalculatorProject.setObjectName("CalculatorProject")
        CalculatorProject.resize(408, 573)
        self.centralwidget = QtWidgets.QWidget(parent=CalculatorProject)
        self.centralwidget.setObjectName("centralwidget")

        # Sets up the layout
        self.grid_layout = QtWidgets.QGridLayout(self.centralwidget)
        self.grid_layout.setObjectName("grid_layout")

        self.lcdNumber = QtWidgets.QLCDNumber(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setObjectName("lcdNumber")
        self.grid_layout.addWidget(self.lcdNumber, 0, 0, 1, 4)

        # Creates the buttons for calculator
        buttons = {
            'C': (1, 0, 1, 1), 'DEL': (1, 1, 1, 1), 'MODE': (1, 2, 1, 1), '+': (1, 3, 1, 1),
            '7': (2, 0, 1, 1), '8': (2, 1, 1, 1), '9': (2, 2, 1, 1), '/': (2, 3, 1, 1),
            '4': (3, 0, 1, 1), '5': (3, 1, 1, 1), '6': (3, 2, 1, 1), '*': (3, 3, 1, 1),
            '1': (4, 0, 1, 1), '2': (4, 1, 1, 1), '3': (4, 2, 1, 1), '-': (4, 3, 1, 1),
            '0': (5, 0, 1, 1), '.': (5, 1, 1, 1), '=': (5, 2, 1, 1)
        }

        for text, pos in buttons.items():
            button = QtWidgets.QPushButton(parent=self.centralwidget)
            button.setText(text)
            font = QtGui.QFont()
            font.setPointSize(27)
            font.setBold(True)
            font.setWeight(75)
            button.setFont(font)
            button.setObjectName(text)
            button.clicked.connect(lambda ch, text=text: self.handle_button_click(text))
            self.grid_layout.addWidget(button, pos[0], pos[1], pos[2], pos[3])

        CalculatorProject.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=CalculatorProject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 408, 26))
        self.menubar.setObjectName("menubar")
        CalculatorProject.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=CalculatorProject)
        self.statusbar.setObjectName("statusbar")
        CalculatorProject.setStatusBar(self.statusbar)

        self.retranslateUi(CalculatorProject)
        QtCore.QMetaObject.connectSlotsByName(CalculatorProject)

    def retranslateUi(self, CalculatorProject):
        _translate = QtCore.QCoreApplication.translate
        CalculatorProject.setWindowTitle(_translate("CalculatorProject", "Calculator"))

    def handle_button_click(self, text):  # what to do when something other than a number is clicked
        if text == 'C':
            self.clear_display()
        elif text == 'DEL':
            self.delete_last()
        elif text in ('+', '-', '*', '/'):
            self.set_operation(text)
        elif text == '=':
            self.calculate()
        else:
            self.add_to_expression(text)

    def add_to_expression(self, value):  # to keep counting up or down
        self.current_input += str(value)
        self.lcdNumber.display(self.current_input)

    def set_operation(self, operator):  # choose between + - * /
        if self.current_input != "":
            self.operation = operator
            self.result = self.current_input
            self.current_input = ""
        self.lcdNumber.display("")

    def calculate(self):  # perform calculations
        if self.current_input != "" and self.operation != "":
            try:
                self.result = str(eval(self.result + self.operation + self.current_input))
                self.lcdNumber.display(self.result)
                self.current_input = self.result
                self.operation = ""
            except Exception:
                self.lcdNumber.display("Error")
                self.current_input = ""
                self.operation = ""

    def clear_display(self):  # to clear the display
        self.current_input = ""
        self.operation = ""
        self.result = ""
        self.lcdNumber.display("")

    def delete_last(self):  # deletes the first digit on the right
        self.current_input = self.current_input[:-1]
        self.lcdNumber.display(self.current_input)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CalculatorProject = QtWidgets.QMainWindow()
    ui = Ui_CalculatorProject()
    ui.setupUi(CalculatorProject)
    CalculatorProject.show()
    sys.exit(app.exec())
