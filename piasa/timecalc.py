from PySide2.QtWidgets import QWidget
import piasa.ui.timecalc_form


class TimeCalculator:
    """
    TimeCalculator is a time unit conversion calculator.

    Supported units include uSecond mSecond, Second, Minute and Hour,
    Conversion between sample and frame count to time is also provided.
    """

    @classmethod
    def micro_to_second(cls, n: float) -> float:
        """Converts microseconds to seconds."""
        return n / 1e6

    @classmethod
    def milli_to_second(cls, n: float) -> float:
        """Converts milliseconds to seconds."""
        return n / 1e3

    @classmethod
    def second_to_second(cls, n: float) -> float:
        """Identity, converts seconds to seconds."""
        return float(n)

    @classmethod
    def minute_to_second(cls, n: float) -> float:
        """Converts minutes to seconds."""
        return n * 60.0

    @classmethod
    def hour_to_second(cls, n: float) -> float:
        """Converts hours to seconds."""
        return n * 3600.0

    @classmethod
    def second_to_micro(cls, n: float) -> float:
        """Converts seconds to microseconds."""
        return n * 10e6

    @classmethod
    def second_to_milli(cls, n: float) -> float:
        """Converts seconds to milliseconds."""
        return n * 10e3

    @classmethod
    def second_to_minute(cls, n: float) -> float:
        """Converts seconds to minutes."""
        return n / 60.0

    @classmethod
    def second_to_hour(cls, n: float) -> float:
        """Converts seconds to hours."""
        return n / 3600.0

    def __init__(self):
        self.form = QWidget()
        self._ui = piasa.ui.timecalc_form.Ui_Form()
        self._ui.setupUi(self.form)
        self._input_scale_buttons = [self._ui.radio_in_samples,
                                     self._ui.radio_in_frames,
                                     self._ui.radio_in_micro,
                                     self._ui.radio_in_milli,
                                     self._ui.radio_in_second,
                                     self._ui.radio_in_minute,
                                     self._ui.radio_in_hour]
        self._output_scale_buttons = [self._ui.radio_out_samples,
                                      self._ui.radio_out_frames,
                                      self._ui.radio_out_micro,
                                      self._ui.radio_out_milli,
                                      self._ui.radio_out_second,
                                      self._ui.radio_out_minute,
                                      self._ui.radio_out_hour]
        self._input_conversion_functions = {
            self._ui.radio_in_samples: self.sample_to_second,
            self._ui.radio_in_frames: self.frame_to_second,
            self._ui.radio_in_micro : TimeCalculator.micro_to_second,
            self._ui.radio_in_milli : TimeCalculator.milli_to_second,
            self._ui.radio_in_second : TimeCalculator.second_to_second,
            self._ui.radio_in_minute : TimeCalculator.minute_to_second,
            self._ui.radio_in_hour : TimeCalculator.hour_to_second}
        self._output_conversion_functions = {
            self._ui.radio_out_samples : self.second_to_sample,
            self._ui.radio_out_frames : self.second_to_frame,
            self._ui.radio_out_micro : TimeCalculator.second_to_micro,
            self._ui.radio_out_milli : TimeCalculator.second_to_milli,
            self._ui.radio_out_second : TimeCalculator.second_to_second,
            self._ui.radio_out_minute : TimeCalculator.second_to_minute,
            self._ui.radio_out_hour : TimeCalculator.second_to_hour}
        self._current_input_scale_button = self._ui.radio_in_second
        self._current_output_scale_button = self._ui.radio_out_second
        self._normalized_value: float = 0.0
        self._input_transform = TimeCalculator.second_to_second
        self._output_transform = TimeCalculator.second_to_second
        for rb in self._input_scale_buttons:
             rb.clicked.connect(self._input_scale_slot_factory(rb))
        for index, rb in enumerate(self._output_scale_buttons):
            rb.clicked.connect(self._output_scale_slot_factory(rb))
            # Ensure both set of scale buttons have exact same text.
            self._input_scale_buttons[index].setText(rb.text())
        self._ui.dspin_input.valueChanged.connect(self._input_value_changed)
        self._ui.dspin_samplerate.valueChanged.connect(lambda x: self.update_ui())
        self._ui.spin_framerate.valueChanged.connect(lambda x: self.update_ui())
        self._ui.button_reset.clicked.connect(lambda x: self._reset())
        self._ui.button_swap.clicked.connect(self._swap)
        self.update_ui()

    def _input_value_changed(self, *_):
        try:
            text = self._ui.dspin_input.text()
            value = float(text)
            self.update_ui()
        except ValueError:
            pass

    def _input_scale_slot_factory(self, client):
        def slot(*_):
            self._input_transform = self._input_conversion_functions[client]
            self.update_ui()
            self._current_input_scale_button = client
        return slot

    def _output_scale_slot_factory(self, client):
        def slot(*_):
            self._output_transform = self._output_conversion_functions[client]
            self.update_ui()
            self._current_output_scale_button = client
        return slot

    def _reset(self, *_):
        self._ui.radio_in_second.click()
        self._ui.radio_out_second.click()
        self._ui.dspin_samplerate.setValue(41.1)
        self._ui.dspin_input.setValue(1.0)
        self.update_ui()

    # Exchanges 'From' and 'To values
    #
    def _swap(self, *_):
        new_in = self.transformed_value
        old_in_scale = self._current_input_scale_button.text()
        old_out_scale = self._current_output_scale_button.text()
        for rb in self._input_scale_buttons:
            if rb.text() == old_out_scale:
                rb.click()
                break
        for rb in self._output_scale_buttons:
            if rb.text() == old_in_scale:
                rb.click()
                break
        self._ui.dspin_input.setValue(new_in)

    @property
    def input_value(self) -> float:
        """Value of 'From' spinner"""
        return self._ui.dspin_input.value()

    @property
    def value_in_seconds(self) -> float:
        """Value of 'From' spinner, converted to seconds."""
        return self._input_transform(self.input_value)

    @property
    def transformed_value(self) -> float:
        """Value of 'From' spinner converted to currently selected 'To' unit."""
        s = self.value_in_seconds
        return self._output_transform(s)

    @property
    def compound_value(self):
        """Formats time in hour:min:sec format."""
        sec = self.value_in_seconds
        hr = int(sec / 3600)
        sec -= hr * 3600
        min = int(sec / 60)
        sec -= min * 60
        frmt = "%02d : %02d : %7.4f"
        return frmt % (hr, min, sec)

    @property
    def scale(self) -> str:
        """The currently selected scale factor."""
        if self.transformed_value != 0:
            s = self.input_value / self.transformed_value
            return "%3.4f" % s
        else:
            return "infinity"

    @property
    def sample_rate(self):
        """The value of 'Sample Rate' spinner in hz."""
        return self._ui.dspin_samplerate.value() * 1000

    def sample_to_second(self, n: int) -> float:
        """Converts sample count to seconds."""
        return n / self.sample_rate

    def second_to_sample(self, s: float) -> int:
        """Converts seconds to sample count."""
        return round(s * self.sample_rate)

    @property
    def frame_rate(self):
        """The value of the 'Frame Rate' spinner."""
        return self._ui.spin_framerate.value()

    def frame_to_second(self, n: int) -> float:
        """Converts frame count to seconds."""
        return float(n) / self.frame_rate

    def second_to_frame(self, s: float) -> int:
        """Converts seconds to frame count."""
        return round(s * self.frame_rate)

    def update_ui(self):
        value = self.transformed_value
        self._ui.line_edit_output.setText(str(value))
        self._ui.line_edit_scale.setText(self.scale)
        self._ui.line_edit_compound.setText(self.compound_value)

