# MIT License

# Copyright (c) 2020 Bo Kamphues

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from PySide2.QtWidgets import QMainWindow
from cabinet import __version__


class MainWindow(QMainWindow):
    # the main cabinet window

    def __init__(self, parent=None):
        # initializes the main cabinet window

        # run parent class initialization first
        super(MainWindow, self).__init__(parent)

        # general window data
        self.setWindowTitle("Cabinet %s" % __version__)
        self.setMinimumSize(800, 500)

        # menu setup
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("Manage")

        # end initialization by calling the window
        self.show()