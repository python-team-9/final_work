import sys
sys.path.append('../Logup/')
sys.path.append('../user/')

import LogupWindow as logup
import UserWindow as user
import BOOS as boss

from PyQt5.QtWidgets import QApplication, QMainWindow

class mainWindows:
    def __init__(self):
        self.logupW = logup.LoadingWindow()
        self.logupW.switch.connect(self.switchWindows)
        self.logupW.show()

    def switchWindows(self):
        self.client = self.logupW.client
        self.id = self.logupW.userid
        self.password = self.logupW.password
        self.username = self.logupW.username
        self.identity = self.logupW.identity
        self.logupW.close()
        if self.identity == 'users':
            self.userW = user.UserWindow(self.client, self.id, self.password, self.username, self.identity)
            self.userW.show()

        elif self.identity == 'bosses':
            print("登录boss")

        else:
            print("登录managers")


if __name__=="__main__":
    app = QApplication(sys.argv)
    main = mainWindows()
    sys.exit(app.exec_())
