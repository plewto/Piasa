from math import log
from PySide2.QtWidgets import QWidget
from piasa.ui.tune_panel import Ui_Form

CENT = 2 ** (1/1200)


def key_name(pclass: int) -> str:
    """
    Converts pitch-class to key template_name/
    :param pclass: The pitch class, an int between 0 and 11 inclusive.
    :return: String representation of pclass.
    """
    lst = ("C ", "C#", "D ", "D#",
           "E ", "F ", "F#", "G ",
           "G#", "A ", "A#", "B ")
    return lst[pclass]


class TuneCalculator:
    """TuneCalculator calculates tuning tables for equal tempered scales."""
    def __init__(self):
        self.form = QWidget()
        self._ui = Ui_Form()
        self._ui.setupUi(self.form)
        self.update_ui()
        self._ui.spin_notes_per_octave.valueChanged.connect(self.update_ui)
        self._ui.spin_reference_key.valueChanged.connect(self.update_ui)
        self._ui.dspin_ref_frequency.valueChanged.connect(self.update_ui)
        self._ui.dspin_speed_of_sound.valueChanged.connect(self.update_ui)
        self._ui.buttonReset.clicked.connect(self._reset)

    @property
    def notes_per_octave(self) -> int:
        """Value of 'Notes Per Octave' spinner."""
        return self._ui.spin_notes_per_octave.value()

    @property
    def reference_key(self) -> int:
        """
        The current value of the 'Reference Key' spinner,

        The reference key is the MIDI key number used for tuning the table.
        The default value of 57 corresponds to middle A.
        """
        return self._ui.spin_reference_key.value()

    @property
    def reference_frequency(self) -> float:
        """
        The current value of the 'Reference Frequency' spinner.

        The reference frequency sets the frequency valuer corresponding to the reference key.
        The default value is 440 hz.
        """
        return  self._ui.dspin_ref_frequency.value()

    @property
    def step_ratio(self):
        """The step ratio between adjacent notes."""
        return 2**(1/self.notes_per_octave)

    def transpose(self, start, steps):
        """Transposes frequency by given number of steps using the current step_ratio."""
        ratio = self.step_ratio ** steps
        return start * ratio

    @property
    def base_frequency(self):
        """The frequency in hz for keynumber 0."""
        rf = self.reference_frequency
        return self.transpose(rf, -self.reference_key)

    def _reset(self, *_):
        self._ui.spin_notes_per_octave.setValue(12)
        self._ui.spin_reference_key.setValue(57)
        self._ui.dspin_ref_frequency.setValue(440.0)
        self._ui.dspin_speed_of_sound.setValue(343.0)

    def _rescale(self):
        self._ui.list_frequencies.clear()
        freq = self.base_frequency
        ratio = self.step_ratio
        c = self._ui.dspin_speed_of_sound.value()
        for k in range(0, 128):
            octave = int(k / 12)
            pclass = key_name(k % 12)
            period = 1.0 / freq
            wavelength = c / freq
            s = "[%03d %2d : %2s] %10.4f  %8.6f  %7.4f" % (k, octave, pclass, freq, period, wavelength)
            self._ui.list_frequencies.insertItem(k, s)
            freq *= ratio

    def update_ui(self):
        self._rescale()
        sr = self.step_ratio
        cents = log(sr, CENT)
        frmt = "%6.4f"
        self._ui.line_edit_ratio.setText(frmt % sr)
        self._ui.line_edit_cents.setText(str(round(cents)))


