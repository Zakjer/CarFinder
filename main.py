from PyQt5 import QtCore, QtGui, QtWidgets
import CarFinder

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 713)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.car_model = QtWidgets.QLineEdit(self.centralwidget)
        self.car_model.setGeometry(QtCore.QRect(420, 150, 161, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.car_model.setFont(font)
        self.car_model.setObjectName("car_model")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(460, 120, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(430, 340, 141, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search.setFont(font)
        self.search.setObjectName("search")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 190, 621, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.min_mileage = QtWidgets.QLineEdit(self.centralwidget)
        self.min_mileage.setGeometry(QtCore.QRect(240, 280, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.min_mileage.setFont(font)
        self.min_mileage.setObjectName("min_mileage")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 250, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.max_mileage = QtWidgets.QLineEdit(self.centralwidget)
        self.max_mileage.setGeometry(QtCore.QRect(380, 280, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.max_mileage.setFont(font)
        self.max_mileage.setObjectName("max_mileage")

        self.min_year = QtWidgets.QLineEdit(self.centralwidget)
        self.min_year.setGeometry(QtCore.QRect(510, 280, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.min_year.setFont(font)
        self.min_year.setText("")
        self.min_year.setObjectName("min_year")

        self.max_year = QtWidgets.QLineEdit(self.centralwidget)
        self.max_year.setGeometry(QtCore.QRect(640, 280, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.max_year.setFont(font)
        self.max_year.setObjectName("max_year")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 250, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 250, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(660, 250, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(600, 360, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Car model"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.label_2.setText(_translate("MainWindow", "Specify details about the car (if you don\'t want to do it then leave the boxes empty)"))
        self.label_3.setText(_translate("MainWindow", "Min. mileage"))
        self.label_4.setText(_translate("MainWindow", "Max. mileage"))
        self.label_5.setText(_translate("MainWindow", "Min. year"))
        self.label_6.setText(_translate("MainWindow", "Max. year"))
        self.checkBox.setText(_translate("MainWindow", "Create excel file with output"))

        self.search.clicked.connect(self.search_car)


    def search_car(self):
            try:
                car_model = self.car_model.text()
            except:
                car_model = ""
            try:
                min_year = int(self.min_year.text())
            except:
                min_year = 0
            try:
                max_year = int(self.max_year.text())
            except:
                max_year = 9999
            try:
                min_mileage = int(self.min_mileage.text())
            except:
                min_mileage = 0
            try:
                max_mileage = int(self.max_mileage.text())
            except:
                max_mileage = 999999

            create_excel_file = False
            if self.checkBox.isChecked():
                create_excel_file = True

            if car_model:
                CarFinder.search_car(car_model, min_year, max_year, min_mileage, max_mileage, create_excel_file)
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(958, 713)

#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")

#         self.car_model = QtWidgets.QLineEdit(self.centralwidget)
#         self.car_model.setGeometry(QtCore.QRect(360, 140, 161, 22))
#         self.car_model.setObjectName("car_model")

#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(390, 110, 91, 21))
#         self.label.setObjectName("label")

#         self.search = QtWidgets.QPushButton(self.centralwidget)
#         self.search.setGeometry(QtCore.QRect(390, 330, 111, 51))
#         self.search.setObjectName("search")

#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(200, 190, 481, 41))
#         self.label_2.setObjectName("label_2")

#         self.min_mileage = QtWidgets.QLineEdit(self.centralwidget)
#         self.min_mileage.setGeometry(QtCore.QRect(200, 260, 113, 22))
#         self.min_mileage.setObjectName("min_mileage")

#         self.label_3 = QtWidgets.QLabel(self.centralwidget)
#         self.label_3.setGeometry(QtCore.QRect(220, 240, 81, 16))
#         self.label_3.setObjectName("label_3")

#         self.max_mileage = QtWidgets.QLineEdit(self.centralwidget)
#         self.max_mileage.setGeometry(QtCore.QRect(340, 260, 113, 22))
#         self.max_mileage.setObjectName("max_mileage")

#         self.min_year = QtWidgets.QLineEdit(self.centralwidget)
#         self.min_year.setGeometry(QtCore.QRect(470, 260, 113, 22))
#         self.min_year.setObjectName("min_year")

#         self.max_year = QtWidgets.QLineEdit(self.centralwidget)
#         self.max_year.setGeometry(QtCore.QRect(590, 260, 113, 22))
#         self.max_year.setObjectName("max_year")

#         self.label_4 = QtWidgets.QLabel(self.centralwidget)
#         self.label_4.setGeometry(QtCore.QRect(360, 240, 81, 16))
#         self.label_4.setObjectName("label_4")

#         self.label_5 = QtWidgets.QLabel(self.centralwidget)
#         self.label_5.setGeometry(QtCore.QRect(500, 240, 55, 16))
#         self.label_5.setObjectName("label_5")

#         self.label_6 = QtWidgets.QLabel(self.centralwidget)
#         self.label_6.setGeometry(QtCore.QRect(620, 240, 55, 16))
#         self.label_6.setObjectName("label_6")

#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 26))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "Type car model"))
#         self.search.setText(_translate("MainWindow", "Search"))
#         self.label_2.setText(_translate("MainWindow", "Specify details about the car (if you don\'t want to do it then leave the boxes empty)"))
#         self.label_3.setText(_translate("MainWindow", "Min. mileage"))
#         self.label_4.setText(_translate("MainWindow", "Max. mileage"))
#         self.label_5.setText(_translate("MainWindow", "Min. year"))
#         self.label_6.setText(_translate("MainWindow", "Max. year"))

#         self.search.clicked.connect(self.search_car)

#     def search_car(self):
#         try:
#             car_model = self.car_model.text()
#         except:
#             car_model = ""
#         try:
#             min_year = int(self.min_year.text())
#         except:
#             min_year = 0
#         try:
#             max_year = int(self.max_year.text())
#         except:
#             max_year = 9999
#         try:
#             min_mileage = int(self.min_mileage.text())
#         except:
#             min_mileage = 0
#         try:
#             max_mileage = int(self.max_mileage.text())
#         except:
#             max_mileage = 999999

#         if car_model:
#             CarFinder.search_car(car_model, min_year, max_year, min_mileage, max_mileage)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())