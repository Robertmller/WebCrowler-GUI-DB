#Montagem da interface gráfica

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel


app = QApplication(sys.argv)

# Formatando a janela
janela = QWidget()
janela.resize(800, 600)
janela.setWindowTitle("Resultado dos dados")

btn = QPushButton("Nome do botão", janela)
# Posição do botão eixo X,Y, largura, altura
btn.setGeometry(5, 5, 100, 40)
btn.setStyleSheet('background-color:gray; color:black')


# Exibi a janela
janela.show()

# Executa a janela
app.exec()
