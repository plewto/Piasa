"""Defines ChordCalculator class."""

from enum import Enum
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QWidget, QListWidgetItem
from piasa.scale.chords import Chord, CHORD_TEMPLATE_DICTIONARY, CHORD_DICTIONARY
from piasa.scale.keynumber import TRANSPOSE_OPTIONS, keyname, transpose, keynumber, pitchclass, octave
from piasa.util import is_int
import piasa.ui.chord_panel

_INTERVALS = (
    "Root",
    "min2",
    "Maj2",
    "min3",
    "Maj3",
    "Per4",
    "Dim5",
    "Per5",
    "min6",
    "Maj6",
    "Dom7",
    "Maj7")


def interval_pattern(template: list) -> str:
    """
    Determines other interval structure.

    :param template: list of key-numbers.
    :return: String description of other's structure.
    """
    acc = ""
    i = 1
    while i < len(template):
        b = template[i]
        a = template[i-1]
        diff = (b - a) % 12
        acc += f"{_INTERVALS[diff]}  "
        i += 1
    return acc


class ChordMatchMode(Enum):
    SUB = 1,
    SUPER = 2,
    SIMILARITY = 3


class ChordCalculator:
    """
    ChordCalculator provides controls for inspection of other structures.

    The UI is divided into two parts.  In the upper part the user selects a other type from a pre-defined set.
    Transposition and inversion options are selected and the other structure is displayed.

    In the bottom section the user enters a sequence of notes and ChordCalculator displays a list of possible chords
    containing those notes.
    """
    def __init__(self):
        self.form = QWidget()
        self._ui = piasa.ui.chord_panel.Ui_Form()
        self._ui.setupUi(self.form)
        self._ui.combo_chord_list.insertItems(0, CHORD_TEMPLATE_DICTIONARY.keys())
        self._ui.combo_key.insertItems(0, TRANSPOSE_OPTIONS)
        self._ui.combo_chord_list.currentIndexChanged.connect(self.update_ui)
        self._ui.combo_key.currentIndexChanged.connect(self.update_ui)
        self._ui.spin_inversion.valueChanged.connect(self.update_ui)
        self._ui.radio_flats.clicked.connect(self.update_ui)
        self._ui.radio_sharps.clicked.connect(self.update_ui)
        self._ui.check_octave.clicked.connect(self.update_ui)
        self._ui.button_find_chords.clicked.connect(self._find_chords)
        self._edit_palette = self._ui.line_edit_user_chord.palette()
        self._normal_background = self._edit_palette.color(self._ui.line_edit_user_chord.backgroundRole())
        self._warning_background = QColor(250, 200, 200)
        self._ui.line_edit_user_chord.setAutoFillBackground(True)
        self._ui.line_edit_user_chord.textChanged.connect(self._validate_user_chord)
        self._ui.radio_sub.clicked.connect(self._find_chords)
        self._ui.radio_super.clicked.connect(self._find_chords)
        self._ui.radio_match.clicked.connect(self._find_chords)
        self._ui.dspin_threshold.valueChanged.connect(self._find_chords)
        self._ui.list_chord_hits.itemClicked.connect(self._finder_clicked)
        self.update_ui()

    @property
    def chord(self) -> str:
        index = self._ui.combo_chord_list.currentIndex()
        return list(CHORD_TEMPLATE_DICTIONARY.keys())[index]

    @property
    def transpose(self) -> int:
        return self._ui.combo_key.currentIndex()

    @property
    def inversion(self) -> int:
        return self._ui.spin_inversion.value()

    @property
    def use_flats(self) -> bool:
        return self._ui.radio_flats.isChecked()

    @property
    def add_octave(self) -> bool:
        return self._ui.check_octave.isChecked()

    @property
    def template(self) -> list:
        chord = CHORD_TEMPLATE_DICTIONARY[self.chord]
        return chord.inversion(self.inversion, self.add_octave)

    @property
    def chord_match_mode(self) -> ChordMatchMode:
        ui = self._ui
        if ui.radio_sub.isChecked():
            return ChordMatchMode.SUB
        elif ui.radio_super.isChecked():
            return ChordMatchMode.SUPER
        else:
            return ChordMatchMode.SIMILARITY

    def keylist_to_string(self, keylist: list) -> str:
        acc = ""
        for keynumber in keylist:
            acc += "%s  " % keyname(keynumber, self.use_flats)
        return acc

    def _clear_text_background(self):
        w = self._ui.line_edit_user_chord
        p = self._edit_palette
        p.setColor(w.backgroundRole(), self._normal_background)
        w.setPalette(p)

    def _set_warning_background(self):
        w = self._ui.line_edit_user_chord
        p = self._edit_palette
        p.setColor(w.backgroundRole(), self._warning_background)
        w.setPalette(p)

    def _validate_user_chord(self, text: str) -> list:
        self._clear_text_background()
        tokens = text.split()
        acc = []
        for token in tokens:
            if is_int(token):
                token = int(token)
            else:
                token = token.capitalize()
            try:
                acc.append(keynumber(token))
            except KeyError:
                self._set_warning_background()
                return []
        return acc

    def _find_super_chords(self, user_chord: Chord):
        qlist = self._ui.list_chord_hits
        qlist.clear()
        acc = []
        for name, prospect in CHORD_DICTIONARY.items():
            if prospect.contains_chord(user_chord.template):
                acc.append(name)
        qlist.insertItems(0, acc)

    def _find_sub_chords(self, user_chord: Chord):
        qlist = self._ui.list_chord_hits
        qlist.clear()
        acc = []
        for name, prospect in CHORD_DICTIONARY.items():
            if prospect.is_sub_chord(user_chord.template):
                acc.append(name)
        qlist.insertItems(0, acc)

    def _find_similar_chords(self, user_chord: Chord, threshold: float):
        qlist = self._ui.list_chord_hits
        qlist.clear()
        acc = []
        for name, prospect in CHORD_DICTIONARY.items():
            match = prospect.similarity(user_chord.template)
            if match >= threshold:
                acc.append(name)
        qlist.insertItems(0, acc)

    def _find_chords(self, *_):
        user_pattern = self._validate_user_chord(self._ui.line_edit_user_chord.text())
        if user_pattern:
            root = user_pattern[0]
            root_pc = pitchclass(root)
            root_octave = octave(root)
            if root_octave > 0:
                user_pattern = transpose(user_pattern, -12 * root_octave)
                root = root_pc
            user_chord = Chord("User", user_pattern)
            mode = self.chord_match_mode
            if mode == ChordMatchMode.SUB:
                self._ui.dspin_threshold.setEnabled(False)
                self._find_sub_chords(user_chord)
            elif mode == ChordMatchMode.SUPER:
                self._ui.dspin_threshold.setEnabled(False)
                self._find_super_chords(user_chord)
            else:
                self._ui.dspin_threshold.setEnabled(True)
                threshold = self._ui.dspin_threshold.value()
                self._find_similar_chords(user_chord, threshold)

    def _finder_clicked(self, item: QListWidgetItem):
        text = item.text()
        key = text.split()[0]
        # xpose = pitchclass(key)
        chord_name = text[len(key):].strip()
        self._ui.combo_chord_list.setCurrentText(chord_name)
        self._ui.combo_key.setCurrentIndex(pitchclass(key))


    def update_ui(self, *_):
        template = self.template
        self._ui.line_edit_template.setText(self.keylist_to_string(template))
        self._ui.line_edit_pattern.setText(interval_pattern(template))
        chord = transpose(template, self.transpose)
        self._ui.line_edit_chord.setText(self.keylist_to_string(chord))
