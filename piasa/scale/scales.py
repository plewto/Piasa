"""
Defines Scale class.
"""

from piasa.scale.keynumber import keyname, keynumber, transpose
from piasa.scale.keynumber import C, Cs, Db, D, Ds, Eb, E, F, Fs, Gb, G, Gs, Ab, A, As, Bb, B


class Scale:
    """
    Scale defines musical scales in terms of a keynumber template list.
    """

    def __init__(self, name: str, template: list, ascending=True, use_flats=False, comments=""):
        self.name: str = name
        self.template: list = keynumber(template)
        self.ascending: bool = ascending
        self.use_flats: bool = use_flats
        self.comments = comments

    def __len__(self):
        return len(self.template)

    def __getitem__(self, index):
        return self.template[index]

    def _append_octave(self, xpose: int = 0) -> list:
        tmp = transpose(list(self.template), xpose)
        if self.ascending:
            tmp.append(transpose(tmp[0], 12))
        else:
            tmp.append(transpose(tmp[0], -12))
        return tmp

    def _interval_sequence(self) -> list:
        tmp = self._append_octave(12)
        acc = []
        for index in range(1, len(tmp)):
            a = keynumber(tmp[index - 1])
            b = keynumber(tmp[index])
            acc.append(b - a)
        return acc

    def transposed(self, steps: int, new_name=None) -> "Scale":
        """
        Produces transposed copy of scale template.
        :param steps:
        :param new_name:
        :return:
        """
        s = Scale(new_name or self.name, transpose(self.template, steps))
        return s

    # NOTE: scale degree is zero based as apposed to the more common
    # musical practice of 1 based.
    def degree(self, n: int, new_name=None) -> "Scale":
        n = n % len(self)
        tmp = self._append_octave()[:-1]
        head, tail = tmp[:n], tmp[n:]
        s = Scale(new_name or self.name, tail + head)
        s.ascending = self.ascending
        s.use_flats = self.use_flats
        return s

    def __str__(self):
        s = f"{self.name} : "
        for q in self._append_octave():
            s += "%3s " % keyname(q, self.use_flats)
        return s


SCALE_DICTIONARY = {
    "Chromatic": Scale("Chromatic", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
    "Major": Scale("Major", [C, D, E, F, G, A, B]),
    "Minor(natural)": Scale("Minor(natural)", [C, D, Eb, F, G, Ab, Bb], use_flats=True),
    "Minor(harmonic)": Scale("Minor(harmonic)", [C, D, Eb, F, G, Ab, B], use_flats=True),
    "Minor(melodic ascending)": Scale("Minor(melodic ascending)", [C, D, Eb, F, G, A, B], use_flats=True),
    "Minor(melodic descending)": Scale("Minor(melodic descending)", ['C1', Bb, Ab, G, F, Eb, D], use_flats=True,
                                       ascending=False),
    "Ionian": Scale("Ionian", [C, D, E, F, G, A, B], use_flats=True, comments="Mode I, equivalent to major scale"),
    "Dorian": Scale("Dorian", [C, D, Eb, F, G, A, Bb], use_flats=True, comments="Mode II"),
    "Phrygian": Scale("Phrygian", [C, Db, Eb, F, G, Ab, Bb], use_flats=True, comments="Mode III"),
    "Lydian": Scale("Lydian", [C, D, E, Fs, G, A, B], use_flats=False, comments="Mode IV"),
    "Mixolydian": Scale("Mixolydian", [C, D, E, F, G, A, Bb], use_flats=True, comments="Mode V"),
    "Aeolian": Scale("Aeolian", [C, D, Eb, F, G, Ab, Bb], use_flats=True,
                     comments="Mode VI, equivalent to natural minor scale"),
    "Lorcian": Scale("Lorcian", [C, Db, Eb, F, Gb, Ab, Bb], use_flats=True, comments="Mode VII"),
    "Whole Tone": Scale("Whole Tone", [C, D, E, Fs, Gs, As]),
    "Octatonic": Scale("Octatonic", ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B']),
    "Acoustic": Scale("Acoustic", [C, D, E, Fs, G, A, Bb]),
    "Altered": Scale("Altered", [C, Db, Eb, E, Gb, Ab, Bb]),
    "Half diminished": Scale("Half diminished", [C, D, Eb, F, Gb, Ab, Bb], use_flats=True),
    "Neapolitan major": Scale("Neapolitan major", [C, Db, Eb, F, G, A, B], use_flats=TabError),
    "Hungarian": Scale("Hungarian", [C, D, Eb, Fs, G, Ab, Bb], use_flats=True),
    "Enigmatic": Scale("Enigmatic", [C, Db, E, Fs, Gs, As, B]),
    "Pentatonic-1": Scale("Pentatonic-1", [C, D, F, G, A], comments="The 'black key' scale"),
    "Pentatonic-2": Scale("Pentatonic-2", [C, Eb, F, G, Bb]),
    "Pentatonic-3": Scale("Pentatonic-3", [C, Db, F, G, Ab]),
    "Pentatonic-4": Scale("Pentatonic-4", [C, D, E, F, G, A]),
    "Arabic": Scale("Arabic", [C, Db, Eb, F, G, Ab], comments="A rough approximation at best")}
