from PyQt5 import QtCore, QtGui, QtWidgets

class GuiLogic(object):
    def __init__(self, num):
        self.yay = num

    def Browse_Button_clicked(self):
        #path = QtWidgets.QFileDialog.getExistingDirectory(gui, 'open directory', 'C:', '')
        print("BROWSE CLICKED! ", self.yay)
