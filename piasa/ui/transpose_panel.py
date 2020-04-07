# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transpose_panel.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(789, 612)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 621, 331))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 81, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 40, 601, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 0, 1, 1)

        self.line_edit_transpose = QLineEdit(self.gridLayoutWidget)
        self.line_edit_transpose.setObjectName(u"line_edit_transpose")
        self.line_edit_transpose.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_transpose, 5, 3, 1, 1)

        self.radio_frequency = QRadioButton(self.gridLayoutWidget)
        self.radio_frequency.setObjectName(u"radio_frequency")
        self.radio_frequency.setChecked(True)

        self.gridLayout.addWidget(self.radio_frequency, 0, 3, 1, 1)

        self.line_edit_freq_ratio = QLineEdit(self.gridLayoutWidget)
        self.line_edit_freq_ratio.setObjectName(u"line_edit_freq_ratio")
        self.line_edit_freq_ratio.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_freq_ratio, 4, 3, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.dspin_time0 = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_time0.setObjectName(u"dspin_time0")
        self.dspin_time0.setReadOnly(False)
        self.dspin_time0.setDecimals(5)
        self.dspin_time0.setMinimum(0.000050000000000)
        self.dspin_time0.setMaximum(20000.000000000000000)
        self.dspin_time0.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.dspin_time0, 1, 4, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.line_edit_freq_diff = QLineEdit(self.gridLayoutWidget)
        self.line_edit_freq_diff.setObjectName(u"line_edit_freq_diff")
        self.line_edit_freq_diff.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_freq_diff, 3, 3, 1, 1)

        self.dspin_time1 = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_time1.setObjectName(u"dspin_time1")
        self.dspin_time1.setReadOnly(False)
        self.dspin_time1.setDecimals(5)
        self.dspin_time1.setMinimum(0.000050000000000)
        self.dspin_time1.setMaximum(20000.000000000000000)
        self.dspin_time1.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.dspin_time1, 2, 4, 1, 1)

        self.dspin_freq1 = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_freq1.setObjectName(u"dspin_freq1")
        self.dspin_freq1.setDecimals(5)
        self.dspin_freq1.setMinimum(0.000050000000000)
        self.dspin_freq1.setMaximum(20000.000000000000000)
        self.dspin_freq1.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.dspin_freq1, 2, 3, 1, 1)

        self.dspin_freq0 = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_freq0.setObjectName(u"dspin_freq0")
        self.dspin_freq0.setDecimals(5)
        self.dspin_freq0.setMinimum(0.000050000000000)
        self.dspin_freq0.setMaximum(20000.000000000000000)
        self.dspin_freq0.setValue(1.000000000000000)

        self.gridLayout.addWidget(self.dspin_freq0, 1, 3, 1, 1)

        self.line_edit_time_diff = QLineEdit(self.gridLayoutWidget)
        self.line_edit_time_diff.setObjectName(u"line_edit_time_diff")
        self.line_edit_time_diff.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_time_diff, 3, 4, 1, 1)

        self.line_edit_time_ratio = QLineEdit(self.gridLayoutWidget)
        self.line_edit_time_ratio.setObjectName(u"line_edit_time_ratio")
        self.line_edit_time_ratio.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_time_ratio, 4, 4, 1, 1)

        self.radio_time = QRadioButton(self.gridLayoutWidget)
        self.radio_time.setObjectName(u"radio_time")

        self.gridLayout.addWidget(self.radio_time, 0, 4, 1, 1)

        self.button_reset = QPushButton(self.gridLayoutWidget)
        self.button_reset.setObjectName(u"button_reset")

        self.gridLayout.addWidget(self.button_reset, 5, 4, 1, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 360, 351, 221))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(9, 9, 331, 221))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.line_edit_lambda = QLineEdit(self.gridLayoutWidget_2)
        self.line_edit_lambda.setObjectName(u"line_edit_lambda")
        self.line_edit_lambda.setReadOnly(True)

        self.gridLayout_2.addWidget(self.line_edit_lambda, 2, 2, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.line_edit_freq0_copy = QLineEdit(self.gridLayoutWidget_2)
        self.line_edit_freq0_copy.setObjectName(u"line_edit_freq0_copy")
        self.line_edit_freq0_copy.setReadOnly(True)

        self.gridLayout_2.addWidget(self.line_edit_freq0_copy, 1, 2, 1, 1)

        self.dspin_speed = QDoubleSpinBox(self.gridLayoutWidget_2)
        self.dspin_speed.setObjectName(u"dspin_speed")
        self.dspin_speed.setMinimum(1.000000000000000)
        self.dspin_speed.setMaximum(3300.000000000000000)
        self.dspin_speed.setValue(343.000000000000000)

        self.gridLayout_2.addWidget(self.dspin_speed, 0, 2, 1, 1)

        self.radio_metric = QRadioButton(self.gridLayoutWidget_2)
        self.radio_metric.setObjectName(u"radio_metric")
        self.radio_metric.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_metric, 0, 3, 1, 1)

        self.radio_imperial = QRadioButton(self.gridLayoutWidget_2)
        self.radio_imperial.setObjectName(u"radio_imperial")

        self.gridLayout_2.addWidget(self.radio_imperial, 1, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Transpose", None))
        self.line_edit_transpose.setPlaceholderText(QCoreApplication.translate("Form", u"0 steps  0 cents", None))
        self.radio_frequency.setText(QCoreApplication.translate("Form", u"Frequency ", None))
        self.line_edit_freq_ratio.setPlaceholderText(QCoreApplication.translate("Form", u"1.00", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Initial", None))
        self.dspin_time0.setSuffix(QCoreApplication.translate("Form", u" sec", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ratio", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Transpose", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Final", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Difference", None))
        self.line_edit_freq_diff.setPlaceholderText(QCoreApplication.translate("Form", u"0.00 hz", None))
        self.dspin_time1.setSuffix(QCoreApplication.translate("Form", u" sec", None))
        self.dspin_freq1.setSuffix(QCoreApplication.translate("Form", u" hz", None))
        self.dspin_freq0.setSuffix(QCoreApplication.translate("Form", u" hz", None))
        self.line_edit_time_diff.setPlaceholderText(QCoreApplication.translate("Form", u"0.00 sec", None))
        self.line_edit_time_ratio.setPlaceholderText(QCoreApplication.translate("Form", u"1.00", None))
        self.radio_time.setText(QCoreApplication.translate("Form", u"Time ", None))
        self.button_reset.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.line_edit_lambda.setPlaceholderText(QCoreApplication.translate("Form", u"343 m", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Wave Length", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Frequency", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Speed of Sound", None))
        self.line_edit_freq0_copy.setPlaceholderText(QCoreApplication.translate("Form", u"1.00", None))
        self.dspin_speed.setSuffix(QCoreApplication.translate("Form", u" m/s", None))
        self.radio_metric.setText(QCoreApplication.translate("Form", u"Meters", None))
        self.radio_imperial.setText(QCoreApplication.translate("Form", u"Feet", None))
    # retranslateUi

