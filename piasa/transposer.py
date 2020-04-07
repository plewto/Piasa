from math import log
from PySide2.QtWidgets import QWidget
import piasa.ui.transpose_panel
from piasa.util import CENT, feet_to_meter, meter_to_feet


class Transposer:
    """
    Determines transposition required to convert one frequency into another.

    The transposition amount is presented as 12-TET steps plus cents.
    """
    def __init__(self):
        self.form = QWidget()
        self._ui = piasa.ui.transpose_panel.Ui_Form()
        self._ui.setupUi(self.form)
        self._enable_signals = True
        self._ui.radio_frequency.clicked.connect(self._select_input_unit)
        self._ui.radio_time.clicked.connect(self._select_input_unit)
        self._ui.radio_frequency.click()
        self._ui.radio_metric.clicked.connect(self._use_metric)
        self._ui.radio_imperial.clicked.connect(self._use_imperial)
        self._ui.dspin_freq0.valueChanged.connect(self._input_value_changed)
        self._ui.dspin_freq1.valueChanged.connect(self._input_value_changed)
        self._ui.dspin_time0.valueChanged.connect(self._input_value_changed)
        self._ui.dspin_time1.valueChanged.connect(self._input_value_changed)
        self._ui.dspin_speed.valueChanged.connect(self._update_ui)
        self._ui.button_reset.clicked.connect(self._reset)
        self._update_ui()

    def _reset(self, *_):
        ui = self._ui
        self._enable_signals = False
        ui.radio_frequency.setChecked(True)
        ui.radio_metric.setChecked(True)
        ui.dspin_freq0.setValue(1.0)
        ui.dspin_freq1.setValue(1.0)
        ui.dspin_speed.setValue(343.0)
        self._update_ui()

    def _input_value_changed(self, *_):
        if self._enable_signals:
            self._update_ui()

    def _select_input_unit(self, *_):
        if self._ui.radio_frequency.isChecked():
            self._ui.dspin_freq0.setEnabled(True)
            self._ui.dspin_freq1.setEnabled(True)
            self._ui.dspin_time0.setEnabled(False)
            self._ui.dspin_time1.setEnabled(False)
        else:
            self._ui.dspin_freq0.setEnabled(False)
            self._ui.dspin_freq1.setEnabled(False)
            self._ui.dspin_time0.setEnabled(True)
            self._ui.dspin_time1.setEnabled(True)

    def _use_metric(self, *_):
        spinner = self._ui.dspin_speed
        ft = spinner.value()
        m = feet_to_meter(ft)
        spinner.setValue(m)
        spinner.setSuffix(" m/s")
        self._update_ui()

    def _use_imperial(self, *_):
        spinner = self._ui.dspin_speed
        m = spinner.value()
        ft = meter_to_feet(m)
        spinner.setSuffix(" ft/s")
        spinner.setValue(ft)
        self._update_ui()

    def _update_ui(self, *_):
        ui = self._ui
        self._enable_signals = False
        if ui.radio_frequency.isChecked():
            freq0 = ui.dspin_freq0.value()
            freq1 = ui.dspin_freq1.value()
            ui.dspin_time0.setValue(1 / freq0)
            ui.dspin_time1.setValue(1 / freq1)
        else:
            time0 = ui.dspin_time0.value()
            time1 = ui.dspin_time1.value()
            ui.dspin_freq0.setValue(1 / time0)
            ui.dspin_freq1.setValue(1 / time1)
        freq0 = ui.dspin_freq0.value()
        freq1 = ui.dspin_freq1.value()
        time0 = ui.dspin_time0.value()
        time1 = ui.dspin_time1.value()
        diff_freq = freq1 - freq0
        diff_time = time1 - time0
        ratio_freq = freq1 / freq0
        ratio_time = time1 / time0
        ui.line_edit_freq_diff.setText("%7.4f hz" % diff_freq)
        ui.line_edit_time_diff.setText("%7.4f sec" % diff_time)
        ui.line_edit_freq_ratio.setText("%7.4f" % ratio_freq)
        ui.line_edit_time_ratio.setText("%7.4f" % ratio_time)
        cents = log(ratio_freq, CENT)
        if cents < 0:
            sign = "-"
        else:
            sign = "+"
        cents = abs(cents)
        steps = int(cents / 100)
        cents = round(cents - 100 * steps)
        ui.line_edit_transpose.setText("%s%d steps  %d cents" % (sign, steps, cents))
        ui.line_edit_freq0_copy.setText("%7.4f hz" % freq0)
        c = ui.dspin_speed.value()
        _lambda = c / freq0
        if ui.radio_imperial.isChecked():
            unit = "ft"
        else:
            unit = "m"
        ui.line_edit_lambda.setText("%7.4f %s" % (_lambda, unit))

        self._enable_signals = True

