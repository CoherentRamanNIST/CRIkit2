# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_KKOptions.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(394, 323)
        Dialog.setStyleSheet("font: 10pt \"Arial\";")
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, -1, -1, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 1, 1, 1)
        self.doubleSpinBoxNRBAmp = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxNRBAmp.setMinimum(-100000.0)
        self.doubleSpinBoxNRBAmp.setMaximum(100000.0)
        self.doubleSpinBoxNRBAmp.setSingleStep(10.0)
        self.doubleSpinBoxNRBAmp.setProperty("value", 0.0)
        self.doubleSpinBoxNRBAmp.setObjectName("doubleSpinBoxNRBAmp")
        self.gridLayout.addWidget(self.doubleSpinBoxNRBAmp, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.doubleSpinBoxCARSAmp = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxCARSAmp.setMinimum(-100000.0)
        self.doubleSpinBoxCARSAmp.setMaximum(100000.0)
        self.doubleSpinBoxCARSAmp.setSingleStep(10.0)
        self.doubleSpinBoxCARSAmp.setProperty("value", 0.0)
        self.doubleSpinBoxCARSAmp.setObjectName("doubleSpinBoxCARSAmp")
        self.gridLayout.addWidget(self.doubleSpinBoxCARSAmp, 4, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 1, 1, 1)
        self.doubleSpinBoxPhase = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxPhase.setMinimum(-360.0)
        self.doubleSpinBoxPhase.setMaximum(360.0)
        self.doubleSpinBoxPhase.setProperty("value", 0.0)
        self.doubleSpinBoxPhase.setObjectName("doubleSpinBoxPhase")
        self.gridLayout.addWidget(self.doubleSpinBoxPhase, 4, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 3, 1, 1)
        self.checkBoxNormToNRB = QtWidgets.QCheckBox(self.frame)
        self.checkBoxNormToNRB.setChecked(True)
        self.checkBoxNormToNRB.setObjectName("checkBoxNormToNRB")
        self.gridLayout.addWidget(self.checkBoxNormToNRB, 1, 1, 1, 1)
        self.spinBoxPadFactor = QtWidgets.QSpinBox(self.frame)
        self.spinBoxPadFactor.setObjectName("spinBoxPadFactor")
        self.gridLayout.addWidget(self.spinBoxPadFactor, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 3, 1, 1)
        self.spinBoxEdge = QtWidgets.QSpinBox(self.frame)
        self.spinBoxEdge.setMinimum(1)
        self.spinBoxEdge.setMaximum(800)
        self.spinBoxEdge.setProperty("value", 30)
        self.spinBoxEdge.setObjectName("spinBoxEdge")
        self.gridLayout.addWidget(self.spinBoxEdge, 7, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButtonInteractive = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonInteractive.sizePolicy().hasHeightForWidth())
        self.pushButtonInteractive.setSizePolicy(sizePolicy)
        self.pushButtonInteractive.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButtonInteractive.setMaximumSize(QtCore.QSize(220, 16777215))
        self.pushButtonInteractive.setObjectName("pushButtonInteractive")
        self.verticalLayout.addWidget(self.pushButtonInteractive)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.checkBoxNormToNRB, self.doubleSpinBoxNRBAmp)
        Dialog.setTabOrder(self.doubleSpinBoxNRBAmp, self.doubleSpinBoxCARSAmp)
        Dialog.setTabOrder(self.doubleSpinBoxCARSAmp, self.doubleSpinBoxPhase)
        Dialog.setTabOrder(self.doubleSpinBoxPhase, self.pushButtonInteractive)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kramers-Kronig Options"))
        self.label_4.setText(_translate("Dialog", "Kramers-Kronig Settings"))
        self.label_5.setText(_translate("Dialog", "Pad Factor"))
        self.label_3.setText(_translate("Dialog", "Phase Offset"))
        self.label.setText(_translate("Dialog", "NRB Bias"))
        self.label_2.setText(_translate("Dialog", "CARS Bias"))
        self.checkBoxNormToNRB.setText(_translate("Dialog", "Norm to NRB"))
        self.label_6.setText(_translate("Dialog", "N Edge Pixels (Avg)"))
        self.pushButtonInteractive.setText(_translate("Dialog", "Interactive Setting Selection"))
