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
        Form.resize(302, 286)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 281, 261))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 81, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.formLayoutWidget = QWidget(self.frame)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(20, 50, 243, 186))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.dspin_starting = QDoubleSpinBox(self.formLayoutWidget)
        self.dspin_starting.setObjectName(u"dspin_starting")
        self.dspin_starting.setDecimals(4)
        self.dspin_starting.setMinimum(0.000100000000000)
        self.dspin_starting.setMaximum(1000000.000000000000000)
        self.dspin_starting.setValue(1.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dspin_starting)

        self.dspin_required = QDoubleSpinBox(self.formLayoutWidget)
        self.dspin_required.setObjectName(u"dspin_required")
        self.dspin_required.setDecimals(4)
        self.dspin_required.setMinimum(0.000100000000000)
        self.dspin_required.setMaximum(1000000.000000000000000)
        self.dspin_required.setValue(1.000000000000000)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dspin_required)

        self.line_edit_scale = QLineEdit(self.formLayoutWidget)
        self.line_edit_scale.setObjectName(u"line_edit_scale")
        self.line_edit_scale.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.line_edit_scale)

        self.line_edit_transpose = QLineEdit(self.formLayoutWidget)
        self.line_edit_transpose.setObjectName(u"line_edit_transpose")
        self.line_edit_transpose.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.line_edit_transpose)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_6)

        self.line_edit_diff = QLineEdit(self.formLayoutWidget)
        self.line_edit_diff.setObjectName(u"line_edit_diff")
        self.line_edit_diff.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_edit_diff)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Transpose", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Starting", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Required", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Scale", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Transpose", None))
#if QT_CONFIG(tooltip)
        self.dspin_starting.setToolTip(QCoreApplication.translate("Form", u"Initial frequency", None))
#endif // QT_CONFIG(tooltip)
        self.dspin_starting.setSuffix(QCoreApplication.translate("Form", u" hz", None))
#if QT_CONFIG(tooltip)
        self.dspin_required.setToolTip(QCoreApplication.translate("Form", u"Required frequency", None))
#endif // QT_CONFIG(tooltip)
        self.dspin_required.setSuffix(QCoreApplication.translate("Form", u" hz", None))
#if QT_CONFIG(tooltip)
        self.line_edit_scale.setToolTip(QCoreApplication.translate("Form", u"Ratio required / starting", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_scale.setPlaceholderText(QCoreApplication.translate("Form", u"1.000", None))
#if QT_CONFIG(tooltip)
        self.line_edit_transpose.setToolTip(QCoreApplication.translate("Form", u"Transpose amount in steps and cents", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_transpose.setPlaceholderText(QCoreApplication.translate("Form", u"0 steps 0 cents", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Diff", None))
#if QT_CONFIG(tooltip)
        self.line_edit_diff.setToolTip(QCoreApplication.translate("Form", u"Differance abs(required - start)", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_diff.setPlaceholderText(QCoreApplication.translate("Form", u"0.000", None))
    # retranslateUi

