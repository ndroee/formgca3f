from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd


class Ui_FormGca3F(object):
    def setupUi(self, FormGca3F):
        FormGca3F.setObjectName("FormGca3F")
        FormGca3F.resize(787, 671)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main/home_1946488.png"),
                       QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FormGca3F.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(parent=FormGca3F)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 321, 201))
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.txtAsal = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtAsal.setObjectName("txtAsal")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtAsal)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.txtLok = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtLok.setObjectName("txtLok")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtLok)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.txtSiteID = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtSiteID.setObjectName("txtSiteID")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtSiteID)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.txtLapis = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtLapis.setObjectName("txtLapis")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtLapis)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.txtBulan = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtBulan.setObjectName("txtBulan")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBulan)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.txtBrtTbg = QtWidgets.QLineEdit(parent=self.groupBox)
        self.txtBrtTbg.setObjectName("txtBrtTbg")
        self.formLayout.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtTbg)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading |
                                QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=FormGca3F)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 140, 243, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.txtBrtP48 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtBrtP48.setObjectName("txtBrtP48")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtP48)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.txtBrtP100 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtBrtP100.setObjectName("txtBrtP100")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtP100)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.txtBrtM100 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtBrtM100.setObjectName("txtBrtM100")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtBrtM100)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.txtTotBrt = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.txtTotBrt.setObjectName("txtTotBrt")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.txtTotBrt)
        self.btnOk = QtWidgets.QPushButton(parent=FormGca3F)
        self.btnOk.setGeometry(QtCore.QRect(450, 290, 80, 26))
        self.btnOk.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Button/right-arrow_664866.png"),
                        QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnOk.setIcon(icon1)
        self.btnOk.setObjectName("btnOk")
        self.btnUpload = QtWidgets.QPushButton(parent=FormGca3F)
        self.btnUpload.setGeometry(QtCore.QRect(10, 50, 80, 26))
        self.btnUpload.setObjectName("btnUpload")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=FormGca3F)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 320, 321, 281))
        self.groupBox_3.setObjectName("groupBox_3")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox_3)
        self.scrollArea.setGeometry(QtCore.QRect(15, 59, 291, 206))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, -183, 274, 698))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout_5 = QtWidgets.QFormLayout(
            self.scrollAreaWidgetContents)
        self.formLayout_5.setObjectName("formLayout_5")

        minerals = ['', 'Cassiterite', 'Monazite', 'Pyrit/Marc', 'Ilmenite', 'Zircon', 'Xenotime', 'Anatase',
                    'Limonite', 'Topaz', 'Tourmaline', 'Siderite', 'Magnetite', 'Spinel', 'Oksida Besi', 'Lp.Pasir', 'Quartz']

        self.cbM1 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM1.setObjectName("cbM1")
        self.cbM1.addItems(minerals)
        self.formLayout_5.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM1)
        self.leM01 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM01.setObjectName("leM01")
        self.formLayout_5.setWidget(
            0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM01)
        self.cbM2 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM2.setObjectName("cbM2")
        self.cbM2.addItems(minerals)
        self.formLayout_5.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM2)
        self.leM02 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM02.setObjectName("leM02")
        self.formLayout_5.setWidget(
            1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM02)
        self.cbM3 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM3.setObjectName("cbM3")
        self.cbM3.addItems(minerals)
        self.formLayout_5.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM3)
        self.leM03 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM03.setObjectName("leM03")
        self.formLayout_5.setWidget(
            2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM03)
        self.cbM4 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM4.setObjectName("cbM4")
        self.cbM4.addItems(minerals)
        self.formLayout_5.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM4)
        self.leM04 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM04.setObjectName("leM04")
        self.formLayout_5.setWidget(
            3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM04)
        self.cbM5 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM5.setObjectName("cbM5")
        self.cbM5.addItems(minerals)
        self.formLayout_5.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM5)
        self.leM05 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM05.setObjectName("leM05")
        self.formLayout_5.setWidget(
            4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM05)
        self.cbM6 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM6.setObjectName("cbM6")
        self.cbM6.addItems(minerals)
        self.formLayout_5.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM6)
        self.leM06 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM06.setObjectName("leM06")
        self.formLayout_5.setWidget(
            5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM06)
        self.cbM7 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM7.setObjectName("cbM7")
        self.cbM7.addItems(minerals)
        self.formLayout_5.setWidget(
            6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM7)
        self.leM07 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM07.setObjectName("leM07")
        self.formLayout_5.setWidget(
            6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM07)
        self.cbM8 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM8.setObjectName("cbM8")
        self.cbM8.addItems(minerals)
        self.formLayout_5.setWidget(
            7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM8)
        self.leM08 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM08.setObjectName("leM08")
        self.formLayout_5.setWidget(
            7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM08)
        self.cbM9 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM9.setObjectName("cbM9")
        self.cbM9.addItems(minerals)
        self.formLayout_5.setWidget(
            8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM9)
        self.leM09 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM09.setObjectName("leM09")
        self.formLayout_5.setWidget(
            8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM09)
        self.cbM10 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM10.setObjectName("cbM10")
        self.cbM10.addItems(minerals)
        self.formLayout_5.setWidget(
            9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM10)
        self.leM10 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM10.setObjectName("leM10")
        self.formLayout_5.setWidget(
            9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM10)
        self.cbM11 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM11.setObjectName("cbM11")
        self.cbM11.addItems(minerals)
        self.formLayout_5.setWidget(
            10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM11)
        self.leM11 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM11.setObjectName("leM11")
        self.formLayout_5.setWidget(
            10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM11)
        self.cbM12 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM12.setObjectName("cbM12")
        self.cbM12.addItems(minerals)
        self.formLayout_5.setWidget(
            11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM12)
        self.leM12 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM12.setObjectName("leM12")
        self.formLayout_5.setWidget(
            11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM12)
        self.cbM13 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM13.setObjectName("cbM13")
        self.cbM13.addItems(minerals)
        self.formLayout_5.setWidget(
            12, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM13)
        self.leM13 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM13.setObjectName("leM13")
        self.formLayout_5.setWidget(
            12, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM13)
        self.cbM14 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM14.setObjectName("cbM14")
        self.cbM14.addItems(minerals)
        self.formLayout_5.setWidget(
            13, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM14)
        self.leM14 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM14.setObjectName("leM14")
        self.formLayout_5.setWidget(
            13, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM14)
        self.cbM15 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM15.setObjectName("cbM15")
        self.cbM15.addItems(minerals)
        self.formLayout_5.setWidget(
            14, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM15)
        self.leM15 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM15.setObjectName("leM15")
        self.formLayout_5.setWidget(
            14, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM15)
        self.cbM16 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM16.setObjectName("cbM16")
        self.cbM16.addItems(minerals)
        self.formLayout_5.setWidget(
            15, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM16)
        self.leM16 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM16.setObjectName("leM16")
        self.formLayout_5.setWidget(
            15, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM16)
        self.cbM17 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM17.setObjectName("cbM17")
        self.cbM17.addItems(minerals)
        self.formLayout_5.setWidget(
            16, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM17)
        self.leM17 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM17.setObjectName("leM17")
        self.formLayout_5.setWidget(
            16, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM17)
        self.cbM18 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM18.setObjectName("cbM18")
        self.cbM18.addItems(minerals)
        self.formLayout_5.setWidget(
            17, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM18)
        self.leM18 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM18.setObjectName("leM18")
        self.formLayout_5.setWidget(
            17, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM18)
        self.cbM19 = QtWidgets.QComboBox(parent=self.scrollAreaWidgetContents)
        self.cbM19.setObjectName("cbM19")
        self.cbM19.addItems(minerals)
        self.formLayout_5.setWidget(
            18, QtWidgets.QFormLayout.ItemRole.LabelRole, self.cbM19)
        self.leM19 = QtWidgets.QLineEdit(parent=self.scrollAreaWidgetContents)
        self.leM19.setObjectName("leM19")
        self.formLayout_5.setWidget(
            18, QtWidgets.QFormLayout.ItemRole.FieldRole, self.leM19)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(70, 30, 44, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(180, 30, 75, 16))
        self.label_12.setObjectName("label_12")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=FormGca3F)
        self.groupBox_4.setGeometry(QtCore.QRect(370, 320, 350, 281))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.groupBox_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName("gridLayout")
        self.cbSR = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbSR.setObjectName("cbSR")
        self.gridLayout.addWidget(self.cbSR, 2, 1, 1, 1)
        self.cbSA = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbSA.setObjectName("cbSA")
        self.gridLayout.addWidget(self.cbSA, 1, 1, 1, 1)
        self.cbA = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbA.setObjectName("cbA")
        self.gridLayout.addWidget(self.cbA, 1, 0, 1, 1)
        self.cbR = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbR.setObjectName("cbR")
        self.gridLayout.addWidget(self.cbR, 2, 0, 1, 1)
        self.cbWR = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbWR.setObjectName("cbWR")
        self.gridLayout.addWidget(self.cbWR, 3, 0, 1, 1)
        self.cbSASR = QtWidgets.QCheckBox(parent=self.groupBox_5)
        self.cbSASR.setObjectName("cbSASR")
        self.gridLayout.addWidget(self.cbSASR, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.groupBox_4)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbCH = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.rbCH.setObjectName("rbCH")
        self.verticalLayout_2.addWidget(self.rbCH)
        self.rbCM = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.rbCM.setObjectName("rbCM")
        self.verticalLayout_2.addWidget(self.rbCM)
        self.rbCK = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.rbCK.setObjectName("rbCK")
        self.verticalLayout_2.addWidget(self.rbCK)
        self.rbC = QtWidgets.QRadioButton(parent=self.groupBox_6)
        self.rbC.setObjectName("rbC")
        self.verticalLayout_2.addWidget(self.rbC)
        self.verticalLayout.addWidget(self.groupBox_6)

        self.retranslateUi(FormGca3F)
        QtCore.QMetaObject.connectSlotsByName(FormGca3F)

    def retranslateUi(self, FormGca3F):
        _translate = QtCore.QCoreApplication.translate
        FormGca3F.setWindowTitle(_translate("FormGca3F", "Form GCA 3 Fraksi"))
        self.groupBox.setTitle(_translate("FormGca3F", "Informasi Sampel"))
        self.label_2.setText(_translate("FormGca3F", "Lokasi"))
        self.label_3.setText(_translate("FormGca3F", "Site ID"))
        self.label_4.setText(_translate("FormGca3F", "Lapis"))
        self.label_5.setText(_translate("FormGca3F", "Bulan/Tahun"))
        self.label_6.setText(_translate("FormGca3F", "Berat Timbang"))
        self.label.setText(_translate("FormGca3F", "Asal Conto"))
        self.groupBox_2.setTitle(_translate("FormGca3F", "Berat Sampel (gr)"))
        self.label_7.setText(_translate("FormGca3F", "#+48"))
        self.label_8.setText(_translate("FormGca3F", "#+100"))
        self.label_9.setText(_translate("FormGca3F", "#-100"))
        self.label_10.setText(_translate("FormGca3F", "Berat Total"))
        self.btnUpload.setText(_translate("FormGca3F", "Upload"))
        self.groupBox_3.setTitle(_translate(
            "FormGca3F", "Analisa Multi Mineral"))
        self.label_11.setText(_translate("FormGca3F", "Mineral"))
        self.label_12.setText(_translate("FormGca3F", "Jumlah Butir"))
        self.groupBox_4.setTitle(_translate(
            "FormGca3F", "Karakter Cassiterite"))
        self.groupBox_5.setTitle(_translate("FormGca3F", "Bentuk Butir"))
        self.cbSR.setText(_translate("FormGca3F", "Sub Rounded"))
        self.cbSA.setText(_translate("FormGca3F", "Sub Angular"))
        self.cbA.setText(_translate("FormGca3F", "Angular"))
        self.cbR.setText(_translate("FormGca3F", "Rounded"))
        self.cbWR.setText(_translate("FormGca3F", "Well Rounded"))
        self.cbSASR.setText(_translate(
            "FormGca3F", "Sub Angular - Sub Rounded"))
        self.groupBox_6.setTitle(_translate("FormGca3F", "Warna"))
        self.rbCH.setText(_translate("FormGca3F", "Cokelat Kehitaman"))
        self.rbCM.setText(_translate("FormGca3F", "Cokelat Kemerahan"))
        self.rbCK.setText(_translate("FormGca3F", "Cokelat Kekuningan"))
        self.rbC.setText(_translate("FormGca3F", "Kecokelatan"))

        self.btnUpload.clicked.connect(self.on_btnUpload_clicked)

    def on_btnUpload_clicked(self):
            # Membuka jendela dialog untuk memilih file Excel
            filePath, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Unggah File Excel", "",
                                                                "Excel Files (*.xls *.xlsx);;All Files (*)")

            # Memeriksa apakah file Excel dipilih atau tidak
            if filePath:
                # Membaca data dari file Excel menggunakan pandas
                try:
                    data = pd.read_excel(filePath)
                except Exception as e:
                    QtWidgets.QMessageBox.critical(None, "Error", f"Gagal membaca file Excel:\n{str(e)}")
                    return

                # Mengisi form di groupBox "Informasi Sampel" dengan data dari file Excel
                if not data.empty:
                    self.txtAsal.setText(str(data.iloc[0]['Asal Conto']))
                    self.txtLok.setText(str(data.iloc[0]['Lokasi']))
                    self.txtSiteID.setText(str(data.iloc[0]['Site ID']))
                    self.txtLapis.setText(str(data.iloc[0]['Lapis']))
                    self.txtBulan.setText(str(data.iloc[0]['Bulan/Tahun']))
                    self.txtBrtTbg.setText(str(data.iloc[0]['Berat Timbang']))

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        FormGca3F = QtWidgets.QWidget()
        ui = Ui_FormGca3F()
        ui.setupUi(FormGca3F)
        FormGca3F.show()
        sys.exit(app.exec())
