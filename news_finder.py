from bs4 import BeautifulSoup
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



class Ui_news_finder(object):
    soup = BeautifulSoup()
    all_news = soup.find()
    def setupUi(self, news_finder):
        news_finder.setObjectName("news_finder")
        news_finder.resize(1114, 829)
        news_finder.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit1 = QtWidgets.QTextEdit(news_finder)
        self.textEdit1.setGeometry(QtCore.QRect(70, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.textEdit1.setFont(font)
        self.textEdit1.setObjectName("textEdit1")
        self.pushButton = QtWidgets.QPushButton(news_finder)
        self.pushButton.setGeometry(QtCore.QRect(70, 90, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget1 = QtWidgets.QTableWidget(news_finder)
        self.tableWidget1.setGeometry(QtCore.QRect(70, 140, 451, 681))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.tableWidget1.setFont(font)
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(3)
        self.tableWidget1.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget1.setHorizontalHeaderItem(2, item)
        self.textEdit3 = QtWidgets.QTextEdit(news_finder)
        self.textEdit3.setGeometry(QtCore.QRect(610, 410, 471, 401))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.textEdit3.setFont(font)
        self.textEdit3.setObjectName("textEdit3")
        self.textEdit2 = QtWidgets.QTextEdit(news_finder)
        self.textEdit2.setGeometry(QtCore.QRect(610, 290, 471, 81))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.textEdit2.setFont(font)
        self.textEdit2.setObjectName("textEdit2")
        self.label = QtWidgets.QLabel(news_finder)
        self.label.setGeometry(QtCore.QRect(790, 130, 271, 141))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Project/default-news.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(news_finder)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(news_finder)
        QtCore.QMetaObject.connectSlotsByName(news_finder)

        self.pushButton.clicked.connect(lambda: self.search())


                

    def retranslateUi(self, news_finder):
        _translate = QtCore.QCoreApplication.translate
        news_finder.setWindowTitle(_translate("news_finder", "Form"))
        self.textEdit1.setHtml(_translate("news_finder", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Consolas\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("news_finder", "Search"))
        item = self.tableWidget1.horizontalHeaderItem(0)
        item.setText(_translate("news_finder", "Title"))
        item = self.tableWidget1.horizontalHeaderItem(1)
        item.setText(_translate("news_finder", "Update at"))
        item = self.tableWidget1.horizontalHeaderItem(2)
        item.setText(_translate("news_finder", "Picture"))
        self.label_2.setText(_translate("news_finder", "NEWS FINDER"))
        
        #edited my myself
        self.textEdit1.setPlaceholderText("Type here to search")
        self.textEdit2.setPlaceholderText("Title")
        self.textEdit2.setReadOnly(True)
        self.textEdit3.setPlaceholderText("Full news") 
        self.textEdit3.setReadOnly(True)

    
    #functions

    def add_item_tableWidget(self):
        self.tableWidget1.setRowCount(0)
        row=0
        self.tableWidget1.setRowCount(len(self.all_news))

        for news in self.all_news:
            news_title = news.find('a').text
            upload_time = news.find('time', class_='published-time publishedAt-m__published-at__2eHYg').text
            self.tableWidget1.setItem(row, 0, QtWidgets.QTableWidgetItem(news_title))
            self.tableWidget1.setItem(row, 1, QtWidgets.QTableWidgetItem(upload_time))
            row=row+1


    def search(self):
        if self.textEdit1.toPlainText()=="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning )
            msg.setText("Please type something")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        
        else:
            key = self.textEdit1.toPlainText()
            link='https://en.prothomalo.com/search?q='+key
            html_text = requests.get(link).text
            self.soup = BeautifulSoup(html_text, 'lxml')
            self.all_news = self.soup.find_all('div', class_='content-area')
            self.add_item_tableWidget()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    news_finder = QtWidgets.QWidget()
    ui = Ui_news_finder()
    ui.setupUi(news_finder)
    news_finder.show()
    sys.exit(app.exec_())
