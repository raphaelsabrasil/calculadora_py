from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        #configurando o layout básico
        self.cw = QWidget()             # self é 'window' em main.py
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        #título da janela
        self.setWindowTitle('Calculadora')
        

    def adjustFixedSize(self):
        #última coisa a ser feita
        self.adjustSize()       # ajuste da tela
        self.setFixedSize(self.width(), self.height())  # fixa tamanho da tela

    # def addToVLayout(self, widget: QWidget):
    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    def makeMsgBox(self):
        return QMessageBox(self)    # self é o parent, o MainWindow da QMessageBox
        