# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tune_panel.ui'
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
        Form.resize(529, 668)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 20, 511, 641))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 191, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 40, 471, 148))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.line_edit_ratio = QLineEdit(self.gridLayoutWidget)
        self.line_edit_ratio.setObjectName(u"line_edit_ratio")
        self.line_edit_ratio.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_ratio, 1, 2, 1, 1)

        self.buttonReset = QPushButton(self.gridLayoutWidget)
        self.buttonReset.setObjectName(u"buttonReset")

        self.gridLayout.addWidget(self.buttonReset, 2, 2, 1, 2)

        self.dspin_ref_frequency = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_ref_frequency.setObjectName(u"dspin_ref_frequency")
        self.dspin_ref_frequency.setDecimals(4)
        self.dspin_ref_frequency.setMinimum(1.000000000000000)
        self.dspin_ref_frequency.setMaximum(20000.000000000000000)
        self.dspin_ref_frequency.setValue(440.000000000000000)

        self.gridLayout.addWidget(self.dspin_ref_frequency, 2, 1, 1, 1)

        self.line_edit_cents = QLineEdit(self.gridLayoutWidget)
        self.line_edit_cents.setObjectName(u"line_edit_cents")

        self.gridLayout.addWidget(self.line_edit_cents, 1, 3, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.spin_notes_per_octave = QSpinBox(self.gridLayoutWidget)
        self.spin_notes_per_octave.setObjectName(u"spin_notes_per_octave")
        self.spin_notes_per_octave.setMinimum(4)
        self.spin_notes_per_octave.setMaximum(100)
        self.spin_notes_per_octave.setValue(12)

        self.gridLayout.addWidget(self.spin_notes_per_octave, 0, 1, 1, 1)

        self.spin_reference_key = QSpinBox(self.gridLayoutWidget)
        self.spin_reference_key.setObjectName(u"spin_reference_key")
        self.spin_reference_key.setMaximum(127)
        self.spin_reference_key.setValue(57)

        self.gridLayout.addWidget(self.spin_reference_key, 1, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.dspin_speed_of_sound = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_speed_of_sound.setObjectName(u"dspin_speed_of_sound")
        self.dspin_speed_of_sound.setDecimals(3)
        self.dspin_speed_of_sound.setMinimum(1.000000000000000)
        self.dspin_speed_of_sound.setMaximum(1000.000000000000000)
        self.dspin_speed_of_sound.setValue(343.000000000000000)

        self.gridLayout.addWidget(self.dspin_speed_of_sound, 3, 1, 1, 1)

        self.list_frequencies = QListWidget(self.frame)
        self.list_frequencies.setObjectName(u"list_frequencies")
        self.list_frequencies.setGeometry(QRect(20, 240, 471, 381))
        font2 = QFont()
        font2.setFamily(u"Liberation Mono")
        self.list_frequencies.setFont(font2)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 210, 51, 20))
        font3 = QFont()
        font3.setPointSize(9)
        self.label_8.setFont(font3)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 210, 41, 20))
        font4 = QFont()
        font4.setPointSize(8)
        self.label_9.setFont(font4)
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(170, 210, 71, 20))
        self.label_10.setFont(font4)
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(280, 210, 41, 20))
        self.label_11.setFont(font4)
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(380, 210, 21, 20))
        font5 = QFont()
        font5.setPointSize(10)
        self.label_12.setFont(font5)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Equal Tempered Scales", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Ratio", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Notes Per Octave", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Reference Frequency", None))
        self.buttonReset.setText(QCoreApplication.translate("Form", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.dspin_ref_frequency.setToolTip(QCoreApplication.translate("Form", u"Frequency of reference key", None))
#endif // QT_CONFIG(tooltip)
        self.dspin_ref_frequency.setSuffix(QCoreApplication.translate("Form", u" hz", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Reference Key", None))
#if QT_CONFIG(tooltip)
        self.spin_reference_key.setToolTip(QCoreApplication.translate("Form", u"MIDI keynumber, 60 = Middle C", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Cents", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Speed of Sound", None))
#if QT_CONFIG(tooltip)
        self.dspin_speed_of_sound.setToolTip(QCoreApplication.translate("Form", u"343 m/s at 20 degrees C", None))
#endif // QT_CONFIG(tooltip)
        self.dspin_speed_of_sound.setSuffix(QCoreApplication.translate("Form", u" m/s", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("Form", u"MIDI key number", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"key", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"octave", None))
#if QT_CONFIG(tooltip)
        self.label_10.setToolTip(QCoreApplication.translate("Form", u"Note frequency in Hertz", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("Form", u"frequency", None))
#if QT_CONFIG(tooltip)
        self.label_11.setToolTip(QCoreApplication.translate("Form", u"Note period in seconds", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("Form", u"period", None))
#if QT_CONFIG(tooltip)
        self.label_12.setToolTip(QCoreApplication.translate("Form", u"Wave length in meters", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Form", u"\u03bb", None))
    # retranslateUi

