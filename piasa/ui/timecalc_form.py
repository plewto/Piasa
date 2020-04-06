# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'time_calculator_form.ui'
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
        Form.resize(663, 624)
        self.frame_input = QFrame(Form)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setGeometry(QRect(20, 40, 251, 501))
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame_input)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 231, 366))
        self.grid_input = QGridLayout(self.gridLayoutWidget)
        self.grid_input.setObjectName(u"grid_input")
        self.grid_input.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)

        self.grid_input.addWidget(self.label_2, 0, 0, 1, 1)

        self.radio_in_frames = QRadioButton(self.gridLayoutWidget)
        self.radio_in_frames.setObjectName(u"radio_in_frames")

        self.grid_input.addWidget(self.radio_in_frames, 3, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.grid_input.addWidget(self.line, 4, 0, 1, 1)

        self.radio_in_milli = QRadioButton(self.gridLayoutWidget)
        self.radio_in_milli.setObjectName(u"radio_in_milli")

        self.grid_input.addWidget(self.radio_in_milli, 6, 0, 1, 1)

        self.radio_in_micro = QRadioButton(self.gridLayoutWidget)
        self.radio_in_micro.setObjectName(u"radio_in_micro")

        self.grid_input.addWidget(self.radio_in_micro, 5, 0, 1, 1)

        self.radio_in_samples = QRadioButton(self.gridLayoutWidget)
        self.radio_in_samples.setObjectName(u"radio_in_samples")

        self.grid_input.addWidget(self.radio_in_samples, 2, 0, 1, 1)

        self.radio_in_second = QRadioButton(self.gridLayoutWidget)
        self.radio_in_second.setObjectName(u"radio_in_second")
        self.radio_in_second.setChecked(True)

        self.grid_input.addWidget(self.radio_in_second, 7, 0, 1, 1)

        self.button_reset = QPushButton(self.gridLayoutWidget)
        self.button_reset.setObjectName(u"button_reset")

        self.grid_input.addWidget(self.button_reset, 11, 0, 1, 1)

        self.dspin_input = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_input.setObjectName(u"dspin_input")
        self.dspin_input.setDecimals(4)
        self.dspin_input.setMaximum(1000000000.000000000000000)

        self.grid_input.addWidget(self.dspin_input, 1, 0, 1, 1)

        self.radio_in_minute = QRadioButton(self.gridLayoutWidget)
        self.radio_in_minute.setObjectName(u"radio_in_minute")

        self.grid_input.addWidget(self.radio_in_minute, 8, 0, 1, 1)

        self.radio_in_hour = QRadioButton(self.gridLayoutWidget)
        self.radio_in_hour.setObjectName(u"radio_in_hour")

        self.grid_input.addWidget(self.radio_in_hour, 9, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.grid_input.addWidget(self.label_8, 12, 0, 1, 1)

        self.frame_output = QFrame(Form)
        self.frame_output.setObjectName(u"frame_output")
        self.frame_output.setGeometry(QRect(280, 40, 251, 501))
        self.frame_output.setFrameShape(QFrame.StyledPanel)
        self.frame_output.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_output)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 231, 480))
        self.grid_output = QGridLayout(self.gridLayoutWidget_2)
        self.grid_output.setObjectName(u"grid_output")
        self.grid_output.setContentsMargins(0, 0, 0, 0)
        self.radio_out_hour = QRadioButton(self.gridLayoutWidget_2)
        self.radio_out_hour.setObjectName(u"radio_out_hour")

        self.grid_output.addWidget(self.radio_out_hour, 9, 0, 1, 1)

        self.line_edit_output = QLineEdit(self.gridLayoutWidget_2)
        self.line_edit_output.setObjectName(u"line_edit_output")
        self.line_edit_output.setReadOnly(True)

        self.grid_output.addWidget(self.line_edit_output, 1, 0, 1, 2)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.grid_output.addWidget(self.label_3, 0, 0, 1, 1)

        self.dspin_samplerate = QDoubleSpinBox(self.gridLayoutWidget_2)
        self.dspin_samplerate.setObjectName(u"dspin_samplerate")
        self.dspin_samplerate.setMinimum(1.000000000000000)
        self.dspin_samplerate.setMaximum(100.000000000000000)
        self.dspin_samplerate.setValue(44.100000000000001)

        self.grid_output.addWidget(self.dspin_samplerate, 12, 1, 1, 1)

        self.radio_out_milli = QRadioButton(self.gridLayoutWidget_2)
        self.radio_out_milli.setObjectName(u"radio_out_milli")

        self.grid_output.addWidget(self.radio_out_milli, 6, 0, 1, 1)

        self.radio_out_second = QRadioButton(self.gridLayoutWidget_2)
        self.radio_out_second.setObjectName(u"radio_out_second")
        self.radio_out_second.setChecked(True)

        self.grid_output.addWidget(self.radio_out_second, 7, 0, 1, 1)

        self.radio_out_samples = QRadioButton(self.gridLayoutWidget_2)
        self.radio_out_samples.setObjectName(u"radio_out_samples")

        self.grid_output.addWidget(self.radio_out_samples, 2, 0, 1, 1)

        self.radio_out_frames = QRadioButton(self.gridLayoutWidget_2)
        self.radio_out_frames.setObjectName(u"radio_out_frames")

        self.grid_output.addWidget(self.radio_out_frames, 3, 0, 1, 1)

        self.radio_out_minute = QRadioButton(self.gridLayoutWidget_2)
        self.radio_out_minute.setObjectName(u"radio_out_minute")

        self.grid_output.addWidget(self.radio_out_minute, 8, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.grid_output.addWidget(self.label_4, 12, 0, 1, 1)

        self.spin_framerate = QSpinBox(self.gridLayoutWidget_2)
        self.spin_framerate.setObjectName(u"spin_framerate")
        self.spin_framerate.setMinimum(1)
        self.spin_framerate.setMaximum(1024)
        self.spin_framerate.setValue(24)

        self.grid_output.addWidget(self.spin_framerate, 13, 1, 1, 1)

        self.button_swap = QPushButton(self.gridLayoutWidget_2)
        self.button_swap.setObjectName(u"button_swap")

        self.grid_output.addWidget(self.button_swap, 11, 0, 1, 2)

        self.radio_out_micro = QRadioButton(self.gridLayoutWidget_2)
        self.radio_out_micro.setObjectName(u"radio_out_micro")

        self.grid_output.addWidget(self.radio_out_micro, 5, 0, 1, 1)

        self.line_3 = QFrame(self.gridLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.grid_output.addWidget(self.line_3, 4, 1, 1, 1)

        self.line_2 = QFrame(self.gridLayoutWidget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.grid_output.addWidget(self.line_2, 4, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.grid_output.addWidget(self.label_5, 13, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.grid_output.addWidget(self.label_7, 14, 0, 1, 1)

        self.line_edit_scale = QLineEdit(self.gridLayoutWidget_2)
        self.line_edit_scale.setObjectName(u"line_edit_scale")
        self.line_edit_scale.setReadOnly(True)

        self.grid_output.addWidget(self.line_edit_scale, 14, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.grid_output.addWidget(self.label_6, 15, 0, 1, 1)

        self.line_edit_compound = QLineEdit(self.gridLayoutWidget_2)
        self.line_edit_compound.setObjectName(u"line_edit_compound")

        self.grid_output.addWidget(self.line_edit_compound, 15, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 181, 20))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"From", None))
        self.radio_in_frames.setText(QCoreApplication.translate("Form", u"Frames", None))
        self.radio_in_milli.setText(QCoreApplication.translate("Form", u"mSecond", None))
        self.radio_in_micro.setText(QCoreApplication.translate("Form", u"\u03bcSecond", None))
        self.radio_in_samples.setText(QCoreApplication.translate("Form", u"Samples", None))
        self.radio_in_second.setText(QCoreApplication.translate("Form", u"Second", None))
        self.button_reset.setText(QCoreApplication.translate("Form", u"Reset", None))
        self.radio_in_minute.setText(QCoreApplication.translate("Form", u"Minute", None))
        self.radio_in_hour.setText(QCoreApplication.translate("Form", u"Hour", None))
        self.label_8.setText("")
        self.radio_out_hour.setText(QCoreApplication.translate("Form", u"Hour", None))
        self.line_edit_output.setText("")
        self.line_edit_output.setPlaceholderText(QCoreApplication.translate("Form", u"1.0", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TO", None))
        self.dspin_samplerate.setSuffix(QCoreApplication.translate("Form", u" K", None))
        self.radio_out_milli.setText(QCoreApplication.translate("Form", u"mSecond ", None))
        self.radio_out_second.setText(QCoreApplication.translate("Form", u"Second", None))
        self.radio_out_samples.setText(QCoreApplication.translate("Form", u"Samples", None))
        self.radio_out_frames.setText(QCoreApplication.translate("Form", u"Frames", None))
        self.radio_out_minute.setText(QCoreApplication.translate("Form", u"Minute", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Sample Rate", None))
        self.button_swap.setText(QCoreApplication.translate("Form", u"Swap", None))
        self.radio_out_micro.setText(QCoreApplication.translate("Form", u"\u03bcSecond", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Frame Rate", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Scale", None))
        self.line_edit_scale.setPlaceholderText(QCoreApplication.translate("Form", u"x.xxx", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Compound", None))
#if QT_CONFIG(tooltip)
        self.line_edit_compound.setToolTip(QCoreApplication.translate("Form", u"Time in hours : minutes : seconds ", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_compound.setPlaceholderText(QCoreApplication.translate("Form", u"hh:mm:ss.sss", None))
        self.label.setText(QCoreApplication.translate("Form", u"Time Conversion", None))
    # retranslateUi

