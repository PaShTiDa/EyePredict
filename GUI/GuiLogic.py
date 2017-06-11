from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5 import QtCore, QtWidgets


class Logic(QWidget):
    def __init__(self, gui):
        super().__init__()
        self.gui = gui
        #self.data_manger = DataManager(self)

    def browse_directory(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        path = QFileDialog.getExistingDirectory(self, "Choose main directory", "", options=options)
        if path:
            print(path)

    def browse_txt_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Load configuration", "",
                                                  "Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)


    def save_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def set_display_data(self, df):
        '''
        :param df: a DataFrame 
        :return: 
        '''

        self.gui.DataTable.setColumnCount(len(df.columns))
        self.gui.DataTable.setRowCount(len(df.index))
        _translate = QtCore.QCoreApplication.translate

        # set headers
        i=0
        for header in df:
            item = QtWidgets.QTableWidgetItem()
            item.setText(_translate("MainWindow", header))
            self.gui.DataTable.setHorizontalHeaderItem(i, item)
            i+=1

        # set content
        for i in range(len(df.index)):
            for j in range(len(df.columns)):
                item = QtWidgets.QTableWidgetItem()
                item.setText(_translate("MainWindow", str(df.iat[i, j])))
                self.gui.DataTable.setItem(i, j, item)

        self.gui.DataTable.resizeColumnsToContents()
        self.gui.DataTable.resizeRowsToContents()

    def FilterData(self):
        query = self.gui.ConfigurationTextEdit.toPlainText()
