"""
Defines several generic functions on 'keynumbers'.

At it's most basic, a keynumber is an integer between 0 and 127 inclusive.  Each keynumber has both an int value
and a string representation.  Some keynumbers have two string representations such as d-sharp and e-flat.

The key names have the form: R[#|b][n]

Where R is the root (white) key, one of the upper case letters: A B C D E F or G.

The optional # and b characters indicate a sharp or flat respectively.

The optional n is an octave between 0 and 10.  If not specified the octave is 0.
"""

from simplegeneric import generic

MINIMUM_KEY_NUMBER = 0
MAXIMUM_KEY_NUMBER = 127

TRANSPOSE_OPTIONS = (
    '[ 0]  C',
    '[ 1]  C# / Db',
    '[ 2]  D',
    '[ 3]  D# / Eb',
    '[ 4]  E',
    '[ 5]  F',
    '[ 6]  F# / Gb',
    '[ 7]  G',
    '[ 8]  G# / Ab',
    '[ 9]  A',
    '[10]  A# / Bb',
    '[11]  B')

# Convenience constants
C  = 0
Cs = 1
Db = 1
D  = 2
Ds = 3
Eb = 3
E  = 4
F  = 5
Fs = 6
Gb = 6
G  = 7
Gs = 8
Ab = 8
A  = 9
As = 10
Bb = 10
B  = 11

_pitch_class_map = {
    'C': 0,
    'C#': 1,
    'Db': 1,
    'D': 2,
    'D#': 3,
    'Eb': 3,
    'E': 4,
    'F': 5,
    'F#': 6,
    'Gb': 6,
    'G': 7,
    'G#': 8,
    'Ab': 8,
    'A': 9,
    'A#': 10,
    'Bb': 10,
    'B': 11}

_flat_name_roots = {
    0 : 'C',
    1 : 'Db',
    2 : 'D',
    3 : 'Eb',
    4 : 'E',
    5 : 'F',
    6 : 'Gb',
    7 : 'G',
    8 : 'Ab',
    9 : 'A',
    10 : 'Bb',
    11 : 'B'}

_sharp_name_roots = {
    0 : 'C',
    1 : 'C#',
    2 : 'D',
    3 : 'D#',
    4 : 'E',
    5 : 'F',
    6 : 'F#',
    7 : 'G',
    8 : 'G#',
    9 : 'A',
    10 : 'A#',
    11 : 'B'}


_sharp_name_map = {}
_flat_name_map = {}
_sharp_keynumber_map = {}
_flat_keynumber_map = {}

for kn in range(0, MAXIMUM_KEY_NUMBER + 1):
    octave = str(int(kn / 12))
    pc = kn % 12
    sharp_name = _sharp_name_roots[pc] + octave
    flat_name = _flat_name_roots[pc] + octave
    _sharp_name_map[kn] = sharp_name
    _sharp_keynumber_map[sharp_name] = kn
    _flat_name_map[kn] = flat_name
    _flat_keynumber_map[flat_name] = kn
    _flat_name_map[kn] = flat_name

for pc in range(0, 12):
    sharp_name = _sharp_name_roots[pc]
    flat_name = _flat_name_roots[pc]
    _sharp_name_map[pc] = sharp_name
    _sharp_keynumber_map[sharp_name] = pc
    _flat_name_map[pc] = flat_name
    _flat_keynumber_map[flat_name] = pc


@generic
def keynumber(n: int) -> int:
    """
    Generic function returns corresponding keynumber.
    :param n:  keynumber is defined for int, string and list arguments.
        An in-range int argument is returned directly.
        Out of range int arguments are transposed as needed to be in range and then returned.
        String arguments are converted to corresponding int value.  Invalid names raise a KeyError.
        For list arguments, keynumber is applied to each list element recursively.
    :return: For int and string arguments, returns an int between 0 and 127 inclusive.
        For list arguments returns a list of keynumbers.
    """
    if n < MINIMUM_KEY_NUMBER:
        kn = n % 12
    elif n > MAXIMUM_KEY_NUMBER:
        kn = 108 + n % 12
    else:
        kn = n
    return kn


@keynumber.when_type(str)
def _keynumber_str(s: str) -> int:
    s = s.strip()
    kn = None
    try:
        kn = _sharp_keynumber_map[s]
    except KeyError:
        try:
            kn = _flat_keynumber_map[s]
        except KeyError:
            msg = f"Invalid keyname: {s}"
            raise KeyError(msg)
    return kn


@keynumber.when_type(list)
def _keynumber_list(lst: list) -> list:
    acc = []
    for q in lst:
        acc.append(keynumber(q))
    return acc


@generic
def keyname(s: str, use_flats = False) -> str:
    """
    Generic function returns string representation of keynumber.
    :param s:  keyname is defined for int, string and list arguments.
       For a valid string argument, returns the string directly.  Raises KeyError if string argument is not a valid
       keyname.
       For int argument, converts to corresponding string representation,  Out of bounds integers are transposed
       to a valid range.
       For list arguments, keyname is applied to each element recursively.
    :param use_flats:
       Many keynames have two equivalent 'enharmonic' representations.  If use_flats is True the 'flat' representation
       is used.
    :return:  key template_name or list of key names.
    """
    s = s.strip()
    rs = None
    if use_flats and s in _flat_keynumber_map.keys():
        rs = s
    elif s in _sharp_keynumber_map.keys():
        rs = s
    if not rs:
        msg = f"Invalid keyname: {s}"
        raise KeyError(msg)
    return rs


@keyname.when_type(int)
def _keyname_int(n: int, use_flats = False) -> str:
    kn = keynumber(n)
    if use_flats:
        return _flat_name_map[kn]
    else:
        return _sharp_name_map[kn]


@keyname.when_type(list)
def _keyname_list(lst: list, use_flats = True) -> list:
    acc = []
    for q in lst:
        acc.append(keyname(q, use_flats))
    return acc

@generic
def octave(n: int) -> int:
    """
    Generic function returns octave value of a keynumber.  octave is defined for int, string and list arguments.
    :param n: The keynumber
        If n is an int, it is first transposed to a valid range and then divided by 12.
        String arguments are converted to int using keynumber.
        For list arguments, octave is applied recursively over the list elements.
    :return: An int between 0 and 10 inclusive, or a list of ints.
    """
    return int(keynumber(n) / 12)


@octave.when_type(str)
def _octave_str(s: str) -> int:
    return octave(keynumber(s))


@octave.when_type(list)
def _octave_list(lst: list) -> list:
    acc = []
    for p in lst:
        acc.append(octave(p))
    return acc


@generic
def pitchclass(n: int) -> int:
    """
    Generic function determines the pitchclass of a keynumber.  The pitch is an int between 0 and 11 inclusive.
    :param n: The keynumber.  pitch class is defined for int, string and list arguments.
        For int argument, the keynumber the result is keynumber mod 12.
        String arguments are converted to ints.
        For list arguments, pitchclass is applied recursively to each list element.
    :return: An int between 0 and 11 inclusive or list of ints.
    """
    return keynumber(n) % 12


@pitchclass.when_type(str)
def _pitchclass_str(s: str) -> int:
    return pitchclass(keynumber(s))


@pitchclass.when_type(list)
def _pitchclass_lst(lst: list) -> list:
    acc = []
    for p in lst:
        acc.append(pitchclass(p))
    return acc


@generic
def transpose(n: int, steps: int) -> int:
    """
    Generic function which transposes keynumber by given number of steps.
    :param n: transpose is defined for int, string and list arguments.
       For int arguments the keynumber is transposed by given step count.  Out of bounds results are automatically
       transposed back to a valid keynumber range.
       String arguments are first converted to int.
       For list arguments, transpose is applied recursively to each list element.
    :param steps: Number of transposition steps.
    :return: int in range 0 127 inclusive or list of ints.
    """
    kn0 = keynumber(n) + steps
    return keynumber(kn0)


@transpose.when_type(str)
def _transpose_str(s: str, steps: int) -> int:
    return transpose(keynumber(s), steps)


@transpose.when_type(list)
def _transpose_list(lst: list, steps: int) -> list:
    acc = []
    for p in lst:
        acc.append(transpose(p, steps))
    return acc


@generic
def transpose_pitchclass(n: int, steps: int) -> int:
    """
    Generic function similar to transpose, but the results are always in the lowest octave.
    :param n: Keynumber to transpose, defined for int, string and list arguments.
    :param steps: Number of transpose steps.
    :return: int in range 0, 11 inclusive or list.
    """
    kn = transpose(n, steps)
    return pitchclass(kn)


@transpose_pitchclass.when_type(str)
def _transpose_pc_str(s: str, steps: int) -> int:
    return transpose_pitchclass(keynumber(s), steps)


@transpose_pitchclass.when_type(list)
def _transpose_pc_list(lst: list, steps: int) -> list:
    acc = []
    for p in lst:
        acc.append(transpose_pitchclass(p, steps))
    return acc

