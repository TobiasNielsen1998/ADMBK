import sys
from itertools import *
from PyQt6 import QtWidgets
from ADMBKmenu import ADMBKmenu

def main():
    """
    Setting up ADMBK - press "y" if you want to reset database
    """
    print("Do you want to restart the ADMBK database? -y/n")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sshFile= 'UI/ADMBKstyle.qss'
    with open(sshFile, 'r') as style:
       app.setStyleSheet(style.read())
    window = ADMBKmenu()
    window.show()
    app.exec()
    