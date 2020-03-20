"""
Copyright 2020 Mohamed Amgd

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

"""
from PyQt5 import QtCore, QtGui, QtWidgets
from Process import process
from collections import OrderedDict
import main


class Ui_MainWindow(object):
    process_dic = OrderedDict()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 596)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 411, 301))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.p_name = QtWidgets.QLineEdit(self.centralwidget)
        self.p_name.setGeometry(QtCore.QRect(620, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p_name.setFont(font)
        self.p_name.setObjectName("p_name")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.p_arrival = QtWidgets.QLineEdit(self.centralwidget)
        self.p_arrival.setGeometry(QtCore.QRect(620, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p_arrival.setFont(font)
        self.p_arrival.setObjectName("p_arrival")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.p_burst = QtWidgets.QLineEdit(self.centralwidget)
        self.p_burst.setGeometry(QtCore.QRect(620, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.p_burst.setFont(font)
        self.p_burst.setObjectName("p_burst")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(470, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.add_p = QtWidgets.QPushButton(self.centralwidget)
        self.add_p.setGeometry(QtCore.QRect(510, 180, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_p.setFont(font)
        self.add_p.setObjectName("add_p")
        self.add_p.clicked.connect(self.add)

        self.remove_p = QtWidgets.QPushButton(self.centralwidget)
        self.remove_p.setGeometry(QtCore.QRect(510, 240, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.remove_p.setFont(font)
        self.remove_p.setObjectName("remove_p")
        self.remove_p.clicked.connect(self.remove)

        self.fcfs = QtWidgets.QPushButton(self.centralwidget)
        self.fcfs.setGeometry(QtCore.QRect(10, 330, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fcfs.setFont(font)
        self.fcfs.setObjectName("fcfs")
        self.fcfs.clicked.connect(self.fcfs_clicked)

        self.sjf = QtWidgets.QPushButton(self.centralwidget)
        self.sjf.setGeometry(QtCore.QRect(110, 330, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sjf.setFont(font)
        self.sjf.setObjectName("sjf")
        self.sjf.clicked.connect(self.sjf_clicked)

        self.srtf = QtWidgets.QPushButton(self.centralwidget)
        self.srtf.setGeometry(QtCore.QRect(190, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.srtf.setFont(font)
        self.srtf.setObjectName("srtf")
        self.srtf.clicked.connect(self.srtf_clicked)

        self.rr = QtWidgets.QPushButton(self.centralwidget)
        self.rr.setGeometry(QtCore.QRect(10, 370, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rr.setFont(font)
        self.rr.setObjectName("rr")
        self.rr.clicked.connect(self.rr_clicked)

        self.q = QtWidgets.QLineEdit(self.centralwidget)
        self.q.setGeometry(QtCore.QRect(130, 370, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.q.setFont(font)
        self.q.setObjectName("q")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 370, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 420, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(380, 420, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.avg_w = QtWidgets.QLCDNumber(self.centralwidget)
        self.avg_w.setGeometry(QtCore.QRect(190, 420, 161, 41))
        self.avg_w.setObjectName("avg_w")

        self.avg_t = QtWidgets.QLCDNumber(self.centralwidget)
        self.avg_t.setGeometry(QtCore.QRect(590, 420, 161, 41))
        self.avg_t.setObjectName("avg_t")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 26))
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
        self.label.setText(_translate("MainWindow", "Process Name : "))
        self.label_2.setText(_translate("MainWindow", "Arrival Time : "))
        self.label_3.setText(_translate("MainWindow", "Burst Time : "))
        self.add_p.setText(_translate("MainWindow", "Add Process"))
        self.remove_p.setText(_translate("MainWindow", "Remove Process"))
        self.fcfs.setText(_translate("MainWindow", "FCFS"))
        self.sjf.setText(_translate("MainWindow", "SJF"))
        self.srtf.setText(_translate("MainWindow", "SRTF"))
        self.rr.setText(_translate("MainWindow", "RR"))
        self.label_4.setText(_translate("MainWindow", "Q :"))
        self.label_5.setText(_translate("MainWindow", "Average Waiting :"))
        self.label_6.setText(_translate("MainWindow", "Average Turn around :"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arrival"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Burst"))

    def add(self):
        rowPosition = self.tableWidget.rowCount()
        name = self.p_name.text()
        if name == "":
            self.show_popup("Process name cannot be empty")
            return None
        try:
            arrival = int(self.p_arrival.text())
            burst = int(self.p_burst.text())
        except:
            self.show_popup("Arrival time and Burst time should be integers")
            return None
        if arrival < 0:
            self.show_popup("Arrival should be more than or equal zero")
            return None
        if burst <= 0:
            self.show_popup("Burst should be more than zero")
            return None
        if name in self.process_dic:
            self.show_popup("Process already exists")
            return None
        self.process_dic[name] = process(int(arrival), int(burst))
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(
            rowPosition, 0, QtWidgets.QTableWidgetItem("{}".format(name)))
        self.tableWidget.setItem(
            rowPosition, 1, QtWidgets.QTableWidgetItem("{}".format(arrival)))
        self.tableWidget.setItem(
            rowPosition, 2, QtWidgets.QTableWidgetItem("{}".format(burst)))

    def remove(self):
        rowPosition = self.tableWidget.rowCount() - 1
        self.tableWidget.removeRow(rowPosition)
        if len(self.process_dic) == 0:
            self.show_popup("There is no Processes to be removed")
            return None
        self.process_dic.popitem()

    def fcfs_clicked(self):
        if len(self.process_dic) == 0:
            self.show_popup("There is no Processes")
            return None
        input_FCFS = dict()
        for i in self.process_dic:
            input_FCFS[i] = process(
                self.process_dic[i].getArrival(), self.process_dic[i].getBurst())
        result = main.FCFS(
            dict(sorted(input_FCFS.items(), key=lambda x: x[1].getArrival())))
        main.printAlgo(result)
        self.avg_w.display(main.avgWaiting(result))
        self.avg_t.display(main.avgTurnAround(result))

    def sjf_clicked(self):
        if len(self.process_dic) == 0:
            self.show_popup("There is no Processes")
            return None
        input_SJF = dict()
        for i in self.process_dic:
            input_SJF[i] = process(
                self.process_dic[i].getArrival(), self.process_dic[i].getBurst())
        result = main.SJF(
            dict(sorted(input_SJF.items(), key=lambda x: x[1].getArrival())))
        main.printAlgo(result)
        self.avg_w.display(main.avgWaiting(result))
        self.avg_t.display(main.avgTurnAround(result))

    def srtf_clicked(self):
        if len(self.process_dic) == 0:
            self.show_popup("There is no Processes")
            return None
        input_SRTF = dict()
        for i in self.process_dic:
            input_SRTF[i] = process(
                self.process_dic[i].getArrival(), self.process_dic[i].getBurst())
        result = main.SRTF(
            dict(sorted(input_SRTF.items(), key=lambda x: x[1].getArrival())))
        main.printAlgo(result)
        self.avg_w.display(main.avgWaiting(result))
        self.avg_t.display(main.avgTurnAround(result))

    def rr_clicked(self):
        if self.q.text() == "":
            self.show_popup("Q cannot be empty")
            return None
        try:
            q = int(self.q.text())
        except:
            self.show_popup("Q should be integer")
            return None
        if q <= 0:
            self.show_popup("Q should be more than zero")
            return None
        if len(self.process_dic) == 0:
            self.show_popup("There is no Processes")
            return None
        input_RR = dict()
        for i in self.process_dic:
            input_RR[i] = process(
                self.process_dic[i].getArrival(), self.process_dic[i].getBurst())
        result = main.RR(
            dict(sorted(input_RR.items(), key=lambda x: x[1].getArrival())), q)
        main.printAlgo(result)
        self.avg_w.display(main.avgWaiting(result))
        self.avg_t.display(main.avgTurnAround(result))

    def show_popup(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText(text)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Close)
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
