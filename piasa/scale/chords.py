"""Defines the Chord class and pre-defined set of other types."""

from piasa.scale.keynumber import keynumber, transpose, pitchclass, keyname


# Rotates list of keynumbers by transposing first value up an octave
# and then move it to the end of the list.  Given a other, a single rotation
# provides one-level of inversion.
#
def _rotate_once(lst: list) -> list:
    acc = lst[1:]
    acc .append(transpose(lst[0], 12))
    return acc


# Rotates other list n times, returns the n-th inversion of the other.
#
def _rotate(lst: list, n: int) -> list:
    acc = list(lst)
    for i in range(n):
        acc = _rotate_once(acc)
    return acc


# Transposes keynumber list to the lowest octave.
# Assumes the first list element is the other's root.
#
def _base_form(chord: list) -> list:
    head = keynumber(chord[0])
    return transpose(chord, -head)


class Chord:

    """
    Defines a Chord by list of keynumbers.
    """

    def __init__(self, name, template, comments=""):
        self.name = str(name)
        self.template = template
        self.comments = str(comments)

    def transpose(self, steps: int) -> list:
        """
        Transposes other key numbers.
        :param steps: Size of transposition.
        :return: List of keynumbers.
        """
        return transpose(self.template, steps)

    def inversion(self, degree, add_octave = False) -> list:
        """
        Produces an inversion of self.
        :param degree: The inversion degree.  For each degree, the first note is transpose up an octave and rotated
        to the end of the keynumber list.
        :param add_octave:  If true, a copy of the first note -after- the inversion, is transposed up an octave
        and appended to the end of the keynumber list.
        :return: list of keynumbers.
        """
        tmp = _rotate(self.template, degree)
        if add_octave:
            head = tmp[0]
            tail = tmp[-1]
            octave = tail
            while pitchclass(octave) != pitchclass(head):
                octave += 1
            tmp.append(octave)
        return tmp

    def similarity(self, other: list) -> float:
        """
        Checks how similar self is to another other.
        :param other: keynumber list used for comparison.
        :return: A value between 0 and 1.  A value of 0 indicates the two chords have nothing in common.  A value of
        1 indicates that every note in other also appears in self.  The first note is ignored.
        """
        a = set(pitchclass(self.template))
        b = set(pitchclass(other))
        c = a.intersection(b)
        match = len(c) / len(a)
        return match

    def contains_chord(self, other: list) -> bool:
        """
        Checks if this other contains all the notes fo another other.
        :param other:  keynumber list under test.
        :return: True iff all notes in other also appear in self.
        """
        a = set(pitchclass(self.template))
        b = set(pitchclass(other))
        return b.issubset(a)

    def is_sub_chord(self, other) -> bool:
        """
        Checks if self is contained in another chord.
        :param other: keynumber list for chord under test.
        :return: True iff all notes in self also appear in other.
        """
        a = set(pitchclass(self.template))
        b = set(pitchclass(other))
        return a.issubset(b)

    def __str__(self):
        return f"Chord({self.name}, {self.template})"


CHORD_TEMPLATE_DICTIONARY = {}
"""
Maps chord chord_name to keynumber templates.

All templates should be relative to keynumber 0.
"""


def _add(chord_name: str, template: list, comments: str = ""):
    """
    Adds new chord to CHORD_TEMPLATE_DICTIONARY.
    """
    chord = Chord(chord_name, keynumber(template), comments)
    CHORD_TEMPLATE_DICTIONARY[chord_name] = chord


_add("Major", [0, 4, 7])
_add("Major 7", [0, 4, 7, 11])
_add("Dominate 7", [0, 4, 7, 10])
_add("Major 6", [0, 4, 7, 9])
_add("Major sus 2", [0, 2, 7], "Major sustained 2")
_add("Major sus 4", [0, 5, 7], "Major sustained 4")
_add("Major 7 sus 4", [0, 5, 7, 10], "Major 7th sustain 4")
_add("Augmented", [0, 3, 8])
_add("Major 7 aug 5", [0, 3, 8, 11], "Major 7th augmented 5th")
_add("Dominate 7 aug 5", [0, 3, 8, 10], "Dominate 7th augmented 5th")
_add("Diminished", [0, 3, 6])
_add("Diminished 7", [0, 3, 6, 10])
_add("Major 9", [0, 4, 7, 11, 14])
_add("Dominate 9", [0, 4, 7, 10, 14])
_add("Major 6 9", [0, 4, 7, 9, 14])
_add("Major 11", [0, 4, 7, 10, 14, 16])
_add("Major 13", [0, 4, 7, 10, 14, 16, 20])
_add("Major add 9", [0, 4, 7, 14])
_add("Dominate 7 flat 9", [0, 4, 7, 10, 13])
_add("Dominate 7 flat 9 aug 5", [0, 4, 8, 10, 13], "Dom 7 flat 9 augmented 5th")
_add("Dominate 7 sharp 9", [0, 4, 7, 10, 15])
_add("Major 9 aug 5", [0, 4, 8, 10, 14], "Major 9 augmented 5th")
_add("Major 9 dim 5", [0, 4, 6, 10, 14], "Major 9 diminished 5th")
_add("Major 9 sharp 11", [0, 4, 7, 10, 14, 18])
_add("Major 13 flat 9", [0, 4, 7, 10, 13, 17, 21])
_add("Major 13 flat 9 flat 5", [0, 4, 6, 10, 13, 17, 21])
_add("Minor", [0, 3, 7])
_add("Minor sharp 7", [0, 3, 7, 11])
_add("Minor 7", [0, 3, 7, 10])
_add("Minor 6", [0, 3, 7, 9])
_add("Diminished 7", [0, 3, 6, 9])
_add("Minor sharp 9", [0, 3, 7, 11, 14])
_add("Minor 9", [0, 3, 7, 10, 14])
_add("Minor 6 9", [0, 3, 7, 9, 14])
_add("Minor 11", [0, 3, 7, 10, 14, 17])
_add("Minor add 9", [0, 3, 7, 14])
_add("Minor add 11", [0, 3, 7, 17])
_add("whole-5", [0, 2, 4, 6, 8], "5 note whole-tone cluster")
_add("whole-6", [0, 2, 4, 6, 8, 10], "6 note whole-tone cluster")
_add("Cycle minor 3rds", [0, 3, 6, 9])
_add("Cycle major 3rds", [0, 4, 8])
_add("Major" , [0, 4, 7])
_add("Major 7", [0, 4, 7, 11])
_add("Dominate 7", [0, 4, 7, 10])
_add("Major 6", [0, 4, 7, 9])
_add("Major sus 2", [0, 2, 7], "Major sustained 2")
_add("Major sus 4", [0, 5, 7], "Major sustained 4")
_add("Major 7 sus 4", [0, 5, 7, 10], "Major 7th sustain 4")
_add("Augmented", [0, 3, 8])
_add("Major 7 aug 5", [0, 3, 8, 11], "Major 7th augmented 5th")
_add("Dominate 7 aug 5", [0, 3, 8, 10], "Dominate 7th augmented 5th")
_add("Diminished", [0, 3, 6])
_add("Diminished 7", [0, 3, 6, 10])
_add("Major 9", [0, 4, 7, 11, 14])
_add("Dominate 9", [0, 4, 7, 10, 14])
_add("Major 6 9", [0, 4, 7, 9, 14])
_add("Major 11", [0, 4, 7, 10, 14, 16])
_add("Major 13", [0, 4, 7, 10, 14, 16, 20])
_add("Major add 9", [0, 4, 7, 14])
_add("Dominate 7 flat 9", [0, 4, 7, 10, 13])
_add("Dominate 7 flat 9 aug 5", [0, 4, 8, 10, 13], "Dom 7 flat 9 augmented 5th")
_add("Dominate 7 sharp 9", [0, 4, 7, 10, 15])
_add("Major 9 aug 5", [0, 4, 8, 10, 14], "Major 9 augmented 5th")
_add("Major 9 dim 5", [0, 4, 6, 10, 14], "Major 9 diminished 5th")
_add("Major 9 sharp 11", [0, 4, 7, 10, 14, 18])
_add("Major 13 flat 9", [0, 4, 7, 10, 13, 17, 21])
_add("Major 13 flat 9 flat 5", [0, 4, 6, 10, 13, 17, 21])
_add("Minor", [0, 3, 7])
_add("Minor sharp 7", [0, 3, 7, 11])
_add("Minor 7", [0, 3, 7, 10])
_add("Minor 6", [0, 3, 7, 9])
_add("Diminished 7", [0, 3, 6, 9])
_add("Minor sharp 9", [0, 3, 7, 11, 14])
_add("Minor 9", [0, 3, 7, 10, 14])
_add("Minor 6 9", [0, 3, 7, 9, 14])
_add("Minor 11", [0, 3, 7, 10, 14, 17])
_add("Minor add 9", [0, 3, 7, 14])
_add("Minor add 11", [0, 3, 7, 17])
_add("whole-6", [0, 2, 4, 6, 8, 10], "whole-tone cluster")
_add("Cycle minor 3rds", [0, 3, 6, 9])
_add("Cycle major 3rds", [0, 4, 8])
_add("Cycle perfect 4ths", [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
_add("Cycle perfect 5ths", [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77])
_add("Cycle augmented 5ths", [0, 8, 16])
_add("Cycle major 6ths", [0, 9, 18, 27])
_add("Cycle major 7ths", [0, 11, 22, 33, 44, 55], "1/2 cycle of major 7ths")
_add("Cycle minor 7ths", [0, 10, 20, 30, 40, 50], "Cycle of minor 7ths")

CHORD_DICTIONARY = {}
"""
Maps names to Chord objects.

Unlike CHORD_TEMPLATE_DICTIONARY, where all chords are in the key of C, CHORD_DICTIONARY contains chords for all 
keys.  
"""

for (template_name, root) in CHORD_TEMPLATE_DICTIONARY.items():
    for key in range(0, 12):
        text = "%-3s %s" % (keyname(key), template_name)
        note_list = transpose(root.template, key)
        CHORD_DICTIONARY[text] = Chord(text, note_list)

