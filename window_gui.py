import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

setting_val = []

class MainWindow(QWidget):  # 창을 만들 QWidget 클래스를 상속 받음
    def __init__(self):  # constructor
        super().__init__()
        # self.setStyleSheet("color:white;background-color:grey;")
        self.initUI()

    def initUI(self):
        # self.lbl_navy = QLabel()
        # self.lbl_navy.setStyleSheet("background-color:navy")

        self.pixmap = QPixmap("broad_tec.png")
        self.pixmap = self.pixmap.scaledToWidth(220)
        self.corp_img = QLabel()
        self.corp_img.setPixmap(QPixmap(self.pixmap))

        self.version_txt = QLabel(' Antenna Measure Software V1.0')
        self.font1 = self.version_txt.font()
        self.font1.setPointSize(13)
        self.font1.setBold(True)
        self.version_txt.setFont(self.font1)

        #self.setting_result = QTableView()
        self.setting_result = QTableWidget()
        #self.setting_result.resize(100, 100)
        #self.setting_result.verticalHeader().SetSectionResizeMode(QHeaderView.Stretch)
        self.setting_result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.setting_result.setRowCount(8)
        self.setting_result.setColumnCount(1)
        self.setting_result.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.set_table_data()

        self.result_lbl = QLabel('Pass or Fail')
        self.result_lbl.setAlignment(Qt.AlignCenter)

        self.measure_result = QTableView()

        self.btn_measure = QPushButton('Measure')
        self.btn_measure.resize(100, 40)
        self.btn_measure.setToolTip('Measure')

        self.btn_disconnect = QPushButton('Disconnect')
        self.btn_disconnect.resize(100, 40)
        self.btn_disconnect.setToolTip('Disconnect')

        self.btn_connect = QPushButton('Connection')
        self.btn_connect.resize(100, 40)
        self.btn_connect.setToolTip('Connection')
        self.btn_connect.clicked.connect(self.clicked_connect)

        self.btn_setting = QPushButton('Setting')
        self.btn_setting.resize(100, 40)
        self.btn_setting.setToolTip('Setting')
        self.btn_setting.clicked.connect(self.clicked_setting)

        self.btn_calib = QPushButton('Calibration')
        self.btn_calib.resize(100, 40)
        self.btn_calib.setToolTip('Calibration')

        self.btn_result = QPushButton('Result')
        self.btn_result.resize(100, 40)
        self.btn_result.setToolTip('Result')

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.corp_img)
        self.hbox.addWidget(self.version_txt)
        self.hbox.addStretch(1)  # stretch 설정 위치에 따라 버튼 위치도 변경됨
        self.hbox.addWidget(self.btn_connect)
        self.hbox.addWidget(self.btn_setting)
        self.hbox.addWidget(self.btn_calib)
        self.hbox.addWidget(self.btn_result)

        self.qbox1 = QBoxLayout(QBoxLayout.TopToBottom)
        self.qbox1_sub = QBoxLayout(QBoxLayout.LeftToRight)
        self.qbox2 = QBoxLayout(QBoxLayout.TopToBottom)
        self.qbox2_sub = QBoxLayout(QBoxLayout.LeftToRight)

        self.qbox1.addSpacing(10)
        self.qbox1.addLayout(self.hbox)
        self.qbox1.addSpacing(20)
        self.qbox1.addLayout(self.qbox1_sub)

        self.qbox1_sub.addLayout(self.qbox2)
        self.qbox1_sub.addWidget(self.measure_result, 75)

        self.setting_result.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        vert = self.setting_result.verticalHeader()
        self.setting_result.setMaximumHeight(vert.length() + 30)
        self.setting_result.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.qbox2.addWidget(self.setting_result)
        #vert_space = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Expanding)#
        #self.qbox2.addItem(vert_space)
        self.qbox2.addSpacing(20)
        self.qbox2.addWidget(self.result_lbl)
        self.qbox2.addLayout(self.qbox2_sub)
        self.qbox2.addSpacing(40)

        self.qbox2_sub.addWidget(self.btn_measure)
        self.qbox2_sub.addWidget(self.btn_disconnect)

        self.setLayout(self.qbox1)
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle('Antenna Measure Software V1.0')
        self.center()
        self.show()

    def set_table_data(self):
        row_header = ['Start Frequency', 'Stop Frequency', 'Measure', 'Power',
                      'Bandwidth', 'Number of Point', 'Measure Result', 'Limit Setting']
        col_header = ['Val.']
        self.setting_result.setVerticalHeaderLabels(row_header)
        self.setting_result.setHorizontalHeaderLabels(col_header)
        '''
        for i, j in setting_val.item():
            row = row_idx_lookup[i]
            for col, val in enumerate(j):
                item = QTableWidgetItem(val)
                if col == 2:
                  item.setTextAlignment(Qt.AlignCenter | Qt.AlignRight)
                    
                self.setting_result.setItem(col, row, item)
        '''

    def clicked_connect(self):
        settingConnect(self)

    def clicked_setting(self):
        settingDialog(self)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, QCloseEvent):
        self.answer = QMessageBox.question("종료 확인", "Are you sure want to exit?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if self.answer == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


class settingConnect(QDialog):
    def __init__(self, parent):
        super(settingConnect, self).__init__(parent)
        self.settingUI()
        self.setGeometry(900, 500, 100, 100)
        self.setWindowTitle("Instrument Connection")
        self.show()

    def settingUI(self):
        hLayout = QHBoxLayout()
        lbl1 = QLabel("IP Address ")
        hLayout.addWidget(lbl1)
        ip1 = QLineEdit()
        hLayout.addWidget(ip1)
        lbl2 = QLabel('.')
        hLayout.addWidget(lbl2)
        ip2 = QLineEdit()
        hLayout.addWidget(ip2)
        lbl3 = QLabel('.')
        hLayout.addWidget(lbl3)
        ip3 = QLineEdit()
        hLayout.addWidget(ip3)
        lbl4 = QLabel('.')
        hLayout.addWidget(lbl4)
        ip4 = QLineEdit()
        hLayout.addWidget(ip4)

        h2Layout = QHBoxLayout()
        self.btn_ok = QPushButton("OK")
        self.btn_cancel = QPushButton("Cancel")
        h2Layout.addWidget(self.btn_ok)
        h2Layout.addWidget(self.btn_cancel)

        vLayout = QVBoxLayout()
        vLayout.addLayout(hLayout)
        vLayout.addLayout(h2Layout)

        self.setLayout(vLayout)


class settingDialog(QDialog):
    def __init__(self, parent):
        super(settingDialog, self).__init__(parent)
        self.settingUI()
        self.show()

    def settingUI(self):
        self.setWindowTitle('Setting')
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()

        self.start_frq = QLineEdit()
        formLayout.addRow('Start Frequency: ', self.start_frq)
        self.stop_frq = QLineEdit()
        formLayout.addRow('Stop Frequency: ', self.stop_frq)
        self.measure = QLineEdit()
        formLayout.addRow('Measure: ', self.measure)
        self.power = QLineEdit()
        formLayout.addRow('Power: ', self.power)
        self.bandwidth = QLineEdit()
        formLayout.addRow('Bandwidth: ', self.bandwidth)
        self.num_of_point = QLineEdit()
        formLayout.addRow('Number of Point: ', self.num_of_point)
        self.measure_result = QLineEdit()
        formLayout.addRow('Measure Result: ', self.measure_result)
        self.limit_setting = QLineEdit()
        formLayout.addRow('Limit Setting: ', self.limit_setting)
        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)

        self.setLayout(dlgLayout)

        self.start_frq.textChanged.connect(self.inputValue_startfq)
        self.stop_frq.textChanged.connect(self.inputValue_stopfq)
        self.measure.textChanged.connect(self.inputValue_ms)
        self.power.textChanged.connect(self.inputValue_pw)
        self.bandwidth.textChanged.connect(self.inputValue_bw)
        self.num_of_point.textChanged.connect(self.inputValue_nop)
        self.measure_result.textChanged.connect(self.inputValue_mr)
        self.limit_setting.textChanged.connect(self.inputValue_ls)

    def inputValue_startfq(self, text):
        setting_val.insert(0, text)
    def inputValue_stopfq(self, text):
        setting_val.insert(1, text)
    def inputValue_ms(self, text):
        setting_val.insert(2, text)
    def inputValue_pw(self, text):
        setting_val.insert(3, text)
    def inputValue_bw(self, text):
        setting_val.insert(4, text)
    def inputValue_nop(self, text):
        setting_val.insert(5, text)
    def inputValue_mr(self, text):
        setting_val.insert(6, text)
    def inputValue_ls(self, text):
        setting_val.insert(7, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 어플리케이션 객체 생성, sys.argv: 커맨드라인으로 인수를 받을 때 제어 관련
    mw = MainWindow()  # 내가 만든 창 객체
    sys.exit(app.exec_())  # 나갈떄, app.exec_: 이벤트 처리를 위한 메인 루프 실행