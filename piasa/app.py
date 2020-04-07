"""Defines main Piasa application class as a Singleton."""

import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QTabWidget
from piasa.beatcalc import BeatCalculator
from piasa.scale.chord_calculator import ChordCalculator
from piasa.scale.scale_calculator import ScaleCalculator
from piasa.transposer import Transposer
from piasa.tunecalc import TuneCalculator
from piasa.timecalc import TimeCalculator


class Piasa(QMainWindow):

    __instance = None
    __qt_app = QApplication(sys.argv)

    def __init__(self):
        if Piasa.__instance:
            raise Exception("Piasa application already exists")
        else:
            QMainWindow.__init__(self)
            self.resize(635, 800)
            self.setWindowTitle("Piasa Producers Calculator")
            self.tab_pane = QTabWidget()
            self.setCentralWidget(self.tab_pane)
            self.time_calculator = TimeCalculator()
            self.beat_calculator = BeatCalculator()
            self.tune_calculator = TuneCalculator()
            self.transposer = Transposer()
            self.scale_calculator = ScaleCalculator()
            self.chord_calculator  = ChordCalculator()
            self.tab_pane.addTab(self.chord_calculator.form, "Chords")
            self.tab_pane.addTab(self.scale_calculator.form, "Scale")
            self.tab_pane.addTab(self.beat_calculator.form, "Beat")
            self.tab_pane.addTab(self.transposer.form, "Transpose")
            self.tab_pane.addTab(self.tune_calculator.form, "Tune")
            self.tab_pane.addTab(self.time_calculator.form, "Time")
            self.beat_calculator.update_ui()
            self.show()
            sys.exit(Piasa.__qt_app.exec_())

