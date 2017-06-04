from PyQt5.QtWidgets import QWidget, QFileDialog


class Logic(QWidget):
    def __init__(self):
        super().__init__()

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
