# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_ImageGainMath.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_formWidgetImages(object):
    def setupUi(self, formWidgetImages):
        formWidgetImages.setObjectName("formWidgetImages")
        formWidgetImages.resize(802, 371)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(formWidgetImages.sizePolicy().hasHeightForWidth())
        formWidgetImages.setSizePolicy(sizePolicy)
        formWidgetImages.setMinimumSize(QtCore.QSize(802, 371))
        formWidgetImages.setMaximumSize(QtCore.QSize(802, 371))
        self.gridLayout = QtWidgets.QGridLayout(formWidgetImages)
        self.gridLayout.setObjectName("gridLayout")
        self.widgetImgOpt = QtWidgets.QWidget(formWidgetImages)
        self.widgetImgOpt.setEnabled(True)
        self.widgetImgOpt.setObjectName("widgetImgOpt")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widgetImgOpt)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout.addWidget(self.widgetImgOpt, 0, 2, 1, 1)
        self.verticalLayoutMathTabs = QtWidgets.QVBoxLayout()
        self.verticalLayoutMathTabs.setObjectName("verticalLayoutMathTabs")
        self.tabWidgetMath = QtWidgets.QTabWidget(formWidgetImages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidgetMath.sizePolicy().hasHeightForWidth())
        self.tabWidgetMath.setSizePolicy(sizePolicy)
        self.tabWidgetMath.setObjectName("tabWidgetMath")
        self.tabBasic = QtWidgets.QWidget()
        self.tabBasic.setObjectName("tabBasic")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tabBasic)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frameBasicMath = QtWidgets.QFrame(self.tabBasic)
        self.frameBasicMath.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBasicMath.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameBasicMath.setObjectName("frameBasicMath")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frameBasicMath)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.labelBasicMath = QtWidgets.QLabel(self.frameBasicMath)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelBasicMath.sizePolicy().hasHeightForWidth())
        self.labelBasicMath.setSizePolicy(sizePolicy)
        self.labelBasicMath.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelBasicMath.setObjectName("labelBasicMath")
        self.verticalLayout_10.addWidget(self.labelBasicMath)
        self.horizontalLayoutBasicButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutBasicButtons.setObjectName("horizontalLayoutBasicButtons")
        self.pushButtonOpFreq1 = QtWidgets.QPushButton(self.frameBasicMath)
        self.pushButtonOpFreq1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonOpFreq1.setObjectName("pushButtonOpFreq1")
        self.horizontalLayoutBasicButtons.addWidget(self.pushButtonOpFreq1)
        self.comboBoxOperations = QtWidgets.QComboBox(self.frameBasicMath)
        self.comboBoxOperations.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxOperations.sizePolicy().hasHeightForWidth())
        self.comboBoxOperations.setSizePolicy(sizePolicy)
        self.comboBoxOperations.setObjectName("comboBoxOperations")
        self.horizontalLayoutBasicButtons.addWidget(self.comboBoxOperations)
        self.pushButtonOpFreq2 = QtWidgets.QPushButton(self.frameBasicMath)
        self.pushButtonOpFreq2.setEnabled(False)
        self.pushButtonOpFreq2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonOpFreq2.setObjectName("pushButtonOpFreq2")
        self.horizontalLayoutBasicButtons.addWidget(self.pushButtonOpFreq2)
        self.pushButtonOpFreq3 = QtWidgets.QPushButton(self.frameBasicMath)
        self.pushButtonOpFreq3.setEnabled(False)
        self.pushButtonOpFreq3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonOpFreq3.setObjectName("pushButtonOpFreq3")
        self.horizontalLayoutBasicButtons.addWidget(self.pushButtonOpFreq3)
        self.verticalLayout_10.addLayout(self.horizontalLayoutBasicButtons)
        self.labelConditionalMath = QtWidgets.QLabel(self.frameBasicMath)
        self.labelConditionalMath.setObjectName("labelConditionalMath")
        self.verticalLayout_10.addWidget(self.labelConditionalMath)
        self.horizontalLayoutConditionButtons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutConditionButtons.setObjectName("horizontalLayoutConditionButtons")
        self.pushButtonCondFreq1 = QtWidgets.QPushButton(self.frameBasicMath)
        self.pushButtonCondFreq1.setEnabled(False)
        self.pushButtonCondFreq1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonCondFreq1.setObjectName("pushButtonCondFreq1")
        self.horizontalLayoutConditionButtons.addWidget(self.pushButtonCondFreq1)
        self.comboBoxCondOps = QtWidgets.QComboBox(self.frameBasicMath)
        self.comboBoxCondOps.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCondOps.sizePolicy().hasHeightForWidth())
        self.comboBoxCondOps.setSizePolicy(sizePolicy)
        self.comboBoxCondOps.setObjectName("comboBoxCondOps")
        self.horizontalLayoutConditionButtons.addWidget(self.comboBoxCondOps)
        self.pushButtonCondFreq2 = QtWidgets.QPushButton(self.frameBasicMath)
        self.pushButtonCondFreq2.setEnabled(False)
        self.pushButtonCondFreq2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonCondFreq2.setObjectName("pushButtonCondFreq2")
        self.horizontalLayoutConditionButtons.addWidget(self.pushButtonCondFreq2)
        self.pushButtonCondFreq3 = QtWidgets.QPushButton(self.frameBasicMath)
        self.pushButtonCondFreq3.setEnabled(False)
        self.pushButtonCondFreq3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButtonCondFreq3.setObjectName("pushButtonCondFreq3")
        self.horizontalLayoutConditionButtons.addWidget(self.pushButtonCondFreq3)
        self.comboBoxCondInEquality = QtWidgets.QComboBox(self.frameBasicMath)
        self.comboBoxCondInEquality.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCondInEquality.sizePolicy().hasHeightForWidth())
        self.comboBoxCondInEquality.setSizePolicy(sizePolicy)
        self.comboBoxCondInEquality.setObjectName("comboBoxCondInEquality")
        self.horizontalLayoutConditionButtons.addWidget(self.comboBoxCondInEquality)
        self.spinBoxInEquality = QtWidgets.QDoubleSpinBox(self.frameBasicMath)
        self.spinBoxInEquality.setEnabled(False)
        self.spinBoxInEquality.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBoxInEquality.setMaximumSize(QtCore.QSize(16777215, 25))
        self.spinBoxInEquality.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBoxInEquality.setDecimals(5)
        self.spinBoxInEquality.setMinimum(-1000000000000.0)
        self.spinBoxInEquality.setMaximum(1000000000000.0)
        self.spinBoxInEquality.setObjectName("spinBoxInEquality")
        self.horizontalLayoutConditionButtons.addWidget(self.spinBoxInEquality)
        self.verticalLayout_10.addLayout(self.horizontalLayoutConditionButtons)
        self.pushButtonBasicMath = QtWidgets.QPushButton(self.frameBasicMath)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBasicMath.sizePolicy().hasHeightForWidth())
        self.pushButtonBasicMath.setSizePolicy(sizePolicy)
        self.pushButtonBasicMath.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonBasicMath.setFont(font)
        self.pushButtonBasicMath.setObjectName("pushButtonBasicMath")
        self.verticalLayout_10.addWidget(self.pushButtonBasicMath)
        self.verticalLayout_11.addWidget(self.frameBasicMath)
        self.tabWidgetMath.addTab(self.tabBasic, "")
        self.tabScripting = QtWidgets.QWidget()
        self.tabScripting.setObjectName("tabScripting")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabScripting)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frameScripting = QtWidgets.QFrame(self.tabScripting)
        self.frameScripting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameScripting.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameScripting.setObjectName("frameScripting")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameScripting)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutScripting = QtWidgets.QVBoxLayout()
        self.verticalLayoutScripting.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayoutScripting.setSpacing(2)
        self.verticalLayoutScripting.setObjectName("verticalLayoutScripting")
        self.labelScripting = QtWidgets.QLabel(self.frameScripting)
        self.labelScripting.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelScripting.setObjectName("labelScripting")
        self.verticalLayoutScripting.addWidget(self.labelScripting)
        self.lineEditScripting = QtWidgets.QLineEdit(self.frameScripting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditScripting.sizePolicy().hasHeightForWidth())
        self.lineEditScripting.setSizePolicy(sizePolicy)
        self.lineEditScripting.setMinimumSize(QtCore.QSize(0, 70))
        self.lineEditScripting.setObjectName("lineEditScripting")
        self.verticalLayoutScripting.addWidget(self.lineEditScripting)
        self.verticalLayout_3.addLayout(self.verticalLayoutScripting)
        self.pushButtonScripting = QtWidgets.QPushButton(self.frameScripting)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonScripting.sizePolicy().hasHeightForWidth())
        self.pushButtonScripting.setSizePolicy(sizePolicy)
        self.pushButtonScripting.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonScripting.setFont(font)
        self.pushButtonScripting.setObjectName("pushButtonScripting")
        self.verticalLayout_3.addWidget(self.pushButtonScripting)
        self.verticalLayout_8.addWidget(self.frameScripting)
        self.tabWidgetMath.addTab(self.tabScripting, "")
        self.verticalLayoutMathTabs.addWidget(self.tabWidgetMath)
        self.gridLayout.addLayout(self.verticalLayoutMathTabs, 1, 1, 2, 2)
        self.checkBox = QtWidgets.QCheckBox(formWidgetImages)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.verticalLayoutGain = QtWidgets.QVBoxLayout()
        self.verticalLayoutGain.setSpacing(2)
        self.verticalLayoutGain.setObjectName("verticalLayoutGain")
        self.labelGain = QtWidgets.QLabel(formWidgetImages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelGain.sizePolicy().hasHeightForWidth())
        self.labelGain.setSizePolicy(sizePolicy)
        self.labelGain.setMaximumSize(QtCore.QSize(16777215, 20))
        self.labelGain.setObjectName("labelGain")
        self.verticalLayoutGain.addWidget(self.labelGain)
        self.spinBoxGain = QtWidgets.QDoubleSpinBox(formWidgetImages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxGain.sizePolicy().hasHeightForWidth())
        self.spinBoxGain.setSizePolicy(sizePolicy)
        self.spinBoxGain.setMaximumSize(QtCore.QSize(16777215, 25))
        self.spinBoxGain.setMaximum(1000.0)
        self.spinBoxGain.setSingleStep(0.5)
        self.spinBoxGain.setProperty("value", 1.0)
        self.spinBoxGain.setObjectName("spinBoxGain")
        self.verticalLayoutGain.addWidget(self.spinBoxGain)
        self.pushButtonGain1 = QtWidgets.QPushButton(formWidgetImages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonGain1.sizePolicy().hasHeightForWidth())
        self.pushButtonGain1.setSizePolicy(sizePolicy)
        self.pushButtonGain1.setObjectName("pushButtonGain1")
        self.verticalLayoutGain.addWidget(self.pushButtonGain1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutGain.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayoutGain, 1, 0, 1, 1)

        self.retranslateUi(formWidgetImages)
        self.tabWidgetMath.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(formWidgetImages)

    def retranslateUi(self, formWidgetImages):
        _translate = QtCore.QCoreApplication.translate
        formWidgetImages.setWindowTitle(_translate("formWidgetImages", "Form"))
        self.labelBasicMath.setText(_translate("formWidgetImages", "Basic Math"))
        self.pushButtonOpFreq1.setText(_translate("formWidgetImages", "Freq 1"))
        self.pushButtonOpFreq2.setText(_translate("formWidgetImages", "Freq 2"))
        self.pushButtonOpFreq3.setText(_translate("formWidgetImages", "Freq 3"))
        self.labelConditionalMath.setText(_translate("formWidgetImages", "Conditional"))
        self.pushButtonCondFreq1.setText(_translate("formWidgetImages", "Freq 1"))
        self.pushButtonCondFreq2.setText(_translate("formWidgetImages", "Freq 2"))
        self.pushButtonCondFreq3.setText(_translate("formWidgetImages", "Freq 3"))
        self.pushButtonBasicMath.setText(_translate("formWidgetImages", "Perform Math"))
        self.tabWidgetMath.setTabText(self.tabWidgetMath.indexOf(self.tabBasic), _translate("formWidgetImages", "Basic Math"))
        self.labelScripting.setText(_translate("formWidgetImages", "Script Command"))
        self.pushButtonScripting.setText(_translate("formWidgetImages", "Perform Math"))
        self.tabWidgetMath.setTabText(self.tabWidgetMath.indexOf(self.tabScripting), _translate("formWidgetImages", "Math Scripting"))
        self.checkBox.setText(_translate("formWidgetImages", "Disable"))
        self.labelGain.setText(_translate("formWidgetImages", "Gain"))
        self.pushButtonGain1.setText(_translate("formWidgetImages", "1.0"))

