# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scale_panel.ui'
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
        Form.resize(567, 350)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 551, 331))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 141, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 40, 531, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 3)

        self.combo_key = QComboBox(self.gridLayoutWidget)
        self.combo_key.setObjectName(u"combo_key")

        self.gridLayout.addWidget(self.combo_key, 5, 2, 1, 1)

        self.combo_scale = QComboBox(self.gridLayoutWidget)
        self.combo_scale.setObjectName(u"combo_scale")

        self.gridLayout.addWidget(self.combo_scale, 0, 2, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.line_edit_comments = QLineEdit(self.gridLayoutWidget)
        self.line_edit_comments.setObjectName(u"line_edit_comments")
        font1 = QFont()
        font1.setPointSize(10)
        self.line_edit_comments.setFont(font1)
        self.line_edit_comments.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_comments, 1, 2, 1, 1)

        self.line_edit_template = QLineEdit(self.gridLayoutWidget)
        self.line_edit_template.setObjectName(u"line_edit_template")
        font2 = QFont()
        font2.setFamily(u"Liberation Mono")
        font2.setPointSize(10)
        self.line_edit_template.setFont(font2)
        self.line_edit_template.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_template, 2, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.radio_flat = QRadioButton(self.gridLayoutWidget)
        self.radio_flat.setObjectName(u"radio_flat")
        self.radio_flat.setChecked(True)

        self.gridLayout.addWidget(self.radio_flat, 8, 0, 1, 1)

        self.line_edit_transposed_scale = QLineEdit(self.gridLayoutWidget)
        self.line_edit_transposed_scale.setObjectName(u"line_edit_transposed_scale")
        self.line_edit_transposed_scale.setFont(font2)
        self.line_edit_transposed_scale.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_transposed_scale, 8, 2, 2, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.line_edit_step_pattern = QLineEdit(self.gridLayoutWidget)
        self.line_edit_step_pattern.setObjectName(u"line_edit_step_pattern")
        self.line_edit_step_pattern.setFont(font2)
        self.line_edit_step_pattern.setReadOnly(False)

        self.gridLayout.addWidget(self.line_edit_step_pattern, 3, 2, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.radio_sharp = QRadioButton(self.gridLayoutWidget)
        self.radio_sharp.setObjectName(u"radio_sharp")

        self.gridLayout.addWidget(self.radio_sharp, 9, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Scales", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Scale", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Template", None))
#if QT_CONFIG(tooltip)
        self.line_edit_template.setToolTip(QCoreApplication.translate("Form", u"Scale in key of C", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("Form", u"Comments", None))
        self.radio_flat.setText(QCoreApplication.translate("Form", u"Flats", None))
#if QT_CONFIG(tooltip)
        self.line_edit_transposed_scale.setToolTip(QCoreApplication.translate("Form", u"Transposed Scale", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Step Pattern", None))
#if QT_CONFIG(tooltip)
        self.line_edit_step_pattern.setToolTip(QCoreApplication.translate("Form", u"Interval step size pattern", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Form", u"Key", None))
        self.radio_sharp.setText(QCoreApplication.translate("Form", u"Sharps", None))
    # retranslateUi

