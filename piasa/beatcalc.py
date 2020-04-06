"""
BeatCalculator determines note durations for given tempo and time-signature.

Durations may be displayed in either seconds or clock ticks.  The user selects a tempo in BPM, a phrase length in
bars, the number of beats per bar and the number of ticks per beat.  From these values the durations of corresponding
phrase, bar, whole-note, half-note, quarter-note, eighth-note, sixteenth-note, thirtysecond-note and sixtyfourth-note
are calculated.  A separate 'tuplet' duration is calculated for all note values.  The tuplet may be set for dotted,
double-dotted, triplet, or user-defined ratio.
"""

from PySide2.QtWidgets import QWidget
from piasa.ui.beat_panel import Ui_Form
from enum import IntEnum
from fractions import Fraction
import piasa.ui.beat_panel


class DisplayUnit(IntEnum):
    SECONDS = 0
    TICKS = 1


class BeatCalculator:

    def __init__(self):
        self.form = QWidget()
        self._ui = piasa.ui.beat_panel.Ui_Form()
        self._ui.setupUi(self.form)
        self._unit = DisplayUnit.SECONDS
        self._tuplet_ratio = Fraction(3,2)
        self._init_unit_slots()
        self._init_tuplet_slots()
        self._ui.dspin_tempo.valueChanged.connect(lambda x: self.update_ui())
        self._ui.spin_bar_count.valueChanged.connect(lambda x: self.update_ui())
        self._ui.spin_beat_count.valueChanged.connect(lambda x: self.update_ui())
        self._ui.spin_tick_count.valueChanged.connect(lambda x: self.update_ui())
        self._time_spinners = [self._ui.dspin_phrase,
                               self._ui.dspin_bar,
                               self._ui.dspin_whole,
                               self._ui.dspin_half,
                               self._ui.dspin_quarter,
                               self._ui.dspin_eighth,
                               self._ui.dspin_sixteen,
                               self._ui.dspin_thrirtysecond,
                               self._ui.dspin_sixtyfour,
                               self._ui.dspin_whole_tuplet,
                               self._ui.dspin_half_tuplet,
                               self._ui.dspin_quarter_tuplet,
                               self._ui.dspin_eighth_tuplet,
                               self._ui.dspin_sixteen_tuplet,
                               self._ui.dspin_thirtysecond_tuplet,
                               self._ui.dspin_sixtyfour_tuplet,
                               self._ui.dspin_tick]
        self._ui.buttonReset.clicked.connect(self._reset_slot)

    def _init_unit_slots(self):
        self._ui.radio_units_seconds.clicked.connect(self._use_seconds)
        self._ui.radio_unit_ticks.clicked.connect(self._use_ticks)

    def _init_tuplet_slots(self):

        def select_standard(n: int, d: int):
            ratio = Fraction(n, d)
            self._tuplet_ratio = ratio
            self._ui.spin_tuplet_numerator.setEnabled(False)
            self._ui.spin_tuplet_denominator.setEnabled(False)
            self.update_ui()

        def select_other(*_):
            n = self._ui.spin_tuplet_numerator.value()
            d = self._ui.spin_tuplet_denominator.value()
            self._tuplet_ratio = Fraction(n, d)
            self._ui.spin_tuplet_numerator.setEnabled(True)
            self._ui.spin_tuplet_denominator.setEnabled(True)
            self.update_ui()

        def change_ratio(*_):
            n = self._ui.spin_tuplet_numerator.value()
            d = self._ui.spin_tuplet_denominator.value()
            self._tuplet_ratio = Fraction(n, d)
            self.update_ui()

        self._ui.radio_tuplet_dot.clicked.connect(lambda x: select_standard(3, 2))
        self._ui.radio_tuplet_dotdot.clicked.connect(lambda x: select_standard(9, 4))
        self._ui.radio_tuplet_tripplet.clicked.connect(lambda x: select_standard(2, 3))
        self._ui.radio_tuplet_other.clicked.connect(select_other)
        self._ui.spin_tuplet_numerator.valueChanged.connect(change_ratio)
        self._ui.spin_tuplet_denominator.valueChanged.connect(change_ratio)

    def _use_seconds(self, *_):
        self._unit = DisplayUnit.SECONDS
        for spinner in self._time_spinners:
            spinner.setDecimals(4)
        self.update_ui()

    def _use_ticks(self, *_):
        self._unit = DisplayUnit.TICKS
        for spinner in self._time_spinners:
            spinner.setDecimals(0)
        self.update_ui()

    def _reset_slot(self, *_):
        self._ui.dspin_tempo.setValue(60)
        self._ui.spin_bar_count.setValue(1)
        self._ui.spin_beat_count.setValue(4)
        self._ui.spin_tick_count.setValue(120)
        self._ui.radio_units_seconds.click()
        self._ui.radio_tuplet_dot.click()

    @property
    def tempo(self) -> float:
        return self._ui.dspin_tempo.value()

    @property
    def bar_count(self) -> int:
        return self._ui.spin_bar_count.value()

    @property
    def beat_count(self) -> int:
        return self._ui.spin_beat_count.value()

    @property
    def ticks_per_beat(self) -> int:
        return self._ui.spin_tick_count.value()

    @property
    def beat_duration(self):
        if self._unit == DisplayUnit.SECONDS:
            return 60.0 / self.tempo
        else:
            return self.ticks_per_beat

    @property
    def phrase_duration(self):
        return self.bar_duration * self.bar_count

    @property
    def bar_duration(self):
        return self.beat_duration * self.beat_count

    @property
    def tick_duration(self):
        if self._unit == DisplayUnit.SECONDS:
            return self.beat_duration / self.ticks_per_beat
        else:
            return 1

    @property
    def whole_note_duration(self):
        return self.beat_duration * 4

    @property
    def half_note_duration(self):
        return self.beat_duration * 2

    @property
    def quarter_note_duration(self):
        return self.beat_duration * 1

    @property
    def eighth_note_duration(self):
        return self.beat_duration * Fraction(1, 2)

    @property
    def sixteenth_note_duration(self):
        return self.beat_duration * Fraction(1, 4)

    @property
    def thirtysecond_note_duration(self):
        return self.beat_duration * Fraction(1, 8)

    @property
    def sixtyfourth_note_duration(self):
        return self.beat_duration * Fraction(1, 16)

    @property
    def whole_tuplet_duration(self):
        return self.whole_note_duration * self._tuplet_ratio

    @property
    def half_tuplet_duration(self):
        return self.half_note_duration * self._tuplet_ratio

    @property
    def quarter_tuplet_duration(self):
        return self.quarter_note_duration * self._tuplet_ratio

    @property
    def eighth_tuplet_duration(self):
        return self.eighth_note_duration * self._tuplet_ratio

    @property
    def sixteenth_tuplet_duration(self):
        return self.sixteenth_note_duration * self._tuplet_ratio

    @property
    def thirtysecond_tuplet_duration(self):
        return self.thirtysecond_note_duration * self._tuplet_ratio

    @property
    def sixtyfourth_tuplet_duration(self):
        return self.sixtyfourth_note_duration * self._tuplet_ratio

    def _update_duration_spinners(self):
        self._ui.dspin_phrase.setValue(self.phrase_duration)
        self._ui.dspin_bar.setValue(self.bar_duration)
        self._ui.dspin_whole.setValue(self.whole_note_duration)
        self._ui.dspin_half.setValue(self.half_note_duration)
        self._ui.dspin_quarter.setValue(self.quarter_note_duration)
        self._ui.dspin_eighth.setValue(self.eighth_note_duration)
        self._ui.dspin_sixteen.setValue(self.sixteenth_note_duration)
        self._ui.dspin_thrirtysecond.setValue(self.thirtysecond_note_duration)
        self._ui.dspin_sixtyfour.setValue(self.sixtyfourth_note_duration)
        self._ui.dspin_whole_tuplet.setValue(self.whole_tuplet_duration)
        self._ui.dspin_half_tuplet.setValue(self.half_tuplet_duration)
        self._ui.dspin_quarter_tuplet.setValue(self.quarter_tuplet_duration)
        self._ui.dspin_eighth_tuplet.setValue(self.eighth_tuplet_duration)
        self._ui.dspin_sixteen_tuplet.setValue(self.sixteenth_tuplet_duration)
        self._ui.dspin_thirtysecond_tuplet.setValue(self.thirtysecond_tuplet_duration)
        self._ui.dspin_sixtyfour_tuplet.setValue(self.sixtyfourth_tuplet_duration)
        self._ui.dspin_tick.setValue(self.tick_duration)

    def update_ui(self):
        self._update_duration_spinners()
