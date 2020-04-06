# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'beat_panel.ui'
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
        Form.resize(553, 761)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 541, 751))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 521, 621))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.dspin_half = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_half.setObjectName(u"dspin_half")
        self.dspin_half.setReadOnly(True)
        self.dspin_half.setDecimals(4)
        self.dspin_half.setMaximum(999999999.000000000000000)

        self.gridLayout.addWidget(self.dspin_half, 8, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)

        self.dspin_tick = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_tick.setObjectName(u"dspin_tick")
        self.dspin_tick.setReadOnly(True)
        self.dspin_tick.setDecimals(6)
        self.dspin_tick.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_tick, 15, 1, 1, 1)

        self.dspin_quarter_tuplet = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_quarter_tuplet.setObjectName(u"dspin_quarter_tuplet")
        self.dspin_quarter_tuplet.setReadOnly(True)
        self.dspin_quarter_tuplet.setDecimals(4)
        self.dspin_quarter_tuplet.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_quarter_tuplet, 9, 2, 1, 1)

        self.line = QFrame(self.gridLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 3)

        self.dspin_half_tuplet = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_half_tuplet.setObjectName(u"dspin_half_tuplet")
        self.dspin_half_tuplet.setReadOnly(True)
        self.dspin_half_tuplet.setDecimals(4)
        self.dspin_half_tuplet.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_half_tuplet, 8, 2, 1, 1)

        self.dspin_thirtysecond_tuplet = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_thirtysecond_tuplet.setObjectName(u"dspin_thirtysecond_tuplet")
        self.dspin_thirtysecond_tuplet.setReadOnly(True)
        self.dspin_thirtysecond_tuplet.setDecimals(4)
        self.dspin_thirtysecond_tuplet.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_thirtysecond_tuplet, 12, 2, 1, 1)

        self.dspin_sixtyfour_tuplet = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_sixtyfour_tuplet.setObjectName(u"dspin_sixtyfour_tuplet")
        self.dspin_sixtyfour_tuplet.setReadOnly(True)
        self.dspin_sixtyfour_tuplet.setDecimals(4)
        self.dspin_sixtyfour_tuplet.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_sixtyfour_tuplet, 13, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 10, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 13, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)

        self.dspin_thrirtysecond = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_thrirtysecond.setObjectName(u"dspin_thrirtysecond")
        self.dspin_thrirtysecond.setReadOnly(True)
        self.dspin_thrirtysecond.setDecimals(4)
        self.dspin_thrirtysecond.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_thrirtysecond, 12, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 12, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)

        self.dspin_whole = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_whole.setObjectName(u"dspin_whole")
        self.dspin_whole.setReadOnly(True)
        self.dspin_whole.setDecimals(3)
        self.dspin_whole.setMaximum(999999999.000000000000000)

        self.gridLayout.addWidget(self.dspin_whole, 7, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.spin_beat_count = QSpinBox(self.gridLayoutWidget)
        self.spin_beat_count.setObjectName(u"spin_beat_count")
        self.spin_beat_count.setMinimum(1)
        self.spin_beat_count.setMaximum(256)
        self.spin_beat_count.setSingleStep(1)
        self.spin_beat_count.setValue(4)

        self.gridLayout.addWidget(self.spin_beat_count, 2, 1, 1, 1)

        self.dspin_tempo = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_tempo.setObjectName(u"dspin_tempo")
        self.dspin_tempo.setDecimals(3)
        self.dspin_tempo.setMinimum(20.000000000000000)
        self.dspin_tempo.setMaximum(300.000000000000000)
        self.dspin_tempo.setValue(120.000000000000000)

        self.gridLayout.addWidget(self.dspin_tempo, 0, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout.addWidget(self.label_17, 3, 0, 1, 1)

        self.dspin_sixtyfour = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_sixtyfour.setObjectName(u"dspin_sixtyfour")
        self.dspin_sixtyfour.setReadOnly(True)
        self.dspin_sixtyfour.setDecimals(4)
        self.dspin_sixtyfour.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_sixtyfour, 13, 1, 1, 1)

        self.spin_tick_count = QSpinBox(self.gridLayoutWidget)
        self.spin_tick_count.setObjectName(u"spin_tick_count")
        self.spin_tick_count.setMinimum(12)
        self.spin_tick_count.setMaximum(46080)
        self.spin_tick_count.setValue(120)

        self.gridLayout.addWidget(self.spin_tick_count, 3, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 15, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)

        self.frame_2 = QFrame(self.gridLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 151, 141))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.radio_units_seconds = QRadioButton(self.gridLayoutWidget_2)
        self.radio_units_seconds.setObjectName(u"radio_units_seconds")
        self.radio_units_seconds.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_units_seconds, 2, 0, 1, 1)

        self.radio_unit_ticks = QRadioButton(self.gridLayoutWidget_2)
        self.radio_unit_ticks.setObjectName(u"radio_unit_ticks")

        self.gridLayout_2.addWidget(self.radio_unit_ticks, 1, 0, 1, 1)

        self.buttonReset = QPushButton(self.gridLayoutWidget_2)
        self.buttonReset.setObjectName(u"buttonReset")

        self.gridLayout_2.addWidget(self.buttonReset, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 2, 4, 1)

        self.dspin_whole_tuplet = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_whole_tuplet.setObjectName(u"dspin_whole_tuplet")
        self.dspin_whole_tuplet.setReadOnly(True)
        self.dspin_whole_tuplet.setDecimals(3)
        self.dspin_whole_tuplet.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_whole_tuplet, 7, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(130, 16777215))

        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)

        self.dspin_eighth_tuplet = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_eighth_tuplet.setObjectName(u"dspin_eighth_tuplet")
        self.dspin_eighth_tuplet.setReadOnly(True)
        self.dspin_eighth_tuplet.setDecimals(4)
        self.dspin_eighth_tuplet.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_eighth_tuplet, 10, 2, 1, 1)

        self.dspin_sixteen_tuplet = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_sixteen_tuplet.setObjectName(u"dspin_sixteen_tuplet")
        self.dspin_sixteen_tuplet.setReadOnly(True)
        self.dspin_sixteen_tuplet.setDecimals(4)
        self.dspin_sixteen_tuplet.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_sixteen_tuplet, 11, 2, 1, 1)

        self.dspin_bar = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_bar.setObjectName(u"dspin_bar")
        self.dspin_bar.setReadOnly(True)
        self.dspin_bar.setDecimals(3)
        self.dspin_bar.setMaximum(999999999.000000000000000)

        self.gridLayout.addWidget(self.dspin_bar, 6, 1, 1, 1)

        self.dspin_eighth = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_eighth.setObjectName(u"dspin_eighth")
        self.dspin_eighth.setReadOnly(True)
        self.dspin_eighth.setDecimals(4)
        self.dspin_eighth.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_eighth, 10, 1, 1, 1)

        self.dspin_sixteen = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_sixteen.setObjectName(u"dspin_sixteen")
        self.dspin_sixteen.setReadOnly(True)
        self.dspin_sixteen.setDecimals(4)
        self.dspin_sixteen.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_sixteen, 11, 1, 1, 1)

        self.dspin_quarter = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_quarter.setObjectName(u"dspin_quarter")
        self.dspin_quarter.setReadOnly(True)
        self.dspin_quarter.setDecimals(4)
        self.dspin_quarter.setMaximum(9999.000000000000000)

        self.gridLayout.addWidget(self.dspin_quarter, 9, 1, 1, 1)

        self.spin_bar_count = QSpinBox(self.gridLayoutWidget)
        self.spin_bar_count.setObjectName(u"spin_bar_count")
        self.spin_bar_count.setMinimum(1)
        self.spin_bar_count.setMaximum(512)

        self.gridLayout.addWidget(self.spin_bar_count, 1, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 5, 2, 2, 1)

        self.dspin_phrase = QDoubleSpinBox(self.gridLayoutWidget)
        self.dspin_phrase.setObjectName(u"dspin_phrase")
        self.dspin_phrase.setMinimumSize(QSize(0, 40))
        self.dspin_phrase.setReadOnly(True)
        self.dspin_phrase.setDecimals(3)
        self.dspin_phrase.setMaximum(999999999.000000000000000)

        self.gridLayout.addWidget(self.dspin_phrase, 5, 1, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.frame)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 640, 524, 103))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.gridLayoutWidget_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 1, 1, 1, 1)

        self.radio_tuplet_dotdot = QRadioButton(self.gridLayoutWidget_3)
        self.radio_tuplet_dotdot.setObjectName(u"radio_tuplet_dotdot")

        self.gridLayout_3.addWidget(self.radio_tuplet_dotdot, 0, 3, 1, 1)

        self.spin_tuplet_numerator = QSpinBox(self.gridLayoutWidget_3)
        self.spin_tuplet_numerator.setObjectName(u"spin_tuplet_numerator")
        self.spin_tuplet_numerator.setEnabled(False)
        self.spin_tuplet_numerator.setMinimum(1)
        self.spin_tuplet_numerator.setMaximum(128)
        self.spin_tuplet_numerator.setValue(3)

        self.gridLayout_3.addWidget(self.spin_tuplet_numerator, 1, 2, 1, 2)

        self.radio_tuplet_other = QRadioButton(self.gridLayoutWidget_3)
        self.radio_tuplet_other.setObjectName(u"radio_tuplet_other")

        self.gridLayout_3.addWidget(self.radio_tuplet_other, 0, 5, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)

        self.radio_tuplet_dot = QRadioButton(self.gridLayoutWidget_3)
        self.radio_tuplet_dot.setObjectName(u"radio_tuplet_dot")
        self.radio_tuplet_dot.setChecked(True)

        self.gridLayout_3.addWidget(self.radio_tuplet_dot, 0, 2, 1, 1)

        self.radio_tuplet_tripplet = QRadioButton(self.gridLayoutWidget_3)
        self.radio_tuplet_tripplet.setObjectName(u"radio_tuplet_tripplet")

        self.gridLayout_3.addWidget(self.radio_tuplet_tripplet, 0, 4, 1, 1)

        self.spin_tuplet_denominator = QSpinBox(self.gridLayoutWidget_3)
        self.spin_tuplet_denominator.setObjectName(u"spin_tuplet_denominator")
        self.spin_tuplet_denominator.setEnabled(False)
        self.spin_tuplet_denominator.setMinimum(1)
        self.spin_tuplet_denominator.setMaximum(128)
        self.spin_tuplet_denominator.setValue(2)

        self.gridLayout_3.addWidget(self.spin_tuplet_denominator, 1, 4, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.dspin_half.setToolTip(QCoreApplication.translate("Form", u"Duration of Half note", None))
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("Form", u"Quarter", None))
#if QT_CONFIG(tooltip)
        self.dspin_tick.setToolTip(QCoreApplication.translate("Form", u"Duration of single tick", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_quarter_tuplet.setToolTip(QCoreApplication.translate("Form", u"Quarter note tuplet duration", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_half_tuplet.setToolTip(QCoreApplication.translate("Form", u"Half note tuplet duration", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_thirtysecond_tuplet.setToolTip(QCoreApplication.translate("Form", u"Thirysecond note tuplet duration", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_sixtyfour_tuplet.setToolTip(QCoreApplication.translate("Form", u"Sixtyfourth note tuplet duration", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"Eighth", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Sixtyfourth", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Bars Per Phrase", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Half", None))
#if QT_CONFIG(tooltip)
        self.dspin_thrirtysecond.setToolTip(QCoreApplication.translate("Form", u"Duration of Thirtysecond note", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("Form", u"Thirtysecond", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Sixteenth", None))
#if QT_CONFIG(tooltip)
        self.dspin_whole.setToolTip(QCoreApplication.translate("Form", u"Duration of Whole note", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Beats Per Bar", None))
#if QT_CONFIG(tooltip)
        self.spin_beat_count.setToolTip(QCoreApplication.translate("Form", u"Number of beats (quarter notes) per bar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_tempo.setToolTip(QCoreApplication.translate("Form", u"Tempo in Beats Per Minute", None))
#endif // QT_CONFIG(tooltip)
        self.dspin_tempo.setSuffix(QCoreApplication.translate("Form", u" BPM", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Phrase", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Ticks Per Beat", None))
#if QT_CONFIG(tooltip)
        self.dspin_sixtyfour.setToolTip(QCoreApplication.translate("Form", u"Duration of Sixtyfourth note", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spin_tick_count.setToolTip(QCoreApplication.translate("Form", u"Number of ticks per beat", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Tick", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Whole", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Bar", None))
        self.label.setText(QCoreApplication.translate("Form", u"Duration Units", None))
#if QT_CONFIG(tooltip)
        self.radio_units_seconds.setToolTip(QCoreApplication.translate("Form", u"Use seconds as duration unit", None))
#endif // QT_CONFIG(tooltip)
        self.radio_units_seconds.setText(QCoreApplication.translate("Form", u"Seconds", None))
#if QT_CONFIG(tooltip)
        self.radio_unit_ticks.setToolTip(QCoreApplication.translate("Form", u"Use ticks as duration unit", None))
#endif // QT_CONFIG(tooltip)
        self.radio_unit_ticks.setText(QCoreApplication.translate("Form", u"Ticks", None))
        self.buttonReset.setText(QCoreApplication.translate("Form", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.dspin_whole_tuplet.setToolTip(QCoreApplication.translate("Form", u"Whole note tuplet duration", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("Form", u"Tempo", None))
#if QT_CONFIG(tooltip)
        self.dspin_eighth_tuplet.setToolTip(QCoreApplication.translate("Form", u"Eighth note tuplet duration", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_sixteen_tuplet.setToolTip(QCoreApplication.translate("Form", u"Sixteenth note tuplet duration", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_bar.setToolTip(QCoreApplication.translate("Form", u"Duration of one bar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_eighth.setToolTip(QCoreApplication.translate("Form", u"Duration of Eighth note", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_sixteen.setToolTip(QCoreApplication.translate("Form", u"Duration of Sixteenth note", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.dspin_quarter.setToolTip(QCoreApplication.translate("Form", u"Duration of Quarter note", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spin_bar_count.setToolTip(QCoreApplication.translate("Form", u"Number of bars per phrase", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Tuplet\n"
"Durations", None))
#if QT_CONFIG(tooltip)
        self.dspin_phrase.setToolTip(QCoreApplication.translate("Form", u"Duration of phrase", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("Form", u"Ratio", None))
#if QT_CONFIG(tooltip)
        self.radio_tuplet_dotdot.setToolTip(QCoreApplication.translate("Form", u"Set tuplet ratio to double-dotted notes (9:4)", None))
#endif // QT_CONFIG(tooltip)
        self.radio_tuplet_dotdot.setText(QCoreApplication.translate("Form", u"Double Dotted", None))
#if QT_CONFIG(tooltip)
        self.spin_tuplet_numerator.setToolTip(QCoreApplication.translate("Form", u"Tuplet ratio numerator", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.radio_tuplet_other.setToolTip(QCoreApplication.translate("Form", u"Use manual tuplet ratio", None))
#endif // QT_CONFIG(tooltip)
        self.radio_tuplet_other.setText(QCoreApplication.translate("Form", u"Other", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Tuplet", None))
#if QT_CONFIG(tooltip)
        self.radio_tuplet_dot.setToolTip(QCoreApplication.translate("Form", u"Set tuple ratio to dotted notes (3:2)", None))
#endif // QT_CONFIG(tooltip)
        self.radio_tuplet_dot.setText(QCoreApplication.translate("Form", u"Dotted", None))
#if QT_CONFIG(tooltip)
        self.radio_tuplet_tripplet.setToolTip(QCoreApplication.translate("Form", u"Set tuplet ratio to tripplets (2:3)", None))
#endif // QT_CONFIG(tooltip)
        self.radio_tuplet_tripplet.setText(QCoreApplication.translate("Form", u"Tripplet", None))
#if QT_CONFIG(tooltip)
        self.spin_tuplet_denominator.setToolTip(QCoreApplication.translate("Form", u"Tublet ratio denominator", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

