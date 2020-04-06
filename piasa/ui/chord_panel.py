# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chord_panel.ui'
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
        Form.resize(623, 638)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 611, 321))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 69, 20))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 40, 591, 275))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.combo_chord_list = QComboBox(self.gridLayoutWidget)
        self.combo_chord_list.setObjectName(u"combo_chord_list")

        self.gridLayout.addWidget(self.combo_chord_list, 1, 1, 1, 2)

        self.line_edit_pattern = QLineEdit(self.gridLayoutWidget)
        self.line_edit_pattern.setObjectName(u"line_edit_pattern")
        font1 = QFont()
        font1.setFamily(u"Cantarell")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.line_edit_pattern.setFont(font1)
        self.line_edit_pattern.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_pattern, 6, 1, 1, 2)

        self.radio_flats = QRadioButton(self.gridLayoutWidget)
        self.radio_flats.setObjectName(u"radio_flats")
        self.radio_flats.setChecked(True)

        self.gridLayout.addWidget(self.radio_flats, 2, 2, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.spin_inversion = QSpinBox(self.gridLayoutWidget)
        self.spin_inversion.setObjectName(u"spin_inversion")
        self.spin_inversion.setMaximum(12)

        self.gridLayout.addWidget(self.spin_inversion, 4, 1, 1, 1)

        self.combo_key = QComboBox(self.gridLayoutWidget)
        self.combo_key.setObjectName(u"combo_key")

        self.gridLayout.addWidget(self.combo_key, 2, 1, 1, 1)

        self.line_edit_chord = QLineEdit(self.gridLayoutWidget)
        self.line_edit_chord.setObjectName(u"line_edit_chord")
        self.line_edit_chord.setFont(font1)
        self.line_edit_chord.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_chord, 7, 1, 1, 2)

        self.line_edit_template = QLineEdit(self.gridLayoutWidget)
        self.line_edit_template.setObjectName(u"line_edit_template")
        self.line_edit_template.setFont(font1)
        self.line_edit_template.setReadOnly(True)

        self.gridLayout.addWidget(self.line_edit_template, 5, 1, 1, 2)

        self.check_octave = QCheckBox(self.gridLayoutWidget)
        self.check_octave.setObjectName(u"check_octave")

        self.gridLayout.addWidget(self.check_octave, 4, 2, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.radio_sharps = QRadioButton(self.gridLayoutWidget)
        self.radio_sharps.setObjectName(u"radio_sharps")

        self.gridLayout.addWidget(self.radio_sharps, 2, 3, 1, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 330, 611, 301))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 581, 281))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 0, 3, 1, 1)

        self.line_edit_user_chord = QLineEdit(self.gridLayoutWidget_2)
        self.line_edit_user_chord.setObjectName(u"line_edit_user_chord")

        self.gridLayout_2.addWidget(self.line_edit_user_chord, 1, 1, 1, 2)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.list_chord_hits = QListWidget(self.gridLayoutWidget_2)
        self.list_chord_hits.setObjectName(u"list_chord_hits")
        font2 = QFont()
        font2.setFamily(u"DejaVu Sans Mono")
        font2.setBold(False)
        font2.setItalic(True)
        font2.setWeight(50)
        self.list_chord_hits.setFont(font2)

        self.gridLayout_2.addWidget(self.list_chord_hits, 1, 3, 5, 1)

        self.radio_sub = QRadioButton(self.gridLayoutWidget_2)
        self.radio_sub.setObjectName(u"radio_sub")
        self.radio_sub.setChecked(True)

        self.gridLayout_2.addWidget(self.radio_sub, 3, 0, 1, 1)

        self.radio_super = QRadioButton(self.gridLayoutWidget_2)
        self.radio_super.setObjectName(u"radio_super")

        self.gridLayout_2.addWidget(self.radio_super, 3, 1, 1, 1)

        self.radio_match = QRadioButton(self.gridLayoutWidget_2)
        self.radio_match.setObjectName(u"radio_match")

        self.gridLayout_2.addWidget(self.radio_match, 3, 2, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_12, 4, 1, 1, 1)

        self.dspin_threshold = QDoubleSpinBox(self.gridLayoutWidget_2)
        self.dspin_threshold.setObjectName(u"dspin_threshold")
        self.dspin_threshold.setEnabled(False)
        self.dspin_threshold.setMaximum(1.000000000000000)
        self.dspin_threshold.setSingleStep(0.100000000000000)
        self.dspin_threshold.setValue(0.500000000000000)

        self.gridLayout_2.addWidget(self.dspin_threshold, 4, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.button_find_chords = QPushButton(self.gridLayoutWidget_2)
        self.button_find_chords.setObjectName(u"button_find_chords")

        self.gridLayout_2.addWidget(self.button_find_chords, 2, 1, 1, 2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Chords", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Template", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Chord", None))
#if QT_CONFIG(tooltip)
        self.combo_chord_list.setToolTip(QCoreApplication.translate("Form", u"Selects chord form", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.line_edit_pattern.setToolTip(QCoreApplication.translate("Form", u"Interval pattern", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_pattern.setPlaceholderText(QCoreApplication.translate("Form", u"X X X", None))
#if QT_CONFIG(tooltip)
        self.radio_flats.setToolTip(QCoreApplication.translate("Form", u"Display accidentals as flats", None))
#endif // QT_CONFIG(tooltip)
        self.radio_flats.setText(QCoreApplication.translate("Form", u"Flats", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Intervals", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Inversion", None))
#if QT_CONFIG(tooltip)
        self.spin_inversion.setToolTip(QCoreApplication.translate("Form", u"Sets chord inversion", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.combo_key.setToolTip(QCoreApplication.translate("Form", u"Selects key", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.line_edit_chord.setToolTip(QCoreApplication.translate("Form", u"Transposed chord in selected key", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_chord.setPlaceholderText(QCoreApplication.translate("Form", u"X X X", None))
#if QT_CONFIG(tooltip)
        self.line_edit_template.setToolTip(QCoreApplication.translate("Form", u"Selected cord template (key of C)", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_template.setPlaceholderText(QCoreApplication.translate("Form", u"X X X", None))
#if QT_CONFIG(tooltip)
        self.check_octave.setToolTip(QCoreApplication.translate("Form", u"Add an octave copy of first note after inversion", None))
#endif // QT_CONFIG(tooltip)
        self.check_octave.setText(QCoreApplication.translate("Form", u"Add Octave", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Chord", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body>\n"
"<p>Enter notes to find matching chords.</p>\n"
"<p>Either MIDI keynumbers or note names may be used.</p>\n"
"<p>Names are specified their 'white' key root, an optional accidental, and an optional octave.</p>\n"
"<p><br/></p>\n"
"<p>Example e-flat is specified as Eb while d-sharp is D#.</p>\n"
"<p>Octaves are an integer between 0 and 10,   C4 and G#4 are</p>\n"
"<p>two notes in the 4th octave.   Generally the octave values are ignored.</p>\n"
"</body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Key", None))
#if QT_CONFIG(tooltip)
        self.radio_sharps.setToolTip(QCoreApplication.translate("Form", u"Display accidentals as sharps", None))
#endif // QT_CONFIG(tooltip)
        self.radio_sharps.setText(QCoreApplication.translate("Form", u"Sharps", None))
        self.label_10.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"Notes", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Matches", None))
#if QT_CONFIG(tooltip)
        self.line_edit_user_chord.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p>Enter notes to find matching chords.</p><p>Either MIDI keynumbers or note names may be used.</p><p>Names are specified their 'white' key root, an optional</p><p>accidental, and an optional octave.</p><p><br/></p><p>Example e-flat is specified as Eb while d-sharp is D#.</p><p>Octaves are an integer between 0 and 10,   C4 and G#4 are</p><p>two notes in the 4th octave.   Generally the octave values are</p><p>ignored.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.line_edit_user_chord.setText(QCoreApplication.translate("Form", u"C E G Bb", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Chord Locator", None))
#if QT_CONFIG(tooltip)
        self.radio_sub.setToolTip(QCoreApplication.translate("Form", u"Match chords which are contained by specified notes.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_sub.setText(QCoreApplication.translate("Form", u"Sub Chords", None))
#if QT_CONFIG(tooltip)
        self.radio_super.setToolTip(QCoreApplication.translate("Form", u"Match chords which contain all of the specified notes.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_super.setText(QCoreApplication.translate("Form", u"Super Chords", None))
#if QT_CONFIG(tooltip)
        self.radio_match.setToolTip(QCoreApplication.translate("Form", u"Returns chords with threshold percent of matching notes.", None))
#endif // QT_CONFIG(tooltip)
        self.radio_match.setText(QCoreApplication.translate("Form", u"Similarity", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Threshold ", None))
        self.button_find_chords.setText(QCoreApplication.translate("Form", u"Find Chords", None))
    # retranslateUi

