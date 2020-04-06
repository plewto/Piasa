"""
Defines ScaleCalculator class.
"""

from PySide2.QtWidgets import QWidget
import piasa.ui.scale_panel
from piasa.scale.keynumber import keyname, TRANSPOSE_OPTIONS
from piasa.scale.scales import SCALE_DICTIONARY


class ScaleCalculator:
    """
    ScaleCalculator provides GUI component to inspect scales.
    """
    def __init__(self):
        self.form = QWidget()
        self._ui = piasa.ui.scale_panel.Ui_Form()
        self._ui.setupUi(self.form)
        self._ui.combo_scale.insertItems(0, list(SCALE_DICTIONARY.keys()))
        self._ui.combo_scale.setCurrentIndex(1)
        self._ui.combo_key.insertItems(0, TRANSPOSE_OPTIONS)
        self._ui.combo_key.setCurrentIndex(0)
        self._ui.combo_scale.currentIndexChanged.connect(self.update_ui)
        self._ui.combo_key.currentIndexChanged.connect(self.update_ui)
        self._ui.radio_flat.clicked.connect(self.update_ui)
        self._ui.radio_sharp.clicked.connect(self.update_ui)
        self.update_ui()

    @property
    def _use_flats(self):
        return self._ui.radio_flat.isChecked()

    @property
    def _transpose(self):
        return self._ui.combo_key.currentIndex()

    def update_ui(self, *_):
        scale_index = self._ui.combo_scale.currentIndex()
        scale_key = list(SCALE_DICTIONARY.keys())[scale_index]
        scale = SCALE_DICTIONARY[scale_key]
        self._ui.line_edit_comments.setText(scale.comments)
        acc = ""
        template = list(scale.template)
        template.append(template[0])
        for index, note in enumerate(keyname(template, self._use_flats)):
            if index == len(template) - 1:
                note = f"{note}`"
            acc += "%-4s" % note
        self._ui.line_edit_template.setText(acc)
        acc = " " * 2
        for step in scale._interval_sequence():
            acc += "%-4s" % step
        self._ui.line_edit_step_pattern.setText(acc)
        scale2 = scale.transposed(self._transpose)
        acc = ""
        for note in scale2.template:
            acc += "%-4s" % keyname(note, self._use_flats)
        acc += "%s`" % keyname(scale2.template[0], self._use_flats)
        self._ui.line_edit_transposed_scale.setText(acc)




