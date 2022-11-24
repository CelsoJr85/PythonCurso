"""PyQT5"""
# Instalar: pip install pyqt5
# Importações
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout

# Criando
class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        #                           linha, coluna, qt linhas cabe o bt, qt colunas
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        # Editando o botão com um CSS
        self.btn.setStyleSheet('font-size: 15px;')
        # Colocando um evento/ação no botão
        self.btn.clicked.connect(lambda: print("Olá mundo!"))
        self.setCentralWidget(self.cw)


# Inicializando
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
