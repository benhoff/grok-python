# Want to profile a script
# Pull up a homebrewed code editor [show the code path]
# using the profile, overlay colors onto our code editor

import sys, os
from PyQt5 import QtGui, QtWidgets, QtCore


app = QtWidgets.QApplication(sys.argv)

main_window = QtWidgets.QMainWindow()
text_edit = QtWidgets.QTextEdit(parent=main_window)
main_window.setCentralWidget(text_edit)
main_window.show()

sys.exit(app.exec_())
