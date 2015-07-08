# Want to profile a script
# Pull up a homebrewed code editor [show the code path]
# using the profile, overlay colors onto our code editor

import sys
import os
import argparse
import profile
import cProfile
from PyQt5 import QtGui, QtWidgets, QtCore
import test_module
import python_syntax


if __name__ == '__main__':
    """
    # NOTE: This totally works
    parser = argparse.ArgumentParser(description='Hand me a file')
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename) as file:
        file_string = file.read()
    text_document = QtGui.QTextDocument(file_string)
    """
    p = cProfile.Profile()
    p.enable()
    test_module.primes(10001)
    test_module.main()
    p.disable()
    print(dir(p))

    stats = p.getstats()
    
    # code object, callcount, reccallcount, totaltime, inlinetime, calls
    # calls in the layer of recursion

    # NOTE: recallcount is recursive count
    # don't think we're concerned with the time aspect
    
    # code objects are strings, need to build a parser for that

    # 1. Get call metadata, and display that in text edit
    # 2. Get subcall code object
        # 2.a determine if new file
        # 2.a.1 get new file contents
    # repeat
        # TODO: explore the code object. Need to understand if can get
        # some metadata from that object
    p.print_stats()

    #python_syntax.PythonHighlighter(text_document)

    # we'll split from here, profile the file
    # look into profiler, especially how the data is stored




    # also going to load it in our text edit
    profile.run('function()', args.filename)
    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()
    text_edit = QtWidgets.QTextEdit(parent=main_window)
    text_edit.setDocument(text_document)
    text_edit.setFont(QtGui.QFont("Times", 12))
    main_window.setCentralWidget(text_edit)
    main_window.show()

    sys.exit(app.exec_())
