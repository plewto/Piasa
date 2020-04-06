from math import log
from PySide2.QtWidgets import QWidget
import piasa.ui.transpose_panel

CENTS = 2**(1/1200.0)


class Transposer:
    """
    Determines transposition required to convert one frequency into another.

    The transposition amount is presented as 12-TET steps plus cents.
    """
    def __init__(self):
        self.form = QWidget()
        self._ui = piasa.ui.transpose_panel.Ui_Form()
        self._ui.setupUi(self.form)
        self.update_ui()
        self._ui.dspin_starting.valueChanged.connect(self.update_ui)
        self._ui.dspin_required.valueChanged.connect(self.update_ui)

    @property
    def starting_value(self):
        """Value of 'Starting' spinner."""
        return self._ui.dspin_starting.value()

    @property
    def final_value(self):
        """Value of 'Required' spinner."""
        return self._ui.dspin_required.value()

    @property
    def ratio(self):
        """Ratio final/starting."""
        sv = self.starting_value
        if sv != 0:
            return self.final_value / sv
        else:
            return 1.0

    @property
    def diff(self):
        """The difference final - starting."""
        return abs(self.final_value - self.starting_value)

    @property
    def transpose_cents(self):
        """Required transposition in cents."""
        return log(self.ratio, CENTS)

    def update_ui(self, *_):
        self._ui.line_edit_scale.setText("%8.4f" % self.ratio)
        self._ui.line_edit_diff.setText(" %f" % self.diff)
        cents = self.transpose_cents
        if cents < 0:
            sign = "-"
        else:
            sign = "+"
        cents = abs(cents)
        steps = int(cents / 100)
        cents = round(cents - steps * 100)
        self._ui.line_edit_transpose.setText(" %s%d steps  %d cents" % (sign, steps, cents))

